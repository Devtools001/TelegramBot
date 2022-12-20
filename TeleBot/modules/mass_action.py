from TeleBot import pgram as app
from pyrogram import filters
from pyrogram.types import ChatPermissions
from TeleBot.modules.pyrogram_funcs.admins import user_admin
BOT_ID = 5724020149

@app.on_message(filters.command("muteall"))
@user_admin
async def mute_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True    
    if bot_permission:
        async for member in app.get_chat_members(chat_id):       
            try:
                    await app.restrict_chat_member(chat_id, member.user.id,ChatPermissions(can_send_messages=False))
                    await msg.reply_text(f"ᴍᴜᴛɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs {member.user.mention}")
                                        
            except Exception:
                pass
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")  
                                         
    
            

