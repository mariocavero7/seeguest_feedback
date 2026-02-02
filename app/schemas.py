from pydantic import BaseModel, Field
from datetime import datetime

class FeedbackCreate(BaseModel):
    guest_name: str = Field(..., min_length=1)
    rating: int = Field(..., ge=1, le=5)
    comment: str = Field(..., min_length=1)

class FeedbackRead(BaseModel):
    id: int
    guest_name: str
    rating: int
    comment: str
    created_at: datetime

class FeedbackStats(BaseModel):
    average_rating: float
    total_count: int