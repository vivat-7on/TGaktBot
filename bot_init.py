from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config


config: Config = load_config()
bot_token = config.tg_bot.token


bot = Bot(token=bot_token)
dp = Dispatcher()