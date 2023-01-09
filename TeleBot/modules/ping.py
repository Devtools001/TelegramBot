import time
import asyncio 
from TeleBot import pgram,get_readable_time,StartTime,DEV_USERS
from pyrogram import filters


@pgram.on_message(filters.command("ping"))
async def _ping(_, message):
    start = time.time()
    msg = await message.reply("⚡")
    end = time.time()
    telegram_ping = str(round((end - start) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))
    await msg.edit(f"""
𝗣𝗢𝗡𝗚 🥀!!
**ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** {telegram_ping}
**sᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ:** {uptime}
        """)



@pgram.on_message(filters.command("pingall") & filters.user(DEV_USERS))
async def _pingall(_, message):
    to_ping = ["ᴋᴀɪᴢᴏᴋᴜ", "ᴋᴀʏᴏ", "ᴛᴇʟᴇɢʀᴀᴍ", "ᴊɪᴋᴀɴ"]
    
