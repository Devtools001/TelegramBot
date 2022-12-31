import asyncio
from TeleBot import pgram
from pyrogram import filters, enums 


@pgram.on_message(filters.command("tagall") & filters.group)
async def tag_all_users(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.") 
        return              
    if replied:        
        usernum= 0
        usertxt = ""
        async for m in pgram.get_chat_members(message.chat.id):        
            usernum += 1
            usertxt += f"\t✨ [{m.user.first_name}](tg://user?id={m.user.id})"
            if usernum == 5:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
    else:
        text = (
            message.text.split(None, 1)[1]
            if len(message.command) < 3
            else message.text.split(None, 1)[1]
        )  
        usernum= 0
        usertxt = ""
        async for m in pgram.get_chat_members(message.chat.id):        
            usernum += 1
            usertxt += f"\t✨ [{m.user.first_name}](tg://user?id={m.user.id})"
            if usernum == 5:
                await pgram.send_message(message.chat.id,f'{usertxt}\n{text}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""            
                
        
           

@pgram.on_message(filters.command("atag") & filters.group)
async def tag_all_admins(_,message):
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇɴᴛɪᴏɴ **ᴀᴅᴍɪɴs**.") 
        return  
    if replied:                   
        username=0
        usertext = ''
        async for m in pgram.get_chat_members(message.chat.id,):
            username += 1
            usertext += f" \n {m.user.first_name}"
        await replied.reply_text(usertext)
    else:
    await message.reply_text("ntg")

    
    

    
