from TeleBot import pgram
from pyrogram import filters

from pyrogram.handlers import MessageHandler
async def my_handler(client, message):
    if message.reply_to_message:
        await pgram.send_message(message.chat.id,"hii how are u")
        print(message)

pgram.add_handler(MessageHandler(my_handler, filters.command("okk") & filters.sticker))    

