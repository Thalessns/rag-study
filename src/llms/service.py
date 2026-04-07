"""Service for the LLMs module."""

from google.genai import Client
from google.genai.errors import ClientError
from chromadb.api.types import QueryResult

from src.llms.exceptions import GeminiAPIErrorException
from src.llms.schemas import (
    CompletionRequest,
    CompletionUsage,
    CompletionResponse,
    LLMInfo,
)


class LLMsService:
    """Service for the LLMs module."""

    client: Client = Client()

    @classmethod
    async def complete(cls, data: CompletionRequest, documents: QueryResult | None) -> CompletionResponse:
        """Generate content for the given user input.

        Args:
            data (CompletionRequest): The user data for the request.
            documents (QueryResult | None): The retrieved documents for the request.

        Returns:
            CompletionResponse: The generated content and usage information.
        """
        await cls._validate_model_use(data.model)
        messages = []
        if documents:
            messages = [{"role": "context", "content": content } for content in documents.get("documents", [])]
        messages.append({"role": "user", "content": data.input})
        response = await cls.client.aio.models.generate_content(
            model=data.model, messages=messages
        )
        texts = []
        for part in response.candidates[0].content.parts:
            texts.append(part.text)
        return CompletionResponse(
            contents=texts,
            usage=CompletionUsage(
                prompt_tokens=response.usage_metadata.prompt_token_count,
                completion_tokens=response.usage_metadata.thoughts_token_count,
                total_tokens=response.usage_metadata.total_token_count,
            ),
        )

    @classmethod
    async def get_available_models(cls) -> list[LLMInfo]:
        """Get available LLMs.

        Returns:
            list[LLMInfo]: List of available LLMs.
        """
        models = []
        for model in await cls.client.aio.models.list():
            models.append(
                LLMInfo(
                    name=model.name.replace("models/", ""),
                    supported_actions=model.supported_actions,
                )
            )
        return models

    @classmethod
    async def get_model_info(cls, model_name: str) -> LLMInfo:
        """Get information about a specific LLM.

        Args:
            model_name (str): The name of the model to get information about.
        Returns:
            LLMInfo: Information about the specified LLM.
        """
        try:
            model = await cls.client.aio.models.get(model=model_name)
        except ClientError as e:
            raise GeminiAPIErrorException(e.code, e.message)
        else:
            return LLMInfo(
                name=model.name.replace("models/", ""),
                supported_actions=model.supported_actions,
            )

    @classmethod
    async def _validate_model_use(cls, model_name: str) -> bool:
        """Validate if the model can be used for the request.

        Args:
            model_name (str): The name of the model to validate.
        Returns:
            bool: True if the model can be used.
        """
        await cls.get_model_info(model_name)
        return True
