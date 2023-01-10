from TeleBot import pgram,DEV_USERS
from pyrogram import filters
from contextlib import suppress


@pgram.on_message(filters.command("leave") & filters.user(DEV_USERS))
async def _leave(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ ʙᴀᴋᴀ.")
    chat_id = message.text.split(None,1)[1].strip()
    if not is_int(chat_id):       
        return await message.reply_text("ʙᴀᴋᴀᴀᴀ ɪᴛ's ɴᴏᴛ ᴀ ᴄʜᴀᴛ ɪᴅ, ᴄʜᴀᴛ ɪᴅ ɪs ᴀɴ ɪɴᴛᴇɢᴇʀ ɴᴏᴛ ᴀ sᴛʀɪɴɢ.")
    else:
        chat_id = int(chat_id)
    print(type(chat_id),chat_id)
