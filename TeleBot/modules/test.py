from TeleBot import pgram as app
from pyrogram import filters
from pyrogram.enums import ChatType

from pyrogram.handlers import MessageHandler

@app.on_message(filters.command("hii"))
async def hii(_,msg):
    print(msg.sender_chat)
    if msg.chat.type != ChatType.PRIVATE:
        await msg.reply_text("public h")
    else:
        await msg.reply_text("private h")
