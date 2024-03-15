from aiogram import types
from config import Dispatcher

from .handlers import start_cmd, transcript


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start'])
    dp.register_message_handler(transcript, content_types=types.ContentType.VOICE)
