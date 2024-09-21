from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import input_file, Message
from pdf2image import convert_from_bytes

from bot_init import bot
from lexicon.lexicon_ru import LEXICON
from services.yolo import yolo_predict

main_router = Router()


@main_router.message(CommandStart())
async def process_start_command(message: Message):
    photo_path = 'files/base.png'
    photo = input_file.FSInputFile(photo_path)
    await message.answer(LEXICON['start'])
    await message.answer_photo(photo=photo)


@main_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        LEXICON['help']
    )


@main_router.message(F.document)
async def send_files(message: Message):
    await message.answer(LEXICON['send_files'])
    file = message.document
    file_id = file.file_id
    file_info = await bot.get_file(file_id)
    downloaded_file = await bot.download_file(file_info.file_path)
    file_bytes = downloaded_file.read()
    # images = convert_from_bytes(file_bytes)
    # for image in images:
    results = yolo_predict(convert_from_bytes(file_bytes))
    for resul in results:
        await message.answer(resul)


@main_router.message()
async def process_help_command(message: Message):
    await message.answer(
        LEXICON['other']
    )
