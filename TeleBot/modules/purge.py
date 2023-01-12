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
        







