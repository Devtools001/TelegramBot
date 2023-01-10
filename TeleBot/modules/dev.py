from TeleBot import pgram,DEV_USERS
from pyrogram import filters
from contextlib import suppress
from pyrogram.errors import BadRequest ,Unauthorized

@pgram.on_message(filters.command("leave") & filters.user(DEV_USERS))
async def _leave(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ ʙᴀᴋᴀ.")
    chat_id = message.text.split(None,1)[1].strip()
    if chat_id.startswith("-100"):       
        chat_id = int(chat_id)        
    else:
        return await message.reply_text("ʙᴀᴋᴀᴀᴀ ɪᴛ's ɴᴏᴛ ᴀ ᴄʜᴀᴛ ɪᴅ, ᴄʜᴀᴛ ɪᴅ ɪs ᴀɴ ɪɴᴛᴇɢᴇʀ ɴᴏᴛ ᴀ sᴛʀɪɴɢ.")
    try:    
        await pgram.leave_chat(chat_id)
    except BadRequest:
        return await message.reply_text("ʙᴇᴇᴘ ʙᴏᴏᴘ, I ᴄᴏᴜʟᴅ ɴᴏᴛ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ(ᴅᴜɴɴᴏ ᴡʜʏ ᴛʜᴏ). 🙃")
    with suppress(Unauthorized):
        return await message.reply_text("ʙᴇᴇᴘ ʙᴏᴏᴘ, I ʟᴇғᴛ ᴛʜᴀᴛ sᴏᴜᴘ!.")

