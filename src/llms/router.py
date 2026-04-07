"""Router for the LLMs module."""

from fastapi import APIRouter, status

from src.llms.schemas import CompletionRequest, CompletionResponse, LLMInfo
from src.llms.service import LLMsService

llms_router = APIRouter(
    prefix="/llms",
    tags=["llms"]
)


@llms_router.post("/complete", status_code=status.HTTP_201_CREATED)
async def complete(data: CompletionRequest) -> CompletionResponse:
    """Generate content for the given user input.
    
    Args:
        data (CompletionRequest): The user data for the request.
    Returns:
        CompletionResponse: The generated content.
    """
    return await LLMsService.complete(data)


@llms_router.get("/", status_code=status.HTTP_200_OK)
async def get_llms() -> list[LLMInfo]:
    """Get available LLMs.
    
    Returns:
        list[LLMInfo]: List of available LLMs.
    """
    return await LLMsService.get_available_models()


@llms_router.get("/{model_name}", status_code=status.HTTP_200_OK)
async def get_model_info(model_name: str) -> LLMInfo:
    """Get information about a specific LLM.
    
    Args:
        model_name (str): The name of the model to get information about.
    Returns:
        LLMInfo: Information about the specified LLM.
    """
    return await LLMsService.get_model_info(model_name)