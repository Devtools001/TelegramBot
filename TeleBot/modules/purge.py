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
