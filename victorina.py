import asyncio
from aiogram import Dispatcher, Bot, types, Router, F
from aiogram.filters import Command
from settings import TG_TOKEN

dp = Dispatcher()

# start_router = Router()

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

    await callback.message.edit_text(f'Вы выбрали тему {callback.data}', reply_markup=keyboard)


async def main():
    bot = Bot(TG_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())