from TeleBot import pgram
from pyrogram import filters

from pyrogram.handlers import MessageHandler
async def my_handler(_, message):
    r = await pgram.get_chat(-1001698076323)
    print(str(r.invite_link))

pgram.add_handler(MessageHandler(my_handler, filters.command("okk")))    

