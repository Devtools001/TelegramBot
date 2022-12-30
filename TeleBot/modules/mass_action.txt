from TeleBot import pgram as app
from pyrogram import filters,enums, Client 
from pyrogram.types import Message
from pyrogram.types import ChatPermissions,ChatMember
from pyrogram.enums import ChatMemberStatus
#from TeleBot.modules.pyrogram_funcs.admins import user_admin

BOT_ID = 5724020149
SUDO = [5459540851,5556308886]

def user_admin(mystic):
    async def wrapper(_, message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if user.status != ChatMemberStatus.ADMINISTRATOR:
            return await message.reply_text("u r not admin") 
                                            
        return await mystic(_, message)

    return wrapper



def user_can_ban(mystic):
    async def wrapper(_, message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        
        if not user.privileges.can_restrict_members:           
            return await message.reply_text("u don't have the permission")                
                                            
        return await mystic(_, message)

    return wrapper


def bot_admin(stark):
    async def wrapper(_,message ):
        chat_id = message.chat.id        
        bot = await app.get_chat_member(chat_id, BOT_ID)  
        
        if bot.status != ChatMemberStatus.ADMINISTRATOR:
            return await message.reply_text("i'm not admin")

                                                           
        return await stark(_,message)

    return wrapper


def bot_can_ban(stark):
    async def wrapper(_,message ):
        chat_id = message.chat.id        
        bot = await app.get_chat_member(chat_id, BOT_ID)  
                
        if not bot.privileges.can_restrict_members:           
            return await message.reply_text("i don't have the permission")                
                                                   
        return await stark(_,message)

    return wrapper
         



@app.on_message(filters.command("muteall"))
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def mute_all(_,msg):
    chat_id=msg.chat.id            
    if msg.reply_to_message:
        await app.ban_chat_member(chat_id, msg.reply_to_message.from_user.id)       
    
