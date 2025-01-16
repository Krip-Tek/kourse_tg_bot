import asyncio
from aiogram import Dispatcher, Bot, types, F
from aiogram.filters import Command
from settings import TG_TOKEN

dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):

    kb = [
        [types.InlineKeyboardButton(text='Меню', callback_data='menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(f'Привет {message.from_user.first_name}\nЭто наша визитка. Ознакомься с меню.',
                         reply_markup=keyboard)


@dp.callback_query(F.data == 'menu')
async def menu_callback(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(text='Кто мы?', callback_data='site_about'),
         types.InlineKeyboardButton(text='Создатели', callback_data='creators')],
        [types.InlineKeyboardButton(text='Как нас найти?', callback_data='site_link'),
         types.InlineKeyboardButton(text='FitBack', callback_data='fitback')],
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'Меню бота\n\n'
                         f'1. Кто мы? - описание нашего сайта.\n'
                         f'2. Как нас найти? - ссылка на наш сайт.\n'
                         f'3. Создатели - почетные разработчики сайта.\n'
                         f'4. FitBack - данные для обратной связи.\n\n'
                         f'Вводи только номер команды.',reply_markup=keyboard)


@dp.callback_query(F.data == 'site_about')
async def site_about_callback(callback: types.CallbackQuery):
    kb = [[
        types.InlineKeyboardButton(text='Назад', callback_data='menu')
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'Мы NeoCorp. Наш сайт занимается предоставлением доступа к приложениям для'
                         f'создания своего персонального помощника.', reply_markup=keyboard)


@dp.callback_query(F.data == 'site_link')
async def site_link_callback(callback: types.CallbackQuery):
    kb = [[
        types.InlineKeyboardButton(text='Назад', callback_data='menu')
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'Наш сайт: www.neocorp.krip.ru', reply_markup=keyboard)


@dp.callback_query(F.data == 'creators')
async def creators_callback(callback: types.CallbackQuery):
    kb = [[
        types.InlineKeyboardButton(text='Назад', callback_data='menu')
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'Царь и баг - создали всё что нас окружает.', reply_markup=keyboard)


@dp.callback_query(F.data == 'fitback')
async def fitback_callback(callback: types.CallbackQuery):
    kb = [[
        types.InlineKeyboardButton(text='Назад', callback_data='menu')
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(f'По всем вопросам обращаться к "Библии" нашего сайта.', reply_markup=keyboard)


@dp.message(F.text == 'Отлично')
async def excelent_handler(message: types.Message):
    await message.answer(f'Ебать ты гений!!!')


async def main():
    bot = Bot(TG_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
