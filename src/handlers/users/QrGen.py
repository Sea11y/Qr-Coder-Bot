import os, shutil
import qrcode
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import InputFile

from loader import dp, bot
from src.states.FSMState import UrlGiv


async def del_png():
    folder = 'your_path' #Deleting files from the specified folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


async def get_qrcode(url, name):
    """Qr Code Generation"""
    qr = qrcode.make(data=url)
    qr.save(stream=f'src/handlers/users/qr_codes/{name}.png')


@dp.message_handler(Text(equals='qr', ignore_case = True))
@dp.message_handler(Command("Qr"))
async def bot_start(message : types.Message):
    await message.answer("Привет 👋!\n\nВведите ссылку, к которой будет отсылать QrCode😃\n\n"
                         "Hello 👋!\n\nEnter the link to which the Qr Code will be sent😃\n\n")
    await UrlGiv.get_link.set()


@dp.message_handler(state=UrlGiv.get_link)
async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['link'] = message.text
        await UrlGiv.next()
        await message.reply('🤔Теперь введите название для файла🤔\n\n'
                            '🤔Now enter a name for the file🤔')


@dp.message_handler(state=UrlGiv.get_name)
async def sending_qrcode(message: types.Message, state: FSMContext):
    try:
    # await message.answer('[+] Processing...')
        async with state.proxy() as data:
            data['name'] = message.text
        png_url = data['link']
        png_name = data['name']
        await get_qrcode(png_url, png_name)
        photo = InputFile(path_or_bytesio=f'src/handlers/users/qr_codes/{png_name}.png')
        await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo)
        await message.answer('🤗Хорошего дня!🤗\n\n'
                             '🤗Have a nice day!🤗')
        await del_png()
    except:
        await del_png()
        await message.answer('😵Произошла ошибка😵\n\n'
                             '😵An error has occurred😵')
    await state.finish()
