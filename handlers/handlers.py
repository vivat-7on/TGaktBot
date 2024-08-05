from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON

main_router = Router()


@main_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        LEXICON['start'])


@main_router.message(CommandStart())
async def process_help_command(message: Message):
    await message.answer(
        LEXICON['help']
    )


@main_router.message(F.document)
async def send_files(message: Message):
    pass


@main_router.message()
async def process_help_command(message: Message):
    await message.answer(
        LEXICON['other']
    )
