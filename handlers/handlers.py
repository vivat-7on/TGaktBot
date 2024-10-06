import logging
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import input_file, Message
from pdf2image import convert_from_bytes

from bot_init import bot
from lexicon.lexicon_ru import (
    LEXICON,
    LEXICON_HANDLERS_LOGGING,
    LEXICON_HANDLERS_ERROR,
)
from services.yolo import load_model, predict_processing, yolo_predicts

main_router = Router()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


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
    try:
        logging.info(f"{LEXICON_HANDLERS_LOGGING['get_doc']} {message.from_user.id}")
        await message.answer(LEXICON['send_files'])
        file = message.document
        file_id = file.file_id
        logging.info(f"{LEXICON_HANDLERS_LOGGING['loading_file']} {file.file_name}...")
        file_info = await bot.get_file(file_id)
        downloaded_file = await bot.download_file(
            file_info.file_path,
            timeout=120,
            chunk_size=1024,
        )
        file_bytes = downloaded_file.read()
        logging.info(LEXICON_HANDLERS_LOGGING['convert_file'].format(file.file_name))
        list_bytes = convert_from_bytes(file_bytes)
        model = load_model()
        if model is None:
            logging.error(LEXICON_HANDLERS_LOGGING['failed_load_yolo'])
            await message.answer(LEXICON_HANDLERS_ERROR['default_answer'])
            return
        logging.info(LEXICON_HANDLERS_LOGGING['getting_predictions'])
        predicts = yolo_predicts(model, list_bytes)
        if predicts is None:
            logging.warning(LEXICON_HANDLERS_LOGGING['failed_predictions'])
            await message.answer(LEXICON_HANDLERS_ERROR['default_answer'])
            return
        for result in predict_processing(predicts):
            await message.answer(result)
    except Exception as e:
        logging.error(f"Ошибка при обработке документа: {e}")
        await message.answer(LEXICON_HANDLERS_ERROR['doc_processing_err'])

@main_router.message()
async def process_help_command(message: Message):
    await message.answer(
        LEXICON['other']
    )
