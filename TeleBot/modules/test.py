from TeleBot import pgram as app
from pyrogram import filters


@app.on_message(filters.command("stat") & filters.group)
async def stat(_, message):
    await message.reply_text(f"ᴛᴏᴛᴀʟ ᴍᴇssᴀɢᴇs ɪɴ {message.chat.title} :- {message.id}")
