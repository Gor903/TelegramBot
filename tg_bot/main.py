from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="6545393934:AAFOhBNw6w6MqSjcDBr9KgHfZdu6qGlJ6W0")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello!!')


if __name__ == "__main__":
    executor.start_polling(dp)
