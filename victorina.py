import asyncio
import json

from aiogram import Dispatcher, Bot, types, F
from aiogram.filters import Command
from settings import TG_TOKEN

dp = Dispatcher()



@dp.message(Command('start'))
async def start_command(message: types.Message)-> None:

    kb = [
        [types.InlineKeyboardButton(text='Меню', callback_data='menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(f'Привет, {message.from_user.first_name}\n'
                            f'Сыграем?', reply_markup=keyboard)

@dp.callback_query(F.data == 'menu')
async def menu_callback(callback: types.CallbackQuery)-> None:
    kb = [
        [types.InlineKeyboardButton(text='Темы', callback_data='themes')],
        [types.InlineKeyboardButton(text='Помощь', callback_data='help')]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'Это веселая викторина.\n'
                         f'Можешь выбрать Тему либо изучить правила.', reply_markup=keyboard)

@dp.callback_query(F.data == 'help')
async def help_callback(callback :types.CallbackQuery) -> None:

    kb = [
        [types.InlineKeyboardButton(text='Назад', callback_data='menu')]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'Данная викторина содержит 4 темы по 10 вопросов в каждой.\n'
                            f'Вопросы каждый раз подбираются случайно.\n'
                            f'Вам будет предложено по 4 варианта ответа,\n'
                            f'Если ваш ответ верный, то вы получаете один бал.\n'
                            f'В конце викторины будет сообщение о количестве правильных ответов.\n\n'
                            f'Соревнуйтесь с друзьями и набирайте больше очков. Удачи!', reply_markup=keyboard)


@dp.callback_query(F.data == 'themes')
async def menu_callback(callback: types.CallbackQuery) -> None:
    kb = [
        [types.InlineKeyboardButton(text='Горы', callback_data='mountain'),
         types.InlineKeyboardButton(text='Города', callback_data='city')],
        [types.InlineKeyboardButton(text='Страны', callback_data='country'),
         types.InlineKeyboardButton(text='Реки', callback_data='river')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)

    await callback.message.edit_text(f'Выберите одну из тем',reply_markup=keyboard)


@dp.callback_query(F.data.in_(['mountain', 'city', 'country', 'river']))
async def theme_check_callback(callback: types.CallbackQuery) -> None:
    kb = [
        [types.InlineKeyboardButton(text='Назад', callback_data='themes')]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    if callback.data == 'mountain':
        await callback.message.edit_text(f'Вы выбрали тему Горы', reply_markup=keyboard)
    elif callback.data == 'city':
        await callback.message.edit_text(f'Вы выбрали тему Города', reply_markup=keyboard)
    elif callback.data == 'country':
        await callback.message.edit_text(f'Вы выбрали тему Страны', reply_markup=keyboard)
    elif callback.data == 'river':
        await callback.message.edit_text(f'Вы выбрали тему Реки', reply_markup=keyboard)

data = {

}
with open('questions.json', 'a+', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


async def main():
    bot = Bot(TG_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())