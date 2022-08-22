from aiogram import executor
import src.handlers
from loader import dp
from src.utils.notify_amdins import on_startup_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
