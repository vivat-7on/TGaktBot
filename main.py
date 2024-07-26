import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        'Привет!\nЯ полезный телеграм бот!\nПришли мне pdf файл\n'
        'и я разделю его для тебя на страницы\nи корвертирую их в jpg')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Пришли мне pdf файл и посмотри что будет'
    )

@dp.message(F.document)
async def send_files(message: Message):
    file = message.document
    await message.answer_document(file.file_id)

@dp.message()
async def process_help_command(message: Message):
    await message.answer(
        'Лучше покажи мне твой акт...'
    )

if __name__ == '__main__':
    dp.run_polling(bot)
