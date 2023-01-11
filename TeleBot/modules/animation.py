import asyncio
from TeleBot import pgram
from pyrogram import filters 

earth = [
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
]


@pgram.on_message(filters.command("earth"))
async def _earth(_, message):
    x = await message.reply("🌍")
    for x in range(18):
        await x.edit(earth[x % 18])
        await asyncio.sleep(1)
    await x.edit_("🌏")
