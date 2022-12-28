from TeleBot import pgram as app
from pyrogram import filters
from pyrogram.enums import ChatType

from pyrogram.handlers import MessageHandler

async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

@app.on_message(filters.command("hii"))
async def hii(_, message):
    print(message.sender_chat.id)
    print(message.from_user.id)
