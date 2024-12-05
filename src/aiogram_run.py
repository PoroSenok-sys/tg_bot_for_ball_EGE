import asyncio
from src.create_bot import bot, dp, set_bot_commands
from src.handlers.start_handlers import router as router_start
from src.handlers.menu_handlers import router as router_menu


async def main():
    dp.include_router(router_start)
    dp.include_router(router_menu)
    await bot.delete_webhook(drop_pending_updates=True)
    await set_bot_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
