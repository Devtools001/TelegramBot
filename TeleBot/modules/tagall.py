import asyncio
from TeleBot import pgram
from pyrogram import filters

spam_chats = []

@pgram.on_message(filters.command("tagall"))
async def tag_all(_,message):      
    spam_chats.append(message.chat.id)
    mnum=0
    usertext = ''
    async for m in pgram.get_chat_members(message.chat.id):
        if not message.chat.id in spam_chats:
            break
        mnum += 1
        mtxt += f"\n[{m.user.first_name}](tg://user?id={m.user.id})"
        if username == 5:
            await pgram.send_message(message.chat.id,f"""
{mtxt}\n\n hi
""")
    try:
        spam_chats.remove(message.chat.id)
    except:
        pass
              
 #   for i in range(1000000000):
        
   
        
           

@pgram.on_message(filters.command("tag"))
async def tag_all(_,message):       
    username=0
    usertext = 'hii '
    async for m in pgram.get_chat_members(message.chat.id):
        username += 1
        usertext += f" \n [{m.user.first_name}](tg://user?id={m.user.id})"
    await message.reply_text(f"""
{usertext}
⸢ʀᴇᴘᴏʀᴛ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ ᴀᴅᴍɪɴs⸥

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /report <reason>: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴꜱ.
๏ @admin: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴs.
 ɴᴏᴛᴇ: ɴᴇɪᴛʜᴇʀ ᴏғ ᴛʜᴇꜱᴇ ᴡɪʟʟ ɢᴇᴛ ᴛʀɪɢɢᴇʀᴇᴅ ɪғ ᴜsᴇs ʙʏ ᴀᴅᴍɪɴs.
๏ /reports <on/off>: ᴄʜᴀɴɢᴇ ʀᴇᴘᴏʀᴛ sᴇᴛᴛɪɴɢ, ᴏʀ ᴠɪᴇᴡ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ.
๏ ɪғ ᴅᴏɴᴇ ɪɴ ᴘᴍ, ᴛᴏɢɢʟᴇꜱ ʏᴏᴜʀ ꜱᴛᴀᴛᴜꜱ.
๏ ɪғ ɪɴ ɢʀᴏᴜᴘ, ᴛᴏɢɢʟᴇꜱ ᴛʜᴀᴛ ɢʀᴏᴜᴘꜱ ꜱᴛᴀᴛᴜꜱ
═───────◇───────═
⸢ʀᴇᴘᴏʀᴛ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ ᴀᴅᴍɪɴs⸥

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /report <reason>: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴꜱ.
๏ @admin: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴs.
 ɴᴏᴛᴇ: ɴᴇɪᴛʜᴇʀ ᴏғ ᴛʜᴇꜱᴇ ᴡɪʟʟ ɢᴇᴛ ᴛʀɪɢɢᴇʀᴇᴅ ɪғ ᴜsᴇs ʙʏ ᴀᴅᴍɪɴs.
๏ /reports <on/off>: ᴄʜᴀɴɢᴇ ʀᴇᴘᴏʀᴛ sᴇᴛᴛɪɴɢ, ᴏʀ ᴠɪᴇᴡ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ.
๏ ɪғ ᴅᴏɴᴇ ɪɴ ᴘᴍ, ᴛᴏɢɢʟᴇꜱ ʏᴏᴜʀ ꜱᴛᴀᴛᴜꜱ.
๏ ɪғ ɪɴ ɢʀᴏᴜᴘ, ᴛᴏɢɢʟᴇꜱ ᴛʜᴀᴛ ɢʀᴏᴜᴘꜱ ꜱᴛᴀᴛᴜꜱ
═───────◇───────═
⸢ʀᴇᴘᴏʀᴛ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ ᴀᴅᴍɪɴs⸥

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /report <reason>: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴꜱ.
๏ @admin: ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ ᴀᴅᴍɪɴs.
 ɴᴏᴛᴇ: ɴᴇɪᴛʜᴇʀ ᴏғ ᴛʜᴇꜱᴇ ᴡɪʟʟ ɢᴇᴛ ᴛʀɪɢɢᴇʀᴇᴅ ɪғ ᴜsᴇs ʙʏ ᴀᴅᴍɪɴs.
๏ /reports <on/off>: ᴄʜᴀɴɢᴇ ʀᴇᴘᴏʀᴛ sᴇᴛᴛɪɴɢ, ᴏʀ ᴠɪᴇᴡ ᴄᴜʀʀᴇɴᴛ ꜱᴛᴀᴛᴜꜱ.
๏ ɪғ ᴅᴏɴᴇ ɪɴ ᴘᴍ, ᴛᴏɢɢʟᴇꜱ ʏᴏᴜʀ ꜱᴛᴀᴛᴜꜱ.
๏ ɪғ ɪɴ ɢʀᴏᴜᴘ, ᴛᴏɢɢʟᴇꜱ ᴛʜᴀᴛ ɢʀᴏᴜᴘꜱ ꜱᴛᴀᴛᴜꜱ
═───────◇───────═
""")
    
                   
            
           
    
    

    
