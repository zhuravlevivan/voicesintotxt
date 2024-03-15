from aiogram.utils import executor
from handlers import register_mh
from config import dp


async def on_startup(_):
    print('Bot Online')

register_mh.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
