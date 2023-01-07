from TeleBot import pgram
from pyrogram import filters, enums
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin,
    user_can_ban )

@pgram.on_message(filters.command("kickme"))
@bot_admin
@bot_can_ban
async def _kickme(_, message):
    user_id = message.from_user.id
    chat_id = message.chat.id
 
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)
    if user_id in administrators:
        await message.reply_text("I ᴡɪsʜ I ᴄᴏᴜʟᴅ... ʙᴜᴛ ʏᴏᴜ'ʀᴇ ᴀɴ ᴀᴅᴍɪɴ.")
        return
    
    bam = await pgram.unban_chat_member(chat_id, user_id)
    if bam:
        await message.reply_text("*ᴋɪᴄᴋs ʏᴏᴜ ᴏᴜᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ*")
    else:
        await message.reply_text("Hᴜʜ? I ᴄᴀɴ'ᴛ :/")
        return     
