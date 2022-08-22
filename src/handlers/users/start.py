from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text
from loader import dp

@dp.message_handler(Text(equals='start', ignore_case = True))
@dp.message_handler(CommandStart(), state="*")
async def start(message: types.Message):
    await message.answer(f"Hello 👋, {message.from_user.full_name}!\n\n"
                         f"I'm QrCode Generator Bot 🤖\n"
                         f"I'll help you with that\n\n"
                         f"To get started: /Qr 📍\n\n"
                         f"Привет 👋 , {message.from_user.full_name}!\n\n"
                         f"Я Бот-генератор QR-кодов 🤖 \n"
                         "Я помогу тебе с этим\n\n"
                         f"Для начала работы: /Qr 📍 ")




