import asyncio
from TeleBot import pgram
from pyrogram import filters 
from TeleBot.modules.helper_funcs.chat_status import user_admin



EDIT_SLEEP = 1
EDIT_TIMES = 18

earth_ani = [
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
    "🌍",
    "🌎",
    "🌏",
]

@user_admin
@pgram.on_message(filters.command("earth"))
async def earth(_,msg):
    for x in range(EDIT_TIMES):
        await msg.edit_text(earth_ani[x % 18])
        asyncio.sleep(EDIT_SLEEP)
    await msg.edit_text("🌍") 
