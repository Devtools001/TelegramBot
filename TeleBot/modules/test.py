from TeleBot import pgram
from pyrogram import filters

from pyrogram.handlers import MessageHandler
async def my_handler(client, message):
        await message.reply_text("hii bro")
        print(message)

pgram.add_handler(MessageHandler(my_handler, filters.command("okk")))    

