from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from TeleBot import BOT_ID,DEV_USERS,DRAGONS


COMMANDERS = [ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER]
SUPREME_USERS = DEV_USERS + DRAGONS


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
            
