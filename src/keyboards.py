from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def unregistered_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/register")]
        ],
        resize_keyboard=True
    )


def registered_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/enter_scores")],
            [KeyboardButton(text="/view_scores")]
        ],
        resize_keyboard=True
    )
