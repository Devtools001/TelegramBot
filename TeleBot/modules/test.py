from TeleBot import pgram as app
from pyrogram import filters
from pyrogram.enums import ChatType

from pyrogram.handlers import MessageHandler

async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")

@app.on_message(filters.command("hii"))
async def hii(_, message):
    a = "BAACAgUAAxkBAAIL92OsCoRS4TIx_8g7ffRf6LYRgMCoAAJkCAAC5clgVZGuzEuQfZLYHgQ"
    if message.reply_to_message:
        await app.download_media(a,progress=progress)
        await message.reply_text(str(message.reply_to_message.video.file_id))

    
