from TeleBot import pgram
from pyrogram import filters

from pyrogram.handlers import MessageHandler

#async def my_handler(client, message):
#    if message.reply_to_message.sticker:
 #       await pgram.send_message(message.chat.id,"hii how are u")
#        print(message)

#pgram.add_handler(MessageHandler(my_handler, filters.command("okk") & filters.sticker))    

@pgram.on_message(filters.text | filters.sticker)
async def text_or_sticker(client, message):
    print("text_or_sticker")

@pgram.on_message(filters.text, group=1)
async def just_text(client, message):
    print("Just Text")
