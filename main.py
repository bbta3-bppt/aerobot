import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from handlers.register import register_dispatcher


logging.basicConfig(level=logging.INFO)
token = os.getenv('BOT_TOKEN')
bot = Bot(token=token, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)


register_dispatcher(dp)


if __name__ == '__main__':
    print('Starting AeroBot...')
    executor.start_polling(dp, skip_updates=True)
