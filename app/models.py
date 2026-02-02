from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Feedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    guest_name: str
    rating: int
    comment: str
    created_at: datetime = Field(default_factory=datetime.utcnow)