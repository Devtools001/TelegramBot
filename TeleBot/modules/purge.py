import time 
from TeleBot import pgram
from pyrogram import filters 
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    user_admin,
    bot_can_del,
    user_can_del)

@pgram.on_message(filters.command(["del","delete"]) & ~filters.private)
@bot_admin
@user_admin
@bot_can_del
@user_can_del
async def _del(_, message):
    if message.sender_chat:
        return
    replied = message.reply_to_message
    chat_id = message.chat.id
    if not replied:
        return await message.reply_text("`ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴅᴇʟᴇᴛᴇ ɪᴛ.`")

    try:
        await pgram.delete_messages(chat_id, replied.id)
        await message.delete()
    except:
        pass        

@pgram.on_message(filters.command("purge"))
@bot_admin
@user_admin
@bot_can_del
@user_can_del
async def _purge(_, message):
    if message.sender_chat:
        return
    start = time.perf_counter()
    replied = message.reply_to_message
    await message.delete()
    if not replied:
        await message.reply_text("**💌 ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʟᴇᴄᴛ ᴡʜᴇʀᴇ ᴛᴏ sᴛᴀʀᴛ ᴘᴜʀɢɪɴɢ ғʀᴏᴍ**.")        
        return 
    
    if len(message.command) > 1 and message.command[1].isdigit():
         _id = replied.id + int(message.command[1])
         if _id > message.id:
            _id = message.id           
    else:
        _id = message.id  

    message_ids = []
    chat_id = message.chat.id
    for message_id in range(replied.id,_id):               
        message_ids.append(message_id)        
        if len(message_ids) == 100:
            await pgram.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True)                        
            message_ids = []
        
    if len(message_ids) > 0:
        await pgram.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True)        
  
    _time = time.perf_counter() - start
    await message.reply_text(f"⏱️ ᴘᴜʀɢᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ɪɴ {_time : 0.2f} sᴇᴄᴏɴᴅ(s)")


__help__ = """
**⸢ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs ɪɴ ᴀ ɢʀᴏᴜᴘ.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /del | /delete : ᴅᴇʟᴇᴛᴇ ᴀ sɪɴɢʟᴇ ᴍᴇssᴀɢᴇ.
๏ /purge : ᴅᴇʟᴇᴛᴇ ᴍᴜʟᴛɪᴘʟᴇ ᴍᴇssᴀɢᴇs.
═───────◇───────═
"""

__mod_name__ = "𝙿ᴜʀɢᴇ"


