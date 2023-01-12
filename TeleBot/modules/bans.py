import html
import time 
from TeleBot import pgram,BOT_ID,DRAGONS,DEV_USERS
from pyrogram import filters, enums
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin,
    user_can_ban )
from TeleBot.modules.pyrogram_funcs.extracting_id import get_id_reason_or_rank,extract_user_id
from TeleBot.helpers.convert import time_converter,convert_time
from contextlib import suppress
from pyrogram.errors import BadRequest 
from TeleBot.helpers.time_checker import get_time, time_string_helper
from pyrogram.types import ChatPermissions



async def extract_time(message, time_val):
    if any(time_val.endswith(unit) for unit in ("m", "h", "d")):
        unit = time_val[-1]
        time_num = time_val[:-1]  # type: str
        if not time_num.isdigit():
            await message.reply_text("Invalid time amount specified.")
            return ""

        if unit == "m":
            bantime = int(time.time() + int(time_num) * 60)
        elif unit == "h":
            bantime = int(time.time() + int(time_num) * 60 * 60)
        elif unit == "d":
            bantime = int(time.time() + int(time_num) * 24 * 60 * 60)
        else:
            # how even...?
            return ""
        return bantime
    else:
        await message.reply_text(
            "Invalid time type specified. Expected m,h, or d, got: {}".format(
                time_val[-1]
            )
        )
        return ""


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
       
         
@pgram.on_message(filters.command(["ban","sban","dban"]) & ~filters.private)
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
        await message.reply_text("I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ ʏᴏᴜ'ʀᴇ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ, ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!")
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
    
    if message.command[0] == "ban":
        await pgram.ban_chat_member(chat_id, user_id)
        await message.reply_text(f"🚨 Bᴀɴɴᴇᴅ Usᴇʀ: {mention}\n🎎 Bᴀɴɴᴇᴅ Bʏ: {message.from_user.mention if message.from_user else 'Anon'}\n")        
    if message.command[0] == "sban":
        await message.delete()
        await message.reply_to_message.delete()
        await pgram.ban_chat_member(chat_id, user_id)
    if message.command[0] == "dban":
        await message.reply_to_message.delete()
        await pgram.ban_chat_member(chat_id, user_id)
        await message.reply_text(f"🚨 Bᴀɴɴᴇᴅ Usᴇʀ: {mention}\n🎎 Bᴀɴɴᴇᴅ Bʏ: {message.from_user.mention if message.from_user else 'Anon'}\n")    
    
            
@pgram.on_message(filters.command("tban") & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _tban(_, message):
    user_id , reason = await get_id_reason_or_rank(message, sender_chat=True)
    chat_id = message.chat.id
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)
    if not user_id:
        await message.reply_text("I ᴅᴏᴜʙᴛ ᴛʜᴀᴛ's ᴀ ᴜsᴇʀ.")
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
         
    if not reason:
        await message.reply_text("You haven't specified a time to ban this user for!")
        return 

    split_reason = reason.split(None, 1)
    time_val = split_reason[0].lower()
    reason = split_reason[1] if len(split_reason) > 1 else ""
    tame = await extract_time(message, time_val)
    try:
        await pgram.ban_chat_member(chat_id,user_id,tame)
        await message.reply_text(            
            f"ʙᴀɴɴᴇᴅ! ᴜsᴇʀ {mention} "
            f"ɪs ɴᴏᴡ ʙᴀɴɴᴇᴅ ғᴏʀ {time_val}.",
            
        )
        return 
    except BadRequest as excp:
        if excp.message == "Reply message not found":
            # Do not reply
            await message.reply_text(
                f"Banned! User will be banned for {time_val}.")
            
            return 
        else:
           await message.reply_text("Well damn, I can't ban that user.")

       
