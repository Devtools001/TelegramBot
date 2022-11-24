from TeleBot import pgram
from pyrogram import filters


@pgram.on_message(filters.command("tagall"))
async def tag_all(_,msg):
    usernme=0
    usertext=""
    async for m in pgram.get_chat_members(msg.chat.id):
        username+=1
        usertext+= f"[{m.user.first_name}](tg://user?id={m.user.id})"
        if username==5:
            text=f"hii \n{usrtxt}"
            await pgram.send_message(msg.chat.id,text)
