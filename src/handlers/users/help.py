from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.dispatcher.filters import Text
from loader import dp

@dp.message_handler(Text(equals='help', ignore_case = True))
@dp.message_handler(CommandHelp(), state="*")
async def show_info(message: types.Message):
    await message.answer('📍 In order to start using the bot: \n'
                         '📍 /Qr - Start \n\n'
                         '📍 Для того, чтобы начать использовать бота:\n'
                         '📍 /Qr - Начать\n', disable_web_page_preview=True)
