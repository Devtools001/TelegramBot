import time
import asyncio
from TeleBot import pgram
from pyrogram import filters,enums
from functools import wraps
from TeleBot import BOT_ID,get_readable_time
from pyrogram.enums import ChatType, ChatMemberStatus ,ChatMembersFilter
from pyrogram import Client
from pyrogram.types import Message 
from pyrogram.types import ChatPermissions,ChatMember


DRAGONS = [5556308886]
DEV_USERS = [5556308886]
COMMANDERS = [ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER]

def bot_admin(func):
    @wraps(func)
    async def is_bot_admin(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)

        if BOT.status != ChatMemberStatus.ADMINISTRATOR:
            if message.chat.title is None:
                await message.reply_text("**ʜᴇʏ ʙᴀʙᴇs ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.**")    
                return 
            else:
                await message.reply_text(f"ʜᴇʏ ʙᴀʙᴇs ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ **{message.chat.title}**")
                return 
        return await func(app,message,*args,**kwargs)
    return is_bot_admin

def bot_can_ban(func):
    @wraps(func)
    async def can_restrict(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)

        if not BOT.privileges.can_restrict_members:
            if message.chat.title is None:
                await message.reply_text("**ʜᴇʏ ʙᴀʙʏ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ. ᴄʜᴇᴄᴋ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴇᴀsᴇ.**🥺")    
                return 
            else:
                await message.reply_text(f"ʜᴇʏ ʙᴀʙʏ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀ ɪɴ **{message.chat.title}**. ᴄʜᴇᴄᴋ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴇᴀsᴇ.🥺")
                return 
        return await func(app,message,*args,**kwargs)
    return can_restrict

def user_admin(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
             
        if (user.status not in COMMANDERS) and user_id not in DRAGONS:
            return await message.reply_text("sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs ᴍғ. ʙᴇᴄᴏᴍᴇ **ᴀᴅᴍɪɴ** ғɪʀsᴛ.")
                                                                            
        return await mystic(app,message,*args,**kwargs)

    return wrapper



def user_can_ban(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.status in COMMANDERS and not user.privileges.can_restrict_members) and user_id not in DRAGONS:                     
            return await message.reply_text("ʜᴇʏ ɴᴏᴏʙ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛ ᴛᴏ **ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs**. ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper
            

@pgram.on_message(filters.command(["banall","unbanall","kickall","muteall","unmuteall"]) & filters.group)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def ban_all(_, message):
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
                              
    
                                                         
    
