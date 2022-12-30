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

def bot_admin(func):
    @wraps(func)
    async def is_bot_admin(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)

        if BOT.status != ChatMemberStatus.ADMINISTRATOR:
            if message.chat.title is None:
                await message.reply_text("i am not admin")    
                return 
            else:
                await message.reply_text(f" I'm not admin in {message.chat.title}")
                return 
        return await func(app,message,*args,**kwargs)
    return is_bot_admin

def bot_can_ban(func):
    @wraps(func)
    async def can_restrict(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)

        if not BOT.privileges.can_restrict_members:
            if message.chat.title is None:
                await message.reply_text("i can't restrict people here make sure am admin and can restrict members")    
                return 
            else:
                await message.reply_text(f"i can't restrict people in {message.chat.title} make sure am admin and can restrict members")
                return 
        return await func(app,message,*args,**kwargs)
    return can_restrict

def user_admin(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
             
        if (user.status != ChatMemberStatus.ADMINISTRATOR) and user_id not in DRAGONS:
            return await message.reply_text("ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ʙᴇ ᴀɴ ᴀᴅᴍɪɴ ᴛᴏ ᴅᴏ ᴛʜɪs!")
                                                                            
        return await mystic(app,message,*args,**kwargs)

    return wrapper



def user_can_ban(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.status == ChatMemberStatus.ADMINISTRATOR and not user.privileges.can_restrict_members) and user_id not in DRAGONS:                     
            return await message.reply_text("sorry son u r not worthy") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper
            

@pgram.on_message(filters.command(["banall","unbanall"]))
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def ban_all(_, message):
    chat_id = message.chat.id    
    if message.command[0] == "banall":
        start = datetime.now()                    
        async for member in pgram.get_chat_members(chat_id):       
            try:
                await pgram.ban_chat_member(chat_id, member.user.id)
                await message.reply_text(f"ғᴜᴄᴋɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴍᴏᴍs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {member.user.mention}") 
                await asyncio.sleep(3) 
        time = (datetime.now() - start).secons                
            except Exception:
                pass
    if message.command[0] == "unbanall":                
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
                                             
    
                                                         
    
