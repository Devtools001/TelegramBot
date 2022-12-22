from TeleBot import pgram
from pyrogram import filters


@pgram.on_message(filters.command("tagall"))
async def tag_all(_,message):
   # members = []
    username=0
    usertext = ''

    logo_text = (
            message.text.split(None, 1)[1]
            if len(message.command) < 3 else None)

    async for m in pgram.get_chat_members(message.chat.id):
        username += 1
        usertext += m.user.mention
        if username == 5:
            await client.send_message(message.chat.id,f"{m.user.mention} , {logo_text}")
           
    
    

    
