from aiogram.filters import BaseFilter
from aiogram.types import Message

from src.crud import is_user_registered


class IsRegisteredFilter(BaseFilter):
    def __init__(self, registered: bool):
        self.registered = registered

    async def __call__(self, message: Message) -> bool:
        user_id = message.from_user.id
        return await is_user_registered(user_id) == self.registered
