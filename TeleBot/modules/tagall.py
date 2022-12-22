import asyncio
from TeleBot import pgram
from pyrogram import filters


#@pgram.on_message(filters.command("tagall"))
#async def tag_all(_,message):  
 
#    logo_text = (
#            message.text.split(None, 1)[1]
#            if len(message.command) < 3 else None)
#    username=0
#    usertext = ''
#   async for m in pgram.get_chat_members(message.chat.id):
#        username += 1
 #       usertext += f"[{m.user.first_name}](tg://user?id={m.user.id}) "
 #       if username == 5:
#            await pgram.send_message(message.chat.id,f"{usertext}\n\n{logo_text}")
#            await asyncio.sleep(1)

@pgram.on_message(filters.command("tag"))
async def tag_all(_,message):  
     
    username=0
    usertext = ''
    async for m in pgram.get_chat_members(message.chat.id):
        username += 1
        usertext += f"[{m.user.first_name}](tg://user?id={m.user.id}) "
    await pgram.send_message(message.chat.id,f"{usertext}\n\n{logo_text}")
    await asyncio.sleep(1)
                   
            
           
    
    

    
