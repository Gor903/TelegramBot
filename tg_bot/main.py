from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from TextReader import read_text

bot = Bot(token="6545393934:AAFOhBNw6w6MqSjcDBr9KgHfZdu6qGlJ6W0")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello!!')


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: types.Message):
    photo = await message.bot.download_file_by_id(file_id=message.photo[-1].file_id)
    text = read_text(photo)
    await message.answer(text)


if __name__ == "__main__":
    executor.start_polling(dp)
