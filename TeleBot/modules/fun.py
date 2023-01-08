import random
from TeleBot import pgram
from TeleBot.modules.fun_strings import *

from pyrogram import filters 
from pyrogram.errors import BadRequest


@pgram.on_message(filters.command("toss"))
async def _run(_, message):
    await message.reply_text(random.choice(TOSS))             


@pgram.on_message(filters.command("runs"))
async def _run(_, message):
    await message.reply_text(random.choice(RUN_STRINGS))             


@pgram.on_message(filters.command("dice"))
async def _run(_, message):
    chat_id = message.chat.id
    await pgram.send_dice(chat_id, "🎲")


@pgram.on_message(filters.command("dart"))
async def _run(_, message):
    chat_id = message.chat.id
    await pgram.send_dice(chat_id, "🎯")

@pgram.on_message(filters.command("slot"))
async def _run(_, message):
    chat_id = message.chat.id
    await pgram.send_dice(chat_id, "🎰")


@pgram.on_message(filters.command("football"))
async def _run(_, message):
    chat_id = message.chat.id
    await pgram.send_dice(chat_id, "⚽")


@pgram.on_message(filters.command("basket"))
async def _run(_, message):
    chat_id = message.chat.id
    await pgram.send_dice(chat_id, "🏀")


@pgram.on_message(filters.command("bowling"))
async def _run(_, message):
    chat_id = message.chat.id
    await pgram.send_dice(chat_id, "🎳")




