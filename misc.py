import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TOKEN = '2045306418:AAG5j5zuSKhz466lLw8jeg_MQ4dlQfTH3Vg'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)