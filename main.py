import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers.handlers import main_router

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config: Config = load_config()
    bot_token = config.tg_bot.token
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    dp.include_router(main_router)
    await dp.start_polling(bot)


asyncio.run(main())
