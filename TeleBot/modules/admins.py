import os
from TeleBot import pgram
from pyrogram import filters
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_change_info,
    user_admin,
    user_can_change_info )

@pgram.on_message(filters.command(["setgtitle","setgdesc","setgpic"]) & ~filters.private)
@bot_admin
@bot_can_change_info
@user_admin
@user_can_change_info
async def g_title(_,message):  
    chat_id = message.chat.id
    mention = message.from_user.mention
    replied = message.reply_to_message
    if not message.from_user:
            return   
    if message.command[0] == "setgtitle":       
        if len(message.command) < 2:
            await message.reply_text(f"ʜᴇʏ **{mention}** ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ.")  
            return
        else:
            get_new_title = message.text.split(None,1)[1]
            try:                    
                await pgram.set_chat_title(chat_id,get_new_title)      
                await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ.")
            except Exception:
                pass    
    if message.command[0] == "setgdesc":
        if len(message.command) < 2:
            await message.reply_text(f"ʜᴇʏ **{mention}** ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀ ɢʀᴏᴜᴘ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ.")  
            return 
        else:
            get_new_desc = message.text.split(None,1)[1]   
            try:                    
                await pgram.set_chat_description(chat_id,get_new_desc)      
                await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ.")
            except Exception:
                pass       
    if message.command[0] == "setgpic":
        if replied :            
            if replied.photo:
                text = await message.reply_text("ᴊᴜsᴛ ᴀ sᴇᴄ..... ")         
                try:
                    g_pic = await replied.download()
                    await pgram.set_chat_photo(chat_id, photo=g_pic)
                    await text.delete()
                    await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴘɪᴄ.")
                    os.remove(g_pic)
                except Exception as error:
                    await message.reply_text(error)
            else:
                await message.reply_text(f"ʜᴇʏ **{mention}** ɪ ᴛʜɪɴɢ ʏᴏᴜ sʜᴏᴜʟᴅ ʀᴇᴘʟʏ ᴛᴏ ᴀ ɪᴍᴀɢᴇ.")
        else:
            await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ɪᴍᴀɢᴇ ʙʀᴜʜ.")
                                   


__help__ = """
**⸢ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ ᴍᴇɴᴛɪᴏɴs ʏᴏᴜ ɪɴ ᴀ ᴄʜᴀᴛ, ᴛʜᴇ ᴜsᴇʀ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ ʏᴏᴜ ᴀʀᴇ AFK. ʏᴏᴜ ᴄᴀɴ ᴇᴠᴇɴ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇᴀsᴏɴ ғᴏʀ ɢᴏɪɴɢ AFK, ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ ᴀs ᴡᴇʟʟ.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
「𝗔𝗗𝗠𝗜𝗡𝗦 𝗢𝗡𝗟𝗬」
 ๏ /promote <ᴜsᴇʀ> <ʀᴀɴᴋ>: ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴜsᴇʀ.
๏ /fullpromote <ᴜsᴇʀ> <ʀᴀɴᴋ>: ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴜsᴇʀ ᴡɪᴛʜ ғᴜʟʟ ʀɪɢʜᴛs.
๏ /demote <ᴜsᴇʀ>: ᴅᴇᴍᴏᴛᴇ ᴀ ᴜsᴇʀ.
๏ /setgtitle <ᴛɪᴛʟᴇ>: ᴇᴅɪᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ.
๏ /setgpic <ʀᴇᴘʟʏ to image>: sᴇᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ.
๏ /setgdesc <ᴛᴇxᴛ>: ᴇᴅɪᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ.
๏ /setgsticker <ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ>: sᴇᴛ ᴛʜᴇ ɢʀᴏᴜᴘ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ.
๏ /adminlist: ʟɪsᴛ ᴛʜᴇ ᴀᴅᴍɪɴs ᴏғ ᴛʜᴇ ᴄʜᴀᴛ.
๏ /bots: ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ʙᴏᴛs ᴏғ ᴛʜᴇ ᴄʜᴀᴛ.
๏ /kickthefools: ᴋɪᴄᴋ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴏᴠᴇʀ ᴀ ᴍᴏɴᴛʜ.
๏ /invitelink: ᴇxᴘᴏʀᴛ ᴛʜᴇ ᴄʜᴀᴛ ɪɴᴠɪᴛᴇ ʟɪɴᴋ..
═───────◇───────═
"""
__mod_name__ = "𝙰ᴅᴍɪɴs"
