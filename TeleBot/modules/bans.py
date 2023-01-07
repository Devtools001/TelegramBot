from TeleBot import pgram,BOT_ID,DRAGONS,DEV_USERS
from pyrogram import filters, enums
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin,
    user_can_ban )
from TeleBot.modules.pyrogram_funcs.extracting_id import get_id_reason_or_rank

SUPREME_USERS = DEV_USERS + DRAGONS

@pgram.on_message(filters.command("kickme") & ~filters.private)
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
    try:
        await pgram.ban_chat_member(chat_id, user_id)
        await pgram.unban_chat_member(chat_id, user_id)
        await message.reply_text("*ᴋɪᴄᴋs ʏᴏᴜ ᴏᴜᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ*")
    except Exception as error:
        await message.reply_text(error)
       
         
@pgram.on_message(filters.command(["ban","sban"]) & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _ban(_, message):
    user_id , reason = await get_id_reason_or_rank(message, sender_chat=True)
    chat_id = message.chat.id
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)
    if not user_id:
        message.reply_text("I ᴅᴏᴜʙᴛ ᴛʜᴀᴛ's ᴀ ᴜsᴇʀ.")
        return 
    if user_id == BOT_ID:
        await message.reply_text("I ᴄᴀɴ'ᴛ ʙᴀɴ ᴍʏsᴇʟғ, ɪ ᴄᴀɴ ʟᴇᴀᴠᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ.")
        return 
    if user_id in SUPREME_USERS:
        await message.reply_text("ʜᴇ ɪs ᴍʏ ʙʀᴀ, ɪ ᴄᴀɴ'ᴛ ɢᴇᴛ ᴀɢᴀɪɴsᴛ ᴍʏ ʙʀᴀ ᴏᴋ ᴍᴏᴛʜᴇʀ ғ*ᴋᴇʀ")
        return
    if user_id in administrators:
        await message.reply_text(f"ʜᴏᴡ ᴀᴍ I sᴜᴘᴘᴏsᴇᴅ ᴛᴏ ʙᴀɴ ᴀɴ ᴀᴅᴍɪɴ. ᴛʜɪɴᴋ {message.from_user.mention} ᴛʜɪɴᴋ.")
    try :
        mention = (await pgram.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    if message.command == "ban":
        await pgram.ban_chat_member(chat_id, user_id)
        await message.reply_text(f"**🚨 Bᴀɴɴᴇᴅ Usᴇʀ:** {mention}\n**🎎 Bᴀɴɴᴇᴅ Bʏ:** {message.from_user.mention if message.from_user else 'Anon'}\n")
    if message.command == "sban":
        await message.reply_to_message.delete()
        await pgram.ban_chat_member(chat_id, user_id)
 
         
                
            
       
   
        
    
         
