from TeleBot import pgram 
from pyrogram import Client, filters 
from pyrogram.types import Message 
from pyrogram.enums import ChatMemberStatus
from TeleBot import BOT_ID
from functools import wraps 



from TeleBot import pgram 
@pgram.on_message(filters.new_chat_members)
async def blah(_,msg):
  count = await pgram.get_chat_members_count(-1001698076323)
  new = int(count) + 1
  await msg.reply_text(f"member count {new}")
