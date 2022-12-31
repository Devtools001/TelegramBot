from TeleBot import pgram 
from pyrogram import Client, filters 
from pyrogram.types import Message 
from pyrogram.enums import ChatMemberStatus
from TeleBot import BOT_ID
from functools import wraps 



from TeleBot import pgram 
@pgram.on_message(filters.command("okk"))
async def blah(_, message):
  await message.reply_to_message.reply_text("hi")
