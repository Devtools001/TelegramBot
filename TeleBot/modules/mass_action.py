from TeleBot import pgram as app
from pyrogram import filters
from pyrogram.types import ChatPermissions,ChatMember
#from TeleBot.modules.pyrogram_funcs.admins import user_admin

BOT_ID = 5724020149

def PermissionCheck(mystic):
    async def wrapper(_, message):
        admin = "administrator"
        creator = "creator"
        ranks = [admin, creator]
        a = await app.get_chat_member(message.chat.id,message.from_user.id)
        if a.status not in ranks:
            return await message.reply_text("you are not admin")
                
        if not a.privileges.can_restrict_members:           
            return await message.reply_text("you don't have the permission")
                        
        return await mystic(_, message)

    return wrapper

@app.on_message(filters.command("muteall"))
@PermissionCheck
async def mute_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True    
    if bot_permission and msg.reply_to_message:
        await app.restrict_chat_member(chat_id, msg.reply_to_message.from_user.id,ChatPermissions(can_send_messages=False))
        
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")  
                                         
    
            

