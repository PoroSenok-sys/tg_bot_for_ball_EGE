from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from src.crud import add_score, get_scores
from src.filters import IsRegisteredFilter
from src.keyboards import registered_keyboard

router = Router()


class EnterScoreStates(StatesGroup):
    waiting_for_subject = State()
    waiting_for_score = State()


@router.message(Command("enter_scores"), IsRegisteredFilter(registered=True))
async def enter_scores_command(message: types.Message, state: FSMContext):
    await message.answer("Введите название предмета")
    await state.set_state(EnterScoreStates.waiting_for_subject)


@router.message(EnterScoreStates.waiting_for_subject, IsRegisteredFilter(registered=True))
async def process_subject(message: types.Message, state: FSMContext):
    await state.update_data(subject=message.text)
    await message.answer("Введите балл за этот предмет")
    await state.set_state(EnterScoreStates.waiting_for_score)


@router.message(EnterScoreStates.waiting_for_score, IsRegisteredFilter(registered=True))
async def process_score(message: types.Message, state: FSMContext):
    try:
        score = int(message.text)
        if score < 0 or score > 100:
            raise ValueError("Баллы должны быть в диапазоне от 0 до 100")
    except ValueError:
        await message.answer("Пожалуйста, введите корректный балл от 0 до 100")
        return

    # Получаем данные из состояния
    data = await state.get_data()
    subject = data["subject"]

    user_id = message.from_user.id

    # Сохраняем балл в базу данных
    new_score = await add_score(student_id=user_id, subject=subject, score=score)
    await message.answer(f"Баллы за предмет '{subject}' сохранены",
                         reply_markup=registered_keyboard())

    await state.clear()


@router.message(Command("view_scores"), IsRegisteredFilter(registered=True))
async def view_scores_command(message: types.Message):
    scores = await get_scores(student_id=message.from_user.id)
    if not scores:
        await message.answer("У вас пока нет сохранённых баллов")
        return

    # Формируем ответ
    response = "Ваши баллы ЕГЭ:\n"
    for score in scores:
        response += f"{score.subject}: {score.score}\n"
    await message.answer(response, reply_markup=registered_keyboard())
