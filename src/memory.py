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

def extract_memory(text: str):
    if not text.strip():
        return None

    text = text.strip()
    lower_text = text.lower()

    if "i prefer" in lower_text or "i like" in lower_text or "i love" in lower_text:
        memory_type = "preference"
    elif "my goal" in lower_text or "i want" in lower_text:
        memory_type = "goal"
    elif "i work" in lower_text or "i am" in lower_text:
        memory_type = "fact"
    else:
        return None

    return {
        "content": text,
        "type": memory_type
    }

def build_memory(text: str, memory_id: str):
    extracted = extract_memory(text)

    if extracted is None:
        return None

    now = datetime.now()

    return create_memory(
        id=memory_id,
        content=extracted["content"],
        type=extracted["type"],
        importance=0.8,
        confidence=0.9,
        created_at=now,
        updated_at=now,
    )