import random
from TeleBot import pgram
from TeleBot.modules.fun_strings import *

from pyrogram import filters 
from pyrogram.errors import BadRequest


@pgram.on_message(filters.command("runs"))
async def _run(_, message):
    await message.reply_text(random.choice(RUN_STRINGS))             
