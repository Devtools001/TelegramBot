from TeleBot import pgram
from pyrogram import filters


@pgram.on_message(filters.command("tagall"))
async def tag_all(_,msg):
    members = []
    usernme=0
    logo_text = (
            message.text.split(None, 1)[1]
            if len(message.command) < 3 else None)
    async for m in pgram.get_chat_members(msg.chat.id):
        members.append(m.user.mention) 
        print(members)   

    
  #  usernme += 1
    #    usertext += m.user.mention
    #    if usernme==5:
      #      text=f"hii \nlogo_text"
     #       await pgram.send_message(msg.chat.id,text)
        
