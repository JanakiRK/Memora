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
