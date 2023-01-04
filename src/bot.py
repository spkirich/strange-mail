import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from box import Box

# Токен Telegram-бота.
TOKEN = os.environ["SM_TOKEN"]

USERS = (
    int(os.environ["SM_USER1"]),
    int(os.environ["SM_USER2"]),
)

GREETINGS = """Добро пожаловать на Странную почту!

Отправь сообщение, и оно обязательно достигнет адресата...
Когда-нибудь )

А чтобы читать сообщения, адресованные тебе, пользуйся командой /fetch
"""

# Telegram-бот.
bot = Bot(token=TOKEN)

# Диспетчер Telegram-бота.
dispatcher = Dispatcher(bot)

boxes = {
    USERS[0]: Box("data", f"{USERS[0]}.json"),
    USERS[1]: Box("data", f"{USERS[1]}.json"),
}


@dispatcher.message_handler(commands=["start"])
async def handle_command_start(message: types.Message):
    """Обработать команду /start."""

    await message.answer(GREETINGS)


@dispatcher.message_handler(commands=["fetch"])
async def handle_command_fetch(message: types.Message):
    """Обработать команду /fetch."""

    await message.answer(boxes[message.from_id].get())


@dispatcher.message_handler()
async def handle_message(message: types.Message):
    """Обработать сообщение."""

    if message.from_id == USERS[0]:
        user = USERS[1]

    if message.from_id == USERS[1]:
        user = USERS[0]

    boxes[user].put(message.text)


if __name__ == "__main__":
    executor.start_polling(dispatcher)
