from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.database import get_session
from app.schemas import FeedbackCreate, FeedbackRead, FeedbackStats
from app.crud import create_feedback, get_feedbacks, get_feedbacks_stats
from app.models import Feedback

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post(
    "",
    response_model=FeedbackRead,
    status_code=status.HTTP_201_CREATED
)

async def create_feedback_endpoint(
    feedback_in: FeedbackCreate,
    session: AsyncSession = Depends(get_session)
):
    if not 1 <= feedback_in.rating <= 5:
        raise HTTPException(
            status_code = 400,
            datail = "Rating must be between 1 and 5"
        )
    feedback = await create_feedback(session, feedback_in)
    return feedback

@router.get(
    "",
    response_model=List[FeedbackRead]
)

async def get_feedbacks_list(
    skip: int = 0,
    limit: int = 10,
    session: AsyncSession = Depends(get_session)
):
    feedback = await get_feedbacks(session)
    return feedback

@router.get(
    "/stats",
    response_model=FeedbackStats
)
async def get_feedbacks_stats_endpoint(
    session: AsyncSession = Depends(get_session)
):
    stats = await get_feedbacks_stats(session)
    return stats

@router.get(
    "/{feedback_id}",
    response_model=FeedbackRead
)
async def get_feedbacks_by_id(
    feedback_id: int,
    session: AsyncSession = Depends(get_session)
):
    feedback = await session.get(Feedback, feedback_id)

    if not feedback:
        raise HTTPException(
            status_code = 404,
            detail = "Feedback not found"
        )
    return feedback