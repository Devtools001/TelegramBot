import os
from TeleBot import pgram,DEV_USERS
from pyrogram import filters
from contextlib import suppress
from pyrogram.errors import BadRequest ,Unauthorized

@pgram.on_message(filters.command(["leave","dleave"]) & filters.user(DEV_USERS))
async def _leave(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ ʙᴀᴋᴀ.")
    user_id = message.from_user.id
    chat_id = message.text.split(None,1)[1].strip()
    if chat_id.startswith("-100"):       
        chat_id = int(chat_id)        
    else:
        return await message.reply_text("ʙᴀᴋᴀᴀᴀ ɪᴛ's ɴᴏᴛ ᴀ ᴄʜᴀᴛ ɪᴅ, ᴄʜᴀᴛ ɪᴅ ɪs ᴀɴ ɪɴᴛᴇɢᴇʀ ɴᴏᴛ ᴀ sᴛʀɪɴɢ.")
    if message.command[0] == "leave":
        try:    
            await pgram.leave_chat(chat_id)
        except BadRequest:
            return await message.reply_text("ʙᴇᴇᴘ ʙᴏᴏᴘ, I ᴄᴏᴜʟᴅ ɴᴏᴛ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ(ᴅᴜɴɴᴏ ᴡʜʏ ᴛʜᴏ). 🙃")
        with suppress(Unauthorized):
            return await pgram.send_message(user_id,"ʙᴇᴇᴘ ʙᴏᴏᴘ, I ʟᴇғᴛ ᴛʜᴀᴛ sᴏᴜᴘ!.")
    if message.command[0] == "dleave":
        try:    
            await pgram.leave_chat(chat_id,delete=True)
        except BadRequest:
            return await message.reply_text("ʙᴇᴇᴘ ʙᴏᴏᴘ, I ᴄᴏᴜʟᴅ ɴᴏᴛ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ɢʀᴏᴜᴘ(ᴅᴜɴɴᴏ ᴡʜʏ ᴛʜᴏ). 🙃")
        with suppress(Unauthorized):
            return await pgram.send_message(user_id,"ʙᴇᴇᴘ ʙᴏᴏᴘ, I ʟᴇғᴛ ᴛʜᴀᴛ sᴏᴜᴘ!. ᴀʟsᴏ ᴅᴇʟᴇᴛᴇᴅ ᴛʜᴇ ᴅɪᴀʟᴏɢs.")


@pgram.on_message(filters.command("restart") & filters.user(DEV_USERS))
async def _restart(_, message):
    text = message.reply("sᴛᴀʀᴛɪɴɢ ᴀ ɴᴇᴡ ɪɴsᴛᴀɴᴄᴇ ᴀɴᴅ sʜᴜᴛᴛɪɴɢ ᴅᴏᴡɴ ᴛʜɪs ᴏɴᴇ. 🎣")
    try:
        os.system("restart.bat")
        os.execv("start.bat", sys.argv)
    except Exception as er:
        print(er)

    text.edit("✨ ʀᴇsᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")




