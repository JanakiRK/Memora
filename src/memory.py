from datetime import datetime
from dataclasses import dataclass

@dataclass
class Memory:
    id: str
    content: str
    type: str
    importance: float
    confidence: float
    created_at: datetime
    updated_at: datetime

def create_memory(id: str, content: str, type: str, importance: float, confidence: float, created_at: datetime, updated_at: datetime) -> Memory:
    return Memory(
        id=id,
        content=content,
        type=type,
        importance=importance,
        confidence=confidence,
        created_at=created_at,
        updated_at=updated_at,
    )
