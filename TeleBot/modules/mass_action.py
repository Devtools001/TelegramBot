from TeleBot import pgram as app
from pyrogram import filters,enums
from pyrogram.types import ChatPermissions,ChatMember
#from TeleBot.modules.pyrogram_funcs.admins import user_admin

BOT_ID = 5724020149
DEV_USER = [5556308886]

def PermissionCheck(mystic):
    async def wrapper(_, message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        user = await app.get_chat_member(chat_id,user_id)
        ADMINS = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            ADMINS.append(m.user.id)

        if user_id not in ADMINS:
            return await message.reply_text("you are not admin")

        elif not user.privileges.can_restrict_members:           
            return await message.reply_text("you don't have the permission")

        elif user_id in DEV_USER:
            return True    
                    
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
                                         
    
            

