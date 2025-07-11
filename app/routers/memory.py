from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from ..memory import MemoryItem, memory_store

router = APIRouter(prefix="/memory", tags=["Memory"])


class StoreMemoryRequest(BaseModel):
    user_id: str
    llm: str
    content: str


@router.post("/", summary="Store a new memory item")
async def store_memory(request: StoreMemoryRequest) -> dict[str, str]:
    """Persist a new memory entry for a given user and LLM."""
    item = MemoryItem(**request.dict())
    memory_store.add(item)
    return {"status": "stored"}


@router.get("/{user_id}", summary="Retrieve all memory for a user", response_model=List[MemoryItem])
async def read_memory(user_id: str) -> List[MemoryItem]:
    """Get the entire memory timeline for a user."""
    return memory_store.get(user_id) 