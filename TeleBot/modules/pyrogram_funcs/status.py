from functools import wraps 
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from TeleBot import BOT_ID,DEV_USERS,DRAGONS
from pyrogram.enums import ChatType

COMMANDERS = [ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER]
SUPREME_USERS = DEV_USERS + DRAGONS


def bot_admin(func):
    @wraps(func)
    async def is_bot_admin(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)
        if message.chat.type == ChatType.PRIVATE:
            await message.reply_text("**💘 ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.**")    
            return 
        else :
            if BOT.status != ChatMemberStatus.ADMINISTRATOR:                                       
                await message.reply_text(f"ʜᴇʏ ʙᴀʙᴇs ɪ'ᴍ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ **{message.chat.title}**")
                return 
        return await func(app,message,*args,**kwargs)
    return is_bot_admin

def bot_can_ban(func):
    @wraps(func)
    async def can_restrict(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)
        if message.chat.type == ChatType.PRIVATE:
            await message.reply_text("**💘 ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.**")    
            return 
        else:
            if not BOT.privileges.can_restrict_members:                        
                await message.reply_text(f"ʜᴇʏ ʙᴀʙʏ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀ ɪɴ **{message.chat.title}**. ᴄʜᴇᴄᴋ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴇᴀsᴇ.🥺")
                return 
        return await func(app,message,*args,**kwargs)
    return can_restrict

def bot_can_change_info(func):
    @wraps(func)
    async def can_change_info(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)

        if not BOT.privileges.can_change_info:
            if message.chat.title is None:
                await message.reply_text("**💘 ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.**")    
                return 
            else:
                await message.reply_text(f"ʜᴇʏ ʙᴀʙʏ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ᴄʜᴀɴɢᴇ ɪɴғᴏ ᴏғ **{message.chat.title}**. ᴄʜᴇᴄᴋ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴇᴀsᴇ.🥺")
                return 
        return await func(app,message,*args,**kwargs)
    return can_change_info


def bot_can_promote(func):
    @wraps(func)
    async def can_promote(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)

        if not BOT.privileges.can_promote_members:
            if message.chat.title is None:
                await message.reply_text("ʜᴇʏ ʙᴀʙʏ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ **ᴘʀᴏᴍᴏᴛᴇ ᴜsᴇʀs** ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ. ᴄʜᴇᴄᴋ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴇᴀsᴇ.🙄")    
                return 
            else:
                await message.reply_text(f"ʜᴇʏ ʙᴀʙʏ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ **ᴘʀᴏᴍᴏᴛᴇ ᴜsᴇʀs** ɪɴ **{message.chat.title}**. ᴄʜᴇᴄᴋ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴇᴀsᴇ.")
                return 
        return await func(app,message,*args,**kwargs)
    return can_promote


def bot_can_pin(func):
    @wraps(func)
    async def can_pin(app : Client, message : Message,*args,**kwargs):
        BOT = await app.get_chat_member(message.chat.id,BOT_ID)

        if not BOT.privileges.can_pin_messages:
            if message.chat.title is None:
                await message.reply_text("ʜᴇʏ ʙᴀʙʏ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ *ᴘɪɴ ᴍᴇssᴀɢᴇs* ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ. ᴄʜᴇᴄᴋ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴇᴀsᴇ.🙄")    
                return 
            else:
                await message.reply_text(f"ʜᴇʏ ʙᴀʙʏ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ **ᴘɪɴ ᴍᴇssᴀɢᴇs** ɪɴ **{message.chat.title}**. ᴄʜᴇᴄᴋ ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴇᴀsᴇ.")
                return 
        return await func(app,message,*args,**kwargs)
    return can_pin

def user_admin(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):  
        try:  
            user_id = message.from_user.id    
            chat_id = message.chat.id
            user = await app.get_chat_member(chat_id,user_id)
        except Exception as e:
            await message.reply_text(e)
            return 
        
        if (user.status not in COMMANDERS) and user_id not in SUPREME_USERS:
            return await message.reply_text("sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs ᴍғ. ʙᴇᴄᴏᴍᴇ **ᴀᴅᴍɪɴ** ғɪʀsᴛ.")
                                                                            
        return await mystic(app,message,*args,**kwargs)

    return wrapper

def user_can_ban(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.status in COMMANDERS and not user.privileges.can_restrict_members) and user_id not in SUPREME_USERS:                     
            return await message.reply_text("ʜᴇʏ ɴᴏᴏʙ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛ ᴛᴏ **ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs**. ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper
            

def user_can_change_info(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.status in COMMANDERS and not user.privileges.can_change_info) and user_id not in SUPREME_USERS:                     
            return await message.reply_text("ʜᴇʏ ɴᴏᴏʙ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛ ᴛᴏ **ᴄʜᴀɴɢᴇ ɪɴғᴏ** ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper
            
def user_can_promote(mystic):
    @wraps(mystic)
    async def wrapper(app : Client, message : Message,*args,**kwargs):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if (user.status in COMMANDERS and not user.privileges.can_promote_members) and user_id not in SUPREME_USERS:                     
            return await message.reply_text("ʜᴇʏ ɴᴏᴏʙ ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛ ᴛᴏ **ᴘʀᴏᴍᴏᴛᴇ ᴜsᴇʀs** ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ") 
                                                    
        return await mystic(app,message,*args,**kwargs)
    return wrapper
            
