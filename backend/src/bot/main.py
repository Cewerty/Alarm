from aiogram import Bot, types, Dispatcher
import asyncio
from keyboards import start_panel_cb

bot = Bot(token="5508982075:AAELN1Kko7vHkNRmu8HCpPTk4CbDRsITkOs")
dp = Dispatcher()


@dp.message()
async def start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=start_panel_cb(True))
    
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('Goida!')
    asyncio.run(main())