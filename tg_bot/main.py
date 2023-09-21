from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from TextReader import read_text
from dotenv import load_dotenv
from DataBase import DataBase
import os

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)
db = DataBase(
    os.getenv('HOST'),
    os.getenv('PORT'),
    os.getenv('DATABASE'),
    os.getenv('DB_USER'),
    os.getenv('DB_PASSWORD'),
)
languages = {
    'English': 'en',
    'Russian': 'ru',
}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello!👋🏻\n'
                                                 f'Send me a photo.👀\n'
                                                 f"/language ➡️ to change text's language.")
    if db.get_language(message.from_user.id) is None:
        db.add_user(message.from_user.id)


@dp.message_handler(commands=['language'])
async def language(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, selective=True)
    keyboard.add(
        types.KeyboardButton('English'),
        types.KeyboardButton('Russian'),
    )
    await message.answer('Choose language.🌎', reply_markup=keyboard)


@dp.message_handler()
async def language_handler(message: types.Message):
    if message.text in languages.keys():
        db.update_user_data(message.from_user.id, languages[message.text])
        await message.answer('👍🏻')


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: types.Message):
    bot_answer = await message.answer("Wait a bit!⏳")
    photo = await message.bot.download_file_by_id(file_id=message.photo[-1].file_id)
    text = read_text(photo, db.get_language(message.from_user.id))
    await bot_answer.delete()
    await message.answer(text)


if __name__ == "__main__":
    executor.start_polling(dp)
