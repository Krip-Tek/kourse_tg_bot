import asyncio
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
    await message.answer(f'Привет, {message.from_user.first_name}\nЭто веселая викторина.\n\n'
                         f'Выбери одну тему из предложенных.', reply_markup=keyboard)



async def main():
    bot = Bot(TG_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())