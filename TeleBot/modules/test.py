from TeleBot import pgram 
from pyrogram import Client, filters 
from pyrogram.types import Message 
from pyrogram.enums import ChatMemberStatus
from TeleBot import BOT_ID
from functools import wraps 



from TeleBot import pgram 
@pgram.on_message(filters.new_chat_members)
async def blah(_,msg):
  await message.reply_to_message.reply_text("hi")
