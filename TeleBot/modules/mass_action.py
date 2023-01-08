import os 
import time
import asyncio
from TeleBot import pgram,DEV_USERS, DRAGONS
from pyrogram import filters,enums, Client 
from TeleBot import get_readable_time
from pyrogram.types import ChatPermissions
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin,
    user_can_ban )
from pyrogram.enums import UserStatus
from pyrogram.errors import FloodWait
from TeleBot.modules.tagall import SPAM_CHATS


SUPREME_USERS = DEV_USERS + DRAGONS


@pgram.on_message(filters.command(["banall","unbanall","kickall","muteall","unmuteall"]) & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def mass_action(_, message):
    chat_id = message.chat.id  
    SPAM_CHATS.append(chat_id)  
    admins = []    
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        admins.append(m.user.id)
    if message.command[0] == "banall":                   
        start = time.time()                    
        async for member in pgram.get_chat_members(chat_id):   
            if chat_id not in SPAM_CHATS:
                break    
            try:
                if member.user.id in (SUPREME_USERS or admins) :
                    pass
                else:
                    await pgram.ban_chat_member(chat_id, member.user.id)
                    await message.reply_text(f"ғᴜᴄᴋɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴍᴏᴍs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {member.user.mention}") 
                    await asyncio.sleep(3)                      
            except Exception:
                pass
        end = get_readable_time((time.time() - start))  
        await message.reply_text(f"**ᴛɪᴍᴇ ᴛᴀᴋᴇɴ ᴛᴏ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ**\n⏲️ **ᴛɪᴍᴇ** » `{end}`")                
    if message.command[0] == "unbanall":  
        start = time.time()              
        x = 0    
        banned_users = []
        async for m in pgram.get_chat_members(chat_id,filter=enums.ChatMembersFilter.BANNED):
            banned_users.append(m.user.id)
            if chat_id not in SPAM_CHATS:
                break       
            try:               
                await pgram.unban_chat_member(chat_id,banned_users[x])
                await message.reply_text(f"ᴜɴʙᴀɴɪɴɢ ᴀʟʟ ᴍᴄ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {m.user.mention}")
                x += 1
                await asyncio.sleep(3)                                                
            except Exception:
                pass           
        end = get_readable_time((time.time() - start))  
        await message.reply_text(f"**ᴛɪᴍᴇ ᴛᴀᴋᴇɴ ᴛᴏ ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ**\n⏲️ **ᴛɪᴍᴇ** »  `{end}`")
    if message.command[0] == "kickall":                                           
        start = time.time() 
        async for member in pgram.get_chat_members(chat_id):
           if chat_id not in SPAM_CHATS:
                break       
           try:
               if member.user.id in (SUPREME_USERS or admins):
                   pass
               else:
                   await pgram.ban_chat_member(chat_id, member.user.id)
                   await message.reply_text(f"ᴋɪᴄᴋɪɴɢ ᴀʟʟ ᴍᴄ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {member.user.mention}")
                   await pgram.unban_chat_member(chat_id,member.user.id)  
                   await asyncio.sleep(3)                                 
           except Exception:
               pass
        end = get_readable_time((time.time() - start))  
        await message.reply_text(f"**ᴋɪᴄᴋᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.\n🕜 ᴛɪᴍᴇ** »`{end}`")    
    if message.command[0] == "muteall":  
        text = await message.reply("**ᴍᴜᴛɪɴɢ ᴀʟʟ ᴜsᴇʀs**......")      
        async for member in pgram.get_chat_members(chat_id):  
            if chat_id not in SPAM_CHATS:
                break     
            try:
                if member.user.id in (SUPREME_USERS or admins):
                    pass
                else:
                    await pgram.restrict_chat_member(chat_id, member.user.id,ChatPermissions(can_send_messages=False))                                                            
            except Exception:
                pass    
        await asyncio.sleep(3)         
        await text.edit(f"**ᴍᴜᴛᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.**")    
    if message.command[0] == "unmuteall":
        text = await message.reply("**unᴍᴜᴛɪɴɢ ᴀʟʟ ᴜsᴇʀs**......")
        x = 0
        muted_users = []
        async for m in pgram.get_chat_members(chat_id,filter=enums.ChatMembersFilter.RESTRICTED):        
            muted_users.append(m.user.id)    
            if chat_id not in SPAM_CHATS:
                break   
            try:               
                await pgram.unban_chat_member(chat_id,muted_users[x])    
                x += 1                                                   
            except Exception:
                pass
        await asyncio.sleep(3)
        await text.edit(f"**unᴍᴜᴛᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ**.") 
    try :
        SPAM_CHATS.remove(chat_id)
    except Exception:
        pass
       
    
    
@pgram.on_message(filters.command("kickthefools") & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _kickthefools(_,message):      
    text = await message.reply("ᴋɪᴄᴋɪɴɢ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴀ ᴍᴏɴᴛʜ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ")  
    chat_id = message.chat.id
    x = 0
    fools = []    
    ADMINS = []  
    start = time.time()     
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        ADMINS.append(m.user.id)
    
    async for member in pgram.get_chat_members(chat_id) :          
        user = member.user        
        if user.status == UserStatus.LAST_MONTH:
            if user.id in ADMINS :
               pass
            else:                
                fools.append(member.user.id)  
    if not fools:
       await text.edit("ᴛʜᴇʀᴇ ᴀʀᴇɴ'ᴛ ᴀɴʏ ғᴏᴏʟs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ")
    else:
        for i in fools:
            try:                         
                await pgram.ban_chat_member(chat_id,fools[x])           
                await pgram.unban_chat_member(chat_id,fools[x])  
                x += 1                
            except IndexError:
                pass
            except FloodWait as e:
                asyncio.sleep(e.value)
        end = get_readable_time((time.time() - start))  
        await text.delete()
        await message.reply_text(f"ᴋɪᴄᴋᴇᴅ {len(fools)} ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴀ ᴍᴏɴᴛʜ.\n⏰ ᴛɪᴍᴇ ᴛᴏᴏᴋ : {end}")


@pgram.on_message(filters.command("gusers") & ~filters.private)
@user_admin
async def _list(_, message):
    msg = await message.reply("`ɢᴇᴛᴛɪɴɢ ᴜsᴇʀs ʟɪsᴛ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.`")
    count = await pgram.get_chat_members_count(message.chat.id)
    title = message.chat.title 
    mentions = f"ᴜꜱᴇʀꜱ ɪɴ {title}: \n"
    async for member in pgram.get_chat_members(message.chat.id):
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
**⸢ᴀ ᴍᴀss ᴀᴄᴛɪᴏɴ ᴍᴏᴅᴜʟᴇ. ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ɢʀᴏᴜᴘs ɴᴏᴛ ɪɴ ᴘʀɪᴠᴀᴛᴇ.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
「𝗔𝗗𝗠𝗜𝗡𝗦 𝗢𝗡𝗟𝗬」
๏ /banall - ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ
๏ /unbanall - ᴜɴʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ.
๏ /kickall - ᴋɪᴄᴋ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ.
๏ /muteall - ᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ.
๏ /unmuteall - ᴜɴᴍᴜᴛᴇ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ.
═───────◇───────═
"""
__mod_name__ =  "𝙼ᴀss-ᴀᴄᴛɪᴏɴ"
                                                         
    
