from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="6545393934:AAFOhBNw6w6MqSjcDBr9KgHfZdu6qGlJ6W0")
dp = Dispatcher(bot)



if __name__ == "__main__":
    executor.start_polling(dp)