from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Feedback
from app.schemas import FeedbackCreate
from sqlalchemy import select, func

async def create_feedback(
    session: AsyncSession,
    feedback_in: FeedbackCreate
) -> Feedback:
    feedback = Feedback(
        guest_name=feedback_in.guest_name,
        rating=feedback_in.rating,
        comment=feedback_in.comment
    )

    session.add(feedback)
    await session.commit()
    await session.refresh(feedback)

    return feedback

async def get_feedbacks(session: AsyncSession) :
    result = await session.execute(select(Feedback).order_by(Feedback.created_at.desc()))
    return result.scalars().all();

async def get_feedbacks_stats(session: AsyncSession) :
    stmt = select(
        func.avg(Feedback.rating),
        func.count(Feedback.id)
    )
    result = await session.execute(stmt)
    avg_rating, count = result.one()

    return {
        "average_rating": round(float(avg_rating), 2) if avg_rating is not None else 0.0,
        "total_count": count
    }

async def get_feedbacks_by_id(
    session: AsyncSession,
    feedback_id: int
): 
    result = await session.execute(
        select(Feedback).where(Feedback.id == feedback_id)
    )
    return result.scalar_one_or_one()
    