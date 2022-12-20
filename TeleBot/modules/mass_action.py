from TeleBot import pgram as app
from pyrogram import filters,enums, Client 
from pyrogram.types import Message
from pyrogram.types import ChatPermissions,ChatMember
from pyrogram.enums import ChatMemberStatus
#from TeleBot.modules.pyrogram_funcs.admins import user_admin

BOT_ID = 5724020149

def PermissionCheck(mystic):
    async def wrapper(_, message):
        user_id = message.from_user.id
        chat_id = message.chat.id

        user = await app.get_chat_member(chat_id,user_id)

        ADMINS = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            ADMINS.append(m.user.id)

        if user.status == ChatMemberStatus.MEMBER:
            return await message.delete()

        else:
            if user_id not in ADMINS:
                return await message.reply_text("you are not admin")

            if not user.privileges.can_restrict_members:           
                return await message.reply_text("you don't have the permission")
                                            
        return await mystic(_, message)

    return wrapper


def bot_admin(stark):
    async def wrapper(_,message ):
        chat_id = message.chat.id        
        bot = await app.get_chat_member(chat_id, BOT_ID)  
        user = await app.get_chat_member(chat_id, message.from_user.id)

        if user.status == ChatMemberStatus.MEMBER:
            return 
      
        else:
            if bot.status != ChatMemberStatus.ADMINISTRATOR:
                return await message.reply_text("i'm not admin")
           
            if not bot.privileges.can_restrict_members:           
                return await message.reply_text("i don't have the permission")

        return await stark(_,message)

    return wrapper
         



@app.on_message(filters.command("muteall"))
@bot_admin
@PermissionCheck
async def mute_all(_,msg):
    chat_id=msg.chat.id            
    if msg.reply_to_message:
        await app.restrict_chat_member(chat_id, msg.reply_to_message.from_user.id,ChatPermissions(can_send_messages=False))       
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")  
                                         
    
            

