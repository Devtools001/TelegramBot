from TeleBot import pgram,DEV_USERS
from pyrogram import filters
from contextlib import suppress


@pgram.on_message(filters.command("leave") & filters.user(DEV_USERS))
async def _leave(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ ʙᴀᴋᴀ.")
    chat_id = message.text.split(None,1)[1].strip()
    print(chat_id) 
