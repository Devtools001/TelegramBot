import asyncio
from TeleBot import pgram
from pyrogram import filters


@pgram.on_message(filters.command("tagall"))
async def tag_all(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 or not replied:
        await message.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs")       
   # usernum= 0
   # usertxt = ""
  #  async for m in pgram.get_chat_members(message.chat.id):        
 #       usernum += 1
   #     usertxt += f"\n[{m.user.first_name}](tg://user?id={m.user.id})"
   #     if usernum == 5:
   #         await pgram.send_message(message.chat.id,f'{usertxt}\n\nhlo')
    #        await asyncio.sleep(2)
   #         usernum = 0
   #         usertxt = ""

            
                
        
           

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
    
                   
            
           
    
    

    
