import os
from TeleBot import pgram,LOG
from pyrogram import filters
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_change_info,
    user_admin,
    user_can_change_info )

@pgram.on_message(filters.command(["setgtitle","setgdesc"]) & ~filters.private)
@bot_admin
@bot_can_change_info
@user_admin
@user_can_change_info
async def g_title_desc(_,message):  
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
    
                                   
@pgram.on_message(filters.command(["setgpic","setgvid"]) & ~filters.private)
@bot_admin
@bot_can_change_info
@user_admin
@user_can_change_info
async def g_pic_vid(_,message):
    chat_id = message.chat.id
    replied = message.reply_to_message

    if not message.from_user:
            return   
    if message.command[0] == "setgpic":
        if replied :            
            if replied.photo:
                text = await message.reply_text("ᴊᴜsᴛ ᴀ sᴇᴄ..... ")  
                g_pic = await replied.download()       
                try:                    
                    await pgram.set_chat_photo(chat_id, photo=g_pic)
                    await text.delete()
                    await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴘɪᴄ.")
                    
                except Exception as error:
                    await message.reply_text(error)

                os.remove(g_pic)

            else:
                await message.reply_text("ʜᴇʏ ʙᴀʙʏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀn ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. ɪғ ʏᴏᴜ ᴀʀᴇ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴛʜᴇɴ ᴜsᴇ /setgvid ᴄᴏᴍᴍᴀɴᴅ.")
        else:
            await message.reply_text("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ɪᴍᴀɢᴇ.")

    if message.command[0] == "setgvid":
        if replied:
            if replied.video:           
                text = await message.reply_text("ᴡᴀɪᴛᴏᴏ.....")  
                g_vid = await replied.download()  
                try:                                
                    await pgram.set_chat_photo(chat_id, video=g_vid)
                    await text.delete()
                    await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴘɪᴄ.")                    
                except Exception as error:
                    await message.reply_text("ʜᴇʏ ʜᴇʏ ʜᴇʏ....\nᴛʜᴇʀᴇ ᴀʀᴇ sᴏᴍᴇ ʟɪᴍɪᴛᴀᴛɪᴏɴs\nʏᴏᴜʀ ᴠɪᴅᴇᴏ ʀᴀᴛɪᴏ ᴍᴜsᴛ ʙᴇ 1:1 ᴀɴᴅ sɪᴢᴇ ᴜɴᴅᴇʀ 2ᴍʙ + ʟᴇss ᴛʜᴇɴ 10 sᴇᴄᴏɴs ᴏғ ʟᴇɴɢᴛʜ.")
                
                os.remove(g_vid)
                   
            else:
                await message.reply_text("ʜᴇʏ ʙᴀʙʏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. ɪғ ʏᴏᴜ ᴀʀᴇ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀn ɪᴍᴀɢᴇ ᴛʜᴇɴ ᴜsᴇ /setgpic ᴄᴏᴍᴍᴀɴᴅ.")
        else:
            await message.reply_text("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ.")  
            
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
