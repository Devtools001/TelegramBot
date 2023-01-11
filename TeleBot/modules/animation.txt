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

moon_ani = [
    "🌗",
    "🌘",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
    "🌗",
    "🌘",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
    "🌗",
    "🌘",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
    "🌗",
    "🌘",
    "🌑",
    "🌒",
    "🌓",
    "🌔",
    "🌕",
    "🌖",
]


@pgram.on_message(filters.command("earth"))
async def _earth(_, message):
    msg = await message.reply("🌍")
    for x in range(18):
        await msg.edit(earth[x % 18])
        await asyncio.sleep(1)
    await msg.edit_("🌏")

@pgram.on_message(filters.command("moon"))
async def _earth(_, message):
    msg = await message.reply("🌚")
    for x in range(32):
        await msg.edit(moon_ani[x % 18])
        await asyncio.sleep(1)
    await msg.edit_("🌙")
