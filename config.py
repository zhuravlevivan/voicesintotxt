from environs import Env
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
env: Env = Env()
env.read_env()

bot = Bot(token=env('TOKEN'))
dp = Dispatcher(bot, storage=storage)
