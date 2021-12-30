import json
import logging
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from main import get_first_desc_video_cards, get_first_desc_cpu, get_first_desc_motherboard, get_first_desc_ram, check_video_cards_desc_update
from main import desc_title_video_cards_bot, desc_price_video_cards_bot, desc_data_video_cards_bot, \
    desc_url_video_cards_bot, desc_title_cpu_bot, desc_price_cpu_bot, desc_data_cpu_bot, desc_url_cpu_bot, \
    desc_title_motherboard_bot, desc_price_motherboard_bot, desc_data_motherboard_bot, desc_url_motherboard_bot, \
    desc_title_ram_bot, desc_price_ram_bot, desc_data_ram_bot, desc_url_ram_bot

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, ReplyKeyboardMarkup, \
    message
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text, Command
from aiogram.utils.markdown import hlink, hbold, hunderline
from config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import keyboard2, keyboard3, keyboard4, keyboard5, keyboard_all, inline_kb1, inline_kb2, \
    inline_kb3, inline_kb4, inline_button_question, inline_kb_question2_kb

s = 0

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
storage = MemoryStorage()


@dp.message_handler(Command(commands='start'))
async def welcome_say(message: types.Message):
    """Приветсвие пользователя"""
    await message.answer('Привет, нажми на кнопку что бы смотреть объявления', reply_markup=keyboard_all)


@dp.message_handler(Text(equals='Назад'))
async def welcome_say(message: types.Message):
    """Возвращяем пользователя на стартовый хэндлер"""
    await message.answer('Нажми на кнопку что бы смотреть объявления', reply_markup=keyboard_all)


@dp.message_handler(Text(equals='Видеокарты'))
async def desc_video_cards_say(message: types.Message):
    """Начальная поочередная выдача объявлений"""
    get_first_desc_video_cards()
    global s
    await message.answer(f'{hlink(desc_title_video_cards_bot[s], desc_url_video_cards_bot[s])}\n'
                         f'{hbold(desc_price_video_cards_bot[s])}\n'
                         f'{hunderline(desc_data_video_cards_bot[s])}\n', reply_markup=keyboard2)
    await message.answer('Выдать все или последние пять видеокарт ?', reply_markup=inline_kb1)
    s += 1


@dp.message_handler(Text(equals='Следующая видеокарты'))
async def desc_video_cards_say(message: types.Message):
    """Поочередная выдача объявлений"""
    global s
    await message.answer(f'{hlink(desc_title_video_cards_bot[s], desc_url_video_cards_bot[s])}\n'
                         f'{hbold(desc_price_video_cards_bot[s])}\n'
                         f'{hunderline(desc_data_video_cards_bot[s])}\n', reply_markup=keyboard2)
    s += 1


@dp.callback_query_handler(text="all_video_cards")
async def all_video_cards_desc_say(callback: types.CallbackQuery):
    """Получаем все объявления видеокарт"""
    get_first_desc_video_cards()
    with open('db/video_cards.json', encoding='utf-8') as file:
        desc_dict = json.load(file)

    for k, v in sorted(desc_dict.items()):
        desc = f"{hlink(v['title'], v['url'])}\n" \
               f"{hbold(v['price'])}\n" \
               f"{hunderline(v['data'])}\n"
        await callback.message.answer(desc)
        await callback.answer()


@dp.callback_query_handler(text='last_five_video_cards')
async def last_five_video_cards_desc_say(callback: types.CallbackQuery):
    """Получаем последние пять объявлений видеокарт"""
    get_first_desc_video_cards()
    with open('db/video_cards.json', encoding='utf-8') as file:
        desc_dict = json.load(file)

    for k, v in sorted(desc_dict.items())[-5:]:
        desc = f"{hlink(v['title'], v['url'])}\n" \
               f"{hbold(v['price'])}\n" \
               f"{hunderline(v['data'])}\n"
        await callback.message.answer(desc)


@dp.message_handler(Text(equals='Процессоры'))
async def desc_say(message: types.Message):
    """Начальная поочередная выдача объявлений процессоров"""
    get_first_desc_cpu()
    global s
    await message.answer(f'{hlink(desc_title_cpu_bot[s], desc_url_cpu_bot[s])}\n'
                         f'{hbold(desc_price_cpu_bot[s])}\n'
                         f'{hunderline(desc_data_cpu_bot[s])}\n', reply_markup=keyboard3)
    await message.answer('Выдать все или последние пять процессоров ?', reply_markup=inline_kb2)
    s += 1


@dp.message_handler(Text(equals='Следующий cpu'))
async def desc_say(message: types.Message):
    """Поочередная выдача объявлений процессоров"""
    global s
    await message.answer(f'{hlink(desc_title_cpu_bot[s], desc_url_cpu_bot[s])}\n'
                         f'{hbold(desc_price_cpu_bot[s])}\n'
                         f'{hunderline(desc_data_cpu_bot[s])}\n', reply_markup=keyboard3)
    s += 1


@dp.callback_query_handler(text="all_cpu")
async def all_desc_say(callback: types.CallbackQuery):
    """Получаем все объявления процессоров"""
    get_first_desc_cpu()
    with open('db/cpu.json', encoding='utf-8') as file:
        desc_dict = json.load(file)

    for k, v in sorted(desc_dict.items()):
        desc = f"{hlink(v['title'], v['url'])}\n" \
               f"{hbold(v['price'])}\n" \
               f"{hunderline(v['data'])}\n"
        await callback.message.answer(desc, reply_markup=keyboard3)
        await callback.answer()
        if message == 'stop':
            break
        else:
            continue


