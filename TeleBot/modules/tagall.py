import asyncio
from TeleBot import pgram
from pyrogram import filters

spam_chats = []

@pgram.on_message(filters.command("tagall"))
async def tag_all(_,message):  
 
    

    username=0
    usertext = ''
    async for m in pgram.get_chat_members(message.chat.id):
       # if not message.chat.id in spam_chats:
        #    break
        username += 1
        usertext += f"\n[{m.user.first_name}](tg://user?id={m.user.id})"
        if username == 5:
            await pgram.send_message(message.chat.id,f"{usertext}\n\nhoi")
            
 #   for i in range(1000000000):
        
   
        
           

@pgram.on_message(filters.command("tag"))
async def tag_all(_,message):       
    username=0
    usertext = 'hii '
    async for m in pgram.get_chat_members(message.chat.id):
        username += 1
        usertext += f" \n [{m.user.first_name}](tg://user?id={m.user.id})"
    await message.reply_text(usertext)
    
                   
            
           
    
    

    
