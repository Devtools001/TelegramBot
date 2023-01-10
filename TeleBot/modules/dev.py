import os
import asyncio 
from TeleBot import pgram,DEV_USERS,BOT_NAME
from pyrogram import filters
from contextlib import suppress
import subprocess
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
    text = await message.reply("🎣 sᴛᴀʀᴛɪɴɢ ᴀ ɴᴇᴡ ɪɴsᴛᴀɴᴄᴇ ᴀɴᴅ sʜᴜᴛᴛɪɴɢ ᴅᴏᴡɴ ᴛʜɪs ᴏɴᴇ.......")
    await text.delete()
    try:
        os.system(f"kill -9 {os.getpid()} && python3 -m TeleBot")
    except Exception as er:
        print(er)


@pgram.on_message(filters.command(["gitpull", "update"]) & filters.user(DEV_USERS))
async def _gitpull(_, message):
    m = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    if str(m[0]) != "A":
        x = await message.reply_text("**» ғᴇᴛᴄʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ғʀᴏᴍ ʀᴇᴩᴏ ᴀɴᴅ ᴛʀʏɪɴɢ ᴛᴏ ʀᴇsᴛᴀʀᴛ...**")
        return os.system(f"kill -9 {os.getpid()} && python3 -m TeleBot")
    else:
        await message.reply_text(f"**» {BOT_NAME} ɪs ᴀʟʀᴇᴀᴅʏ ᴜᴩ-ᴛᴏ-ᴅᴀᴛᴇ !**")


__mod_name__ = "𝙳ᴇᴠ"

__help__ = """
**⸢ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ʙʏ ᴅᴇᴠ ᴏғ ᴛʜᴇ ʙᴏᴛ ᴏʀ ᴏᴡɴᴇʀ⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /leave : ʟᴇᴀᴠᴇ ᴀ ᴄʜᴀᴛ
๏ /restart : ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
๏ /gitpull , /update : ᴘᴜsʜ ᴛʜᴇ ᴄʜᴀɴɢᴇs ɪɴ ʀᴇᴘᴏ ᴀɴᴅ ʀᴇsᴛᴀʀᴛs.
═───────◇───────═
"""
