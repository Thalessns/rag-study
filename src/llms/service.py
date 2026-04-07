"""Service for the LLMs module."""

from google.genai import Client


class LLMsService:
    """Service for the LLMs module."""

    client: Client = Client()

    @classmethod
    async def complete(cls, data: BaseModel) -> Any:
        """Generate content for the given user input.
        
        Args:
            data (BaseModel): The user data for the request.
        """
        response = cls.client.aio.models.generate_content(
            model=data.model, contents=data.contents
        )
        return response
