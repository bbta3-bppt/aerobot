from aiogram import Dispatcher
from handlers.katakan import katakansebenarnya, siapapembuat


def register_dispatcher(dp: Dispatcher):
    dp.register_message_handler(katakansebenarnya, commands=['katakansebenarnya'])
    dp.register_message_handler(siapapembuat, commands=['siapayangmembuatkamu'])
