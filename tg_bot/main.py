from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from TextReader import read_text
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello!👋🏻\n'
                                                 f'Send me a photo.👀')


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: types.Message):
    bot_answer = await message.answer("Wait a bit!⏳")
    photo = await message.bot.download_file_by_id(file_id=message.photo[-1].file_id)
    text = read_text(photo)
    await bot_answer.delete()
    await message.answer(text)


if __name__ == "__main__":
    executor.start_polling(dp)
