from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.db.models import Student, Score
from src.db.session import async_session_factory


async def create_student(user_id: int, first_name: str, last_name: str) -> Student:
    async with async_session_factory() as session:
        student = Student(id=user_id, first_name=first_name, last_name=last_name, is_registered=True)
        session.add(student)
        await session.commit()
        await session.refresh(student)
        return student


async def get_student_by_id(student_id: int):
    async with async_session_factory() as session:
        result = await session.execute(select(Student).where(Student.id == student_id))
        return result.scalar()


async def is_user_registered(user_id: int) -> bool:
    async with async_session_factory() as session:
        result = await session.execute(select(Student).where(Student.id == user_id))
        student = result.scalar()
        return student.is_registered if student else False


async def add_score(student_id: int, subject: str, score: int):
    async with async_session_factory() as session:
        student = await get_student_by_id(student_id)
        if not student:
            return None
        new_score = Score(subject=subject, score=score, student_id=student_id)
        session.add(new_score)
        await session.commit()
        await session.refresh(new_score)
        return new_score


async def get_scores(student_id: int):
    async with async_session_factory() as session:
        result = await session.execute(select(Student).options(joinedload(Student.scores)).where(
            Student.id == student_id)
        )
        student = result.scalar()
        return student.scores if student else None
