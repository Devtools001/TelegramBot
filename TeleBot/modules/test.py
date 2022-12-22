from TeleBot import pgram
from pyrogram import filters

from pyrogram.handlers import MessageHandler
async def my_handler(_, message):
    r = await pgram.get_chat(-896858281)
    await message.reply_text(str(r.invite_link))

pgram.add_handler(MessageHandler(my_handler, filters.command("okk")))    

