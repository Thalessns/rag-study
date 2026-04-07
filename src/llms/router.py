"""Router for the LLMs module."""

from fastapi import APIRouter

from src.llms.service import LLMsService

router = APIRouter(
    prefix="/llms",
    tags=["LLMs"]
)


@router.get("/")
async def get_llms() -> set[str]:
    """Get available LLMs.
    
    Returns:
        set[str]: Set of available LLMs.
    """
    return await LLMsService.get_available_llms()
