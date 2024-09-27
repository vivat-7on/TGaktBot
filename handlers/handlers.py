import logging
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import input_file, Message
from pdf2image import convert_from_bytes

from bot_init import bot
from lexicon.lexicon_ru import LEXICON
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
        logging.info(f"Получен документ от пользователя {message.from_user.id}")
        await message.answer(LEXICON['send_files'])
        file = message.document
        file_id = file.file_id
        logging.info(f"Загрузка файла {file.file_name}...")
        file_info = await bot.get_file(file_id)
        downloaded_file = await bot.download_file(
            file_info.file_path,
            timeout=120,
            chunk_size=1024,
        )
        file_bytes = downloaded_file.read()
        logging.info(f"Конвертация файла {file.file_name} в изображения...")
        list_bytes = convert_from_bytes(file_bytes)
        model = load_model()
        if model is None:
            logging.error("Не удалось загрузить модель YOLO.")
            await message.answer(
                "Не фартонуло( Попробуйте загрузить файл ещё раз.")
            return
        logging.info("Получение предсказаний от модели YOLO...")
        predicts = yolo_predicts(model, list_bytes)
        if predicts is None:
            logging.warning("Модель не вернула предсказаний.")
            await message.answer("Не фартонуло( Попробуйте загрузить файл ещё раз.")
            return
        for result in predict_processing(predicts):
            await message.answer(result)
    except Exception as e:
        logging.error(f"Ошибка при обработке документа: {e}")
        await message.answer(
            "Произошла ошибка при обработке вашего документа. Пожалуйста, попробуйте снова.")

@main_router.message()
async def process_help_command(message: Message):
    await message.answer(
        LEXICON['other']
    )
