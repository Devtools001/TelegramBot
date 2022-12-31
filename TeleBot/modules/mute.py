import time
import asyncio
from TeleBot import pgram
from pyrogram import filters,enums
from TeleBot import get_readable_time
from pyrogram.types import ChatPermissions
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin,
    user_can_ban )

@pgram.on_message(filters.command(["banall","unbanall","kickall","muteall","unmuteall"]) & filters.group)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def mass_action(_, message):
    chat_id = message.chat.id    
    if message.command[0] == "banall":
        start = time.time()                    
        async for member in pgram.get_chat_members(chat_id):       
            try:
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
           try:
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
            try:
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
            try:
                await pgram.unban_chat_member(chat_id,muted_users[x])    
                x += 1                                                   
            except Exception:
                pass
        await asyncio.sleep(3)
        await text.edit(f"**unᴍᴜᴛᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ**.")            
                              
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
                                                         
    
