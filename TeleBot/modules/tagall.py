import asyncio
from TeleBot import pgram
from pyrogram import filters


@pgram.on_message(filters.command("tagall") & filters.group)
async def tag_all(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs") 
        return 

    text = (
            message.text.split(None, 1)[1]
            if len(message.command) < 3
            else message.text.split(None, 1)[1]
        )
       
    usernum= 0
    usertxt = ""
    async for m in pgram.get_chat_members(message.chat.id):        
        usernum += 1
        usertxt += f" [{m.user.first_name}](tg://user?id={m.user.id})"
        if usernum == 5:
            await pgram.send_message(message.chat.id,f'{usertxt}\n{text}')
            await asyncio.sleep(2)
            usernum = 0
            usertxt = ""

            
                
        
           

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
""")
    
                   
            
           
    
    

    