@dp.callback_query_handler(text='last_five_cpu')
async def all_desc_say(callback: types.CallbackQuery):
    """Получаем последние пять объявлений процессоров"""
    get_first_desc_cpu()
    with open('db/cpu.json', encoding='utf-8') as file:
        desc_dict = json.load(file)

    for k, v in sorted(desc_dict.items())[-5:]:
        desc = f"{hlink(v['title'], v['url'])}\n" \
               f"{hbold(v['price'])}\n" \
               f"{hunderline(v['data'])}\n"
        await callback.message.answer(desc, reply_markup=keyboard3)


@dp.message_handler(Text(equals='Материнские платы'))
async def desc_say(message: types.Message):
    """Начальная поочередная выдача объявлений мат. плат"""
    get_first_desc_motherboard()
    global s
    await message.answer(f'{hlink(desc_title_motherboard_bot[s], desc_url_motherboard_bot[s])}\n'
                         f'{hbold(desc_price_motherboard_bot[s])}\n'
                         f'{hunderline(desc_data_motherboard_bot[s])}\n', reply_markup=keyboard4)
    await message.answer('Выдать все или последние пять мат. плат ?', reply_markup=inline_kb3)
    s += 1


@dp.message_handler(Text(equals='Следующая мат. плата'))
async def desc_say(message: types.Message):
    """Поочередная выдача объявлений мат. плат"""
    global s
    await message.answer(f'{hlink(desc_title_motherboard_bot[s], desc_url_motherboard_bot[s])}\n'
                         f'{hbold(desc_price_motherboard_bot[s])}\n'
                         f'{hunderline(desc_data_motherboard_bot[s])}\n', reply_markup=keyboard4)
    s += 1


@dp.callback_query_handler(text="all_motherboard")
async def all_desc_say(callback: types.CallbackQuery):
    """Получаем все объявления мат. плат"""
    get_first_desc_motherboard()
    with open('db/motherboard.json', encoding='utf-8') as file:
        desc_dict = json.load(file)

    for k, v in sorted(desc_dict.items()):
        desc = f"{hlink(v['title'], v['url'])}\n" \
               f"{hbold(v['price'])}\n" \
               f"{hunderline(v['data'])}\n"
        await callback.message.answer(desc)
        await callback.answer()


@dp.callback_query_handler(text='last_five_motherboard')
async def all_desc_say(callback: types.CallbackQuery):
    """Получаем последние пять объявлений мат. плат"""
    get_first_desc_motherboard()
    with open('db/motherboard.json', encoding='utf-8') as file:
        desc_dict = json.load(file)

    for k, v in sorted(desc_dict.items())[-5:]:
        desc = f"{hlink(v['title'], v['url'])}\n" \
               f"{hbold(v['price'])}\n" \
               f"{hunderline(v['data'])}\n"
        await callback.message.answer(desc)


@dp.message_handler(Text(equals='Оперативная память'))
async def desc_say(message: types.Message):
    """Начальная поочередная выдача объявлений оперативной памяти"""
    get_first_desc_ram()
    global s
    await message.answer(f'{hlink(desc_title_ram_bot[s], desc_url_ram_bot[s])}\n'
                         f'{hbold(desc_price_ram_bot[s])}\n'
                         f'{hunderline(desc_data_ram_bot[s])}\n', reply_markup=keyboard5)
    await message.answer('Выдать все или последние пять ОЗУ ?', reply_markup=inline_kb4)
    s += 1


@dp.message_handler(Text(equals='Следующая ОЗУ'))
async def desc_say(message: types.Message):
    """Поочередная выдача объявлений оперативной памяти"""
    global s
    await message.answer(f'{hlink(desc_title_ram_bot[s], desc_url_ram_bot[s])}\n'
                         f'{hbold(desc_price_ram_bot[s])}\n'
                         f'{hunderline(desc_data_ram_bot[s])}\n', reply_markup=keyboard5)
    s += 1


@dp.callback_query_handler(text="all_ram")
async def all_desc_say(callback: types.CallbackQuery):
    """Получаем все объявления оперативной памяти"""
    get_first_desc_ram()
    with open('db/ram.json', encoding='utf-8') as file:
        desc_dict = json.load(file)

    for k, v in sorted(desc_dict.items()):
        desc = f"{hlink(v['title'], v['url'])}\n" \
               f"{hbold(v['price'])}\n" \
               f"{hunderline(v['data'])}\n"
        await callback.message.answer(desc)
        await callback.answer()


@dp.callback_query_handler(text='last_five_ram')
async def all_desc_say(callback: types.CallbackQuery):
    """Получаем последние пять объявлений оперативной памяти"""
    get_first_desc_ram()
    with open('db/ram.json', encoding='utf-8') as file:
        desc_dict = json.load(file)

    for k, v in sorted(desc_dict.items())[-5:]:
        desc = f"{hlink(v['title'], v['url'])}\n" \
               f"{hbold(v['price'])}\n" \
               f"{hunderline(v['data'])}\n"
        await callback.message.answer(desc)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(desc_every_minute())
    executor.start_polling(dp)
