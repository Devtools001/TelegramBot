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
async def _del(_, message):
    if message.sender_chat:
        return
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("**💌 ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʟᴇᴄᴛ ᴡʜᴇʀᴇ ᴛᴏ sᴛᴀʀᴛ ᴘᴜʀɢɪɴɢ ғʀᴏᴍ**.")
    message_id = replied.id + 1
    del_to = message.id
    del_list = []
    for i in range(message_id,del_to):
        del_list.append(i)
        if len(del_list) == 100:
            await pgram.delete_messages(message.chat.id, del_list)
            del_list = []             
            print(del_list)