@pgram.on_message(filters.command("unban") & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _unban(_, message):
    chat_id = message.chat.id
    replied = message.reply_to_message
    admin = message.from_user.mention
    user = await extract_user_id(message)
    banned_users = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
        banned_users.append(m.user.id)
    if (replied
        and replied.sender_chat 
        and replied.sender_chat != chat_id):
        await message.reply_text("ʏᴏᴜ ᴄᴀɴɴᴏᴛ ᴜɴʙᴀɴ ᴀ ᴄʜᴀɴɴᴇʟ")
        return
    if not user:
        await message.reply_text("I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ ʏᴏᴜ'ʀᴇ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ, ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!")
        return 
    if user not in banned_users:
        await message.reply_text("ʙʀᴜʜ ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ɴᴏᴛ ʙᴀɴɴᴇᴅ.")
    else :
        try:
            await pgram.unban_chat_member(chat_id,user)
            umention = (await pgram.get_users(user)).mention
            await message.reply_text(f"🍵 ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ : {umention}\n🎎 ᴜɴʙᴀɴɴᴇᴅ ʙʏ : {admin}")
        except BadRequest as ok:
            await message.reply_text(ok)
        
@pgram.on_message(filters.command(["kick","dkick","skick","punch"]) & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _kick(_, message):
    chat_id = message.chat.id    
    user_id = await extract_user_id(message)
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)            

    if not user_id:
        await message.reply_text("I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ ʏᴏᴜ'ʀᴇ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ, ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!")
        return 
    if user_id == BOT_ID:
        await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴍʏsᴇʟғ, ɪ ᴄᴀɴ ʟᴇᴀᴠᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ.")
        return 
    if user_id in SUPREME_USERS:
        await message.reply_text("ʜᴇ ɪs ᴍʏ ʙʀᴀ, ɪ ᴄᴀɴ'ᴛ ɢᴇᴛ ᴀɢᴀɪɴsᴛ ᴍʏ ʙʀᴀ ᴏᴋ ᴍᴏᴛʜᴇʀ ғ*ᴋᴇʀ")
        return 
    if user_id in administrators:
        await message.reply_text(f"ʜᴏᴡ ᴀᴍ ɪ sᴜᴘᴘᴏsᴇᴅ ᴛᴏ ᴋɪᴄᴋ ᴀɴ ᴀᴅᴍɪɴ. ᴛʜɪɴᴋ {message.from_user.mention} ᴛʜɪɴᴋ.")
        return 
    try:
        mention = (await pgram.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )    
    text = f"ᴋɪᴄᴋᴇᴅ\n✨ ᴋɪᴄᴋᴇᴅ ʙʏ: {message.from_user.mention}\n💥 ᴜsᴇʀ: {mention}"
      
    if message.command[0] in ["kick","punch"]:
        try:
            await pgram.ban_chat_member(chat_id,user_id) 
            await pgram.unban_chat_member(chat_id,user_id)
            await message.reply_text(text)
        except BadRequest as err :
            await message.reply_text(err)
    if message.command[0] == "dkick":  
        try:
            await message.reply_to_message.delete()
            await pgram.ban_chat_member(chat_id,user_id) 
            await pgram.unban_chat_member(chat_id,user_id)
            await message.reply_text(text)
        except BadRequest as err :
            await message.reply_text(err) 
    if message.command[0] == "skick":
        try:
            await message.reply_to_message.delete()
            await message.delete()
            await pgram.ban_chat_member(chat_id,user_id) 
            await pgram.unban_chat_member(chat_id,user_id)            
        except BadRequest as err :
            await message.reply_text(err)        
     
@pgram.on_message(filters.command(["mute","dmute","smute"]) & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _kick(_, message):
    chat_id = message.chat.id    
    user_id = await extract_user_id(message)
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)            
    res_users = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
        res_users.append(m.user.id)
    if not user_id:
        await message.reply_text("I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ ʏᴏᴜ'ʀᴇ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ, ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!")
        return 
    if user_id == BOT_ID:
        await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴍʏsᴇʟғ, ɪ ᴄᴀɴ ʟᴇᴀᴠᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ.")
        return 
    if user_id in SUPREME_USERS:
        await message.reply_text("ʜᴇ ɪs ᴍʏ ʙʀᴀ, ɪ ᴄᴀɴ'ᴛ ɢᴇᴛ ᴀɢᴀɪɴsᴛ ᴍʏ ʙʀᴀ ᴏᴋ ᴍᴏᴛʜᴇʀ ғ*ᴋᴇʀ")
        return 
    if user_id in administrators:
        await message.reply_text(f"ʜᴏᴡ ᴀᴍ ɪ sᴜᴘᴘᴏsᴇᴅ ᴛᴏ ᴍᴜᴛᴇ ᴀɴ ᴀᴅᴍɪɴ. ᴛʜɪɴᴋ {message.from_user.mention} ᴛʜɪɴᴋ.")
        return 
    if user_id in res_users:
        await message.reply_text("ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴍᴜᴛᴇᴅ")
        return  
    try:
        mention = (await pgram.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )    
    text = f"*ᴍᴜᴛᴇᴅ*\n✨ ᴍᴜᴛᴇᴅ ʙʏ: {message.from_user.mention}\n💥 ᴜsᴇʀ: {mention}"
      
    if message.command[0] == "mute":
        try:
            await pgram.restrict_chat_member(chat_id,user_id,ChatPermissions())             
            await message.reply_text(text)
        except BadRequest as err :
            await message.reply_text(err)
    if message.command[0] == "dmute":  
        if not message.reply_to_message:
            await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ sᴏᴍᴇᴏɴᴇ's ᴍᴇssᴀɢᴇ ʙᴀʙʏ ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ")
        else:
            try:
                await message.reply_to_message.delete()
                await pgram.restrict_chat_member(chat_id,user_id,ChatPermissions())
                await message.reply_text(text)
            except BadRequest as err :
                await message.reply_text(err) 
    if message.command[0] == "smute":
        if not message.reply_to_message:
            await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ sᴏᴍᴇᴏɴᴇ's ᴍᴇssᴀɢᴇ ʙᴀʙʏ ʙʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ")
        else:
            try:
                await message.delete()
                await message.reply_to_message.delete()
                await pgram.restrict_chat_member(chat_id,user_id,ChatPermissions())            
            except BadRequest as err :
                await message.reply_text(err)        
     
    
@pgram.on_message(filters.command("unmute") & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _unmute(_, message):
    chat_id = message.chat.id
    replied = message.reply_to_message
    admin = message.from_user.mention
    user = await extract_user_id(message)
    res_users = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
        res_users.append(m.user.id)
    if (replied
        and replied.sender_chat 
        and replied.sender_chat != chat_id):
        await message.reply_text("ʏᴏᴜ ᴄᴀɴɴᴏᴛ ᴜɴᴍᴜᴛᴇ ᴀ ᴄʜᴀɴɴᴇʟ")
        return
    if not user:
        await message.reply_text("I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ ʏᴏᴜ'ʀᴇ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ, ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!")
        return 
    if user not in res_users:
        await message.reply_text("ʙʀᴜʜ ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ɴᴏᴛ ᴍᴜᴛᴇᴅ.")
    else :
        try:
            await pgram.unban_chat_member(chat_id,user)
            umention = (await pgram.get_users(user)).mention
            await message.reply_text(f"🍵 ᴜɴᴍᴜᴛᴇᴅ ᴜsᴇʀ : {umention}\n🎎 ᴜɴᴍᴜᴛᴇᴅ ʙʏ : {admin}")
        except BadRequest as ok:
            await message.reply_text(ok)
    


@pgram.on_message(filters.command("gusers") & ~filters.private)
@user_admin
async def _list(_, message):
    msg = await message.reply("`ɢᴇᴛᴛɪɴɢ ᴜsᴇʀs ʟɪsᴛ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.`")
    count = await pgram.get_chat_members_count(message.chat.id)
    title = message.chat.title 
    mentions = f"ᴜꜱᴇʀꜱ ɪɴ {title}: \n"
    async for member in pgram.get_chat_members(message.chat.id.):
        mentions += (
            f"\nᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ {member.user.id}"
            if member.user.is_deleted
            else f"\n{member.user.mention} {member.user.id}"
            )
    
    with open("userslist.txt", "w+") as file:
        file.write(mentions)
    await pgram.send_document(
        message.chat.id,
        "userslist.txt",
        caption=f"`{count}` ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs ɪɴ `{title}`\n"       
    )
    await msg.delete()
    os.remove("userslist.txt")      


__help__ = """
**⸢ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /kickme : ᴘᴜɴᴄʜs ᴛʜᴇ ᴜsᴇʀ ᴡʜᴏ ɪssᴜᴇᴅ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ
「𝗔𝗗𝗠𝗜𝗡𝗦 𝗢𝗡𝗟𝗬」
๏ /ban ᴏʀ /dban <ᴜsᴇʀʜᴀɴᴅʟᴇ> : ʙᴀɴs ᴀ ᴜsᴇʀ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
๏ /sban <ᴜsᴇʀʜᴀɴᴅʟᴇ> : sɪʟᴇɴᴛʟʏ ʙᴀɴ ᴀ ᴜsᴇʀ. ᴅᴇʟᴇᴛᴇs ᴄᴏᴍᴍᴀɴᴅ, ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴅᴏᴇsɴ'ᴛ ʀᴇᴘʟʏ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
๏ /tban <ᴜsᴇʀʜᴀɴᴅʟᴇ> x(m/h/d) : ʙᴀɴs ᴀ ᴜsᴇʀ ғᴏʀ x ᴛɪᴍᴇ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ). ᴍ = ᴍɪɴᴜᴛᴇs, ʜ = ʜᴏᴜʀs, ᴅ = ᴅᴀʏs.
๏ /listbans : ʟɪsᴛ ᴏғ ʙᴀɴɴᴇᴅ ᴜsᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
๏ /unban <ᴜsᴇʀʜᴀɴᴅʟᴇ> :  ᴜɴʙᴀɴs a user. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
๏ /punch <ᴜsᴇʀʜᴀɴᴅʟᴇ> :  Punches a user out of the group, (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
๏ /mute or /dmute <ᴜsᴇʀʜᴀɴᴅʟᴇ> : sɪʟᴇɴᴄᴇs ᴀ ᴜsᴇʀ. ᴄᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, ᴍᴜᴛɪɴɢ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴜsᴇʀ.
๏ /tmute <userhandle> x(m/h/d) : ᴍᴜᴛᴇs a ᴜsᴇʀ ғᴏʀ x ᴛɪᴍᴇ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ). m = ᴍɪɴᴜᴛᴇs, h = ʜᴏᴜʀs, ᴅ = ᴅᴀʏs.
๏ /unmute <userhandle> : ᴜɴᴍᴜᴛᴇs ᴀ ᴜsᴇʀ. ᴄᴀɴ ᴀʟsᴏ ʙᴇ ᴜsᴇᴅ ᴀs ᴀ ʀᴇᴘʟʏ, ᴍᴜᴛɪɴɢ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴜsᴇʀ. 
═───────◇───────═
"""
__mod_name__ = "𝙱ᴀɴs"

