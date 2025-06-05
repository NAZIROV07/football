from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_FROM = int(os.getenv("CHANNEL_FROM"))
CHANNEL_TO = int(os.getenv("CHANNEL_TO"))

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.channel_post()
async def repost(message: Message):
    if message.chat.id == CHANNEL_FROM:
        await bot.copy_message(chat_id=CHANNEL_TO, from_chat_id=CHANNEL_FROM, message_id=message.message_id)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
