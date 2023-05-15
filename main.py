from aiogram import Bot
from aiogram.types import *
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher 
from core.config import TOKEN
from core.utils import password_generator

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(text= 'Здравствуйте, этот бот предназначен для генерация пароля. Пожалуйста, укажите длину вашего пароля')

@dp.message_handler(content_types=ContentTypes.TEXT)
async def send_password(message: Message):
    if message.text.isdigit():
        password = password_generator(message.text)
        await message.answer(text=password)
    else:
        await message.answer(text='Пожалуйста введите число')


if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    except(KeyboardInterrupt, SystemExit):
        pass