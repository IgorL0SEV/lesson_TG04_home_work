import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random


from gtts import gTTS
import os

from config import TOKEN
from key_home_work import keyb_start, inline_keyb, inline_keyb_2, keyboard_2, inline_keyb_3

import key_home_work as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.text == "Привет")
async def hello_button(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=inline_keyb_2)

@dp.message(F.text == "Пока")
async def bye_button(message: Message):
    await message.answer(f"Пока, {message.from_user.first_name}!")

@dp.message(F.text == 'dynamic')
async def dynamic(message: Message):
   await message.answer("Загрузка дополнительных опций! \n", show_alert=True)
   await message.answer(f"Новые опции доступны Вам, {message.from_user.first_name}!", reply_markup=inline_keyb_3)


@dp.callback_query(F.data == 'more')
async def more(callback: CallbackQuery):
   await callback.answer("Открываем новые опции!", show_alert=True)
   await callback.message.edit_text('Вот новые опции!', reply_markup=await kb.keyboard_2())


@dp.callback_query()
async def handle_callbacks(callback: CallbackQuery):
    # Ответить на callback-запрос
    await callback.answer()
    # Отправить сообщение с текстом, соответствующим callback_data
    await callback.message.answer(callback.data)


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот демонстрирует работу кнопок, \n а также выполняет команды \n /help \n /start")

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Сделайте выбор, {message.from_user.first_name}', reply_markup=keyb_start)







async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())