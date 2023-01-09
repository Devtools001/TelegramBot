import time
import asyncio 
from TeleBot import pgram,get_readable_time,StartTime
from pyrogram import filters


@pgram.on_message(filters.command("ping"))
async def _ping(_, message):
    start = time.time()
    msg = await message.reply("⚡")
    end = time.time()
    telegram_ping = str(round((end - start) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))
    await msg.edit(f"""
        𝗣𝗢𝗡𝗚 🥀!!\n"
        "**ᴛɪᴍᴇ ᴛᴀᴋᴇɴ:** {telegram_ping}\n"
        "**sᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ:** {uptime}"""       
    )


    
