import environ
from aiogram import Bot, types, Dispatcher
from asyncio import run
from aiogram.filters import Command
from aiogram.types import BotCommand
env = environ.Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: types.Message):
    await message.reply("""
    Assalomu aleykum, Get My ID botimizga xush kelibsiz !\nSiz bot orqali o'zingizni va boshqalarni telegram hisobi IDsini aniqlashingiz mumkin.Buning uchun bizga shunchaki xabar yuborishingiz kifoya qiladi.
    """)


@dp.message(Command(commands=['help']))
async def help_command(message: types.Message):
    await message.reply("""
    Bot sizga o'zingizni va boshqalarni telegram hisobining IDsini topishga yordam beradi.
    """)


@dp.message()
async def get_my_id_function(message: types.Message):
    if message.forward_from is not None:
        response = f"""
Sizning hisob ID: {message.chat.id}
Joriy chat ID: {message.chat.id}
Uzatilgan hisob ID: {message.forward_from.id}
        """

        await message.answer(response)
    else:
        response = f"""
Sizning hisob ID: {message.chat.id}
Joriy chat ID: {message.chat.id}
                """

        await message.answer(response)


async def start():
    bot = Bot(BOT_TOKEN)
    await bot.set_my_commands([
        BotCommand(command='/start', description='Botni ishga tushirish'),
        BotCommand(command='/help', description='Yordam')
    ])
    await dp.start_polling(bot, polling_timeout=1)


run(start())