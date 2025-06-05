import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ChatType
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import BaseFilter

API_TOKEN = '7790903467:AAGSnh4euRb2iItn1MsmWKRqavuqNj62i2U'
SOURCE_CHANNEL_ID = -1002879419379  # ID канала-источника
TARGET_CHANNEL_ID = -1002727712840  # ID канала-приёмника

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Фильтр: только сообщения из нужного канала
class SourceChannelFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.id == SOURCE_CHANNEL_ID

@dp.channel_post(SourceChannelFilter())
async def forward_channel_post(message: Message):
    await bot.copy_message(
        chat_id=TARGET_CHANNEL_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
