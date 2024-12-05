from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from src.crud import create_student
from src.filters import IsRegisteredFilter
from src.keyboards import unregistered_keyboard, registered_keyboard

router = Router()


class RegisterStates(StatesGroup):
    waiting_for_name = State()


@router.message(Command("start"), IsRegisteredFilter(registered=False))
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать! Введите /register, чтобы зарегистрироваться",
                         reply_markup=unregistered_keyboard())


@router.message(Command("register"), IsRegisteredFilter(registered=False))
async def register_command(message: types.Message, state: FSMContext):
    await message.answer("Введите ваше имя и фамилию через пробел")
    await state.set_state(RegisterStates.waiting_for_name)


@router.message(RegisterStates.waiting_for_name, IsRegisteredFilter(registered=False))
async def process_registration(message: types.Message, state: FSMContext):
    name_parts = message.text.split()
    if len(name_parts) != 2:
        await message.answer("Пожалуйста, введите имя и фамилию через пробел")
        return
    user_id = message.from_user.id
    student = await create_student(user_id, name_parts[0], name_parts[1])
    await message.answer(f"Регистрация завершена! Ваш ID: {student.id}",
                         reply_markup=registered_keyboard())
    await state.clear()
