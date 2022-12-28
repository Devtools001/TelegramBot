from TeleBot import pgram as app
from pyrogram import filters
from pyrogram.enums import ChatType

from pyrogram.handlers import MessageHandler

async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

@app.on_message(filters.command("hii"))
async def hii(_, message):
    if message.reply_to_message:
        await app.download_media(message.reply_to_message.photo.file_id,progress=progress)

    
