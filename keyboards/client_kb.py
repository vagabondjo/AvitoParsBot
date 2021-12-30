from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

button1 = ['Смотреть объявления']
keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard1.add(*button1)
button2 = ['Следующая видеокарты', 'Назад']
keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.add(*button2)
button3 = ['Следующий cpu', 'Назад']
keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard3.add(*button3)
button4 = ['Следующая мат. плата', 'Назад']
keyboard4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard4.add(*button4)
button5 = ['Следующая ОЗУ', 'Назад']
keyboard5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard5.add(*button4)

buttons = ['Видеокарты', 'Процессоры', 'Материнские платы', 'Оперативная память', 'Получать свежие объявления видеокарт']
keyboard_all = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_all.add(*buttons)

inline_button_question = [
    InlineKeyboardButton('Да', callback_data='user_id'),
    InlineKeyboardButton('Нет', callback_data='no')
]

inline_button_video_cards = [
    InlineKeyboardButton('Выдать все видеокарты', callback_data='all_video_cards'),
    InlineKeyboardButton('Выдать последнии пять видеокарт', callback_data='last_five_video_cards')]
inline_kb1 = InlineKeyboardMarkup().add(*inline_button_video_cards)
inline_button_cpu = [
    InlineKeyboardButton('Выдать все cpu', callback_data='all_cpu'),
    InlineKeyboardButton('Выдать последние пять cpu', callback_data='last_five_cpu')
]
inline_kb2 = InlineKeyboardMarkup().add(*inline_button_cpu)
inline_button_motherboard = [
    InlineKeyboardButton('Выдать все мат. платы', callback_data='all_motherboard'),
    InlineKeyboardButton('Выдать последнии пять мат. плат', callback_data='last_five_motherboard')
]
inline_kb3 = InlineKeyboardMarkup().add(*inline_button_motherboard)
inline_button_ram = [
    InlineKeyboardButton('Выдать все ОЗУ', callback_data='all_ram'),
    InlineKeyboardButton('Выдать последнии пять ОЗУ', callback_data='last_five_ram')
]
inline_kb4 = InlineKeyboardMarkup().add(*inline_button_ram)
inline_kb_question2 = [InlineKeyboardButton('Продолжить', callback_data='user_id2')]
inline_kb_question2_kb = InlineKeyboardMarkup().add(*inline_kb_question2)