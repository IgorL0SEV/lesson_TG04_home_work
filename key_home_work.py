from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


keyb_start = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Привет"), KeyboardButton(text="Пока"), KeyboardButton(text="dynamic")]
        ], resize_keyboard=True)


inline_keyb = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Привет", callback_data="hello")],
   [InlineKeyboardButton(text="Продолжим общение", callback_data="links")],
   [InlineKeyboardButton(text="Пока", callback_data="bye")]
])


inline_keyb_2 = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Новости", url="https://lenta.ru")],
            [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru")],
            [InlineKeyboardButton(text="Видео", url="https://www.youtube.com")]
        ]
    )

inline_keyb_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data='more')]
])

text_1 = "Текст для опции 1"
text_2 = "Текст для опции 2"
test = [("Опция 1", text_1), ("Опция 2", text_2)]

async def keyboard_2():
    keyboard = InlineKeyboardBuilder()
    for key, callback_data in test:
        keyboard.add(InlineKeyboardButton(text=key, callback_data=callback_data))
    return keyboard.adjust(2).as_markup()

