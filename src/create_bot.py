import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand

from src.db.session import settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def set_bot_commands(loc_bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать работу"),
        BotCommand(command="/register", description="Регистрация"),
        BotCommand(command="/enter_scores", description="Ввести баллы ЕГЭ"),
        BotCommand(command="/view_scores", description="Просмотреть баллы ЕГЭ"),
    ]
    await loc_bot.set_my_commands(commands)
