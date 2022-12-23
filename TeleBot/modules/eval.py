from TeleBot import pgram
from pyrogram import filters

@pgram.on_message(filters.command("eval")
async def(_, message):
    print(message.text)
    print(message.command)
