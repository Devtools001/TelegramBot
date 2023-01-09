import time
import asyncio 
from typing import List
from TeleBot import pgram,get_readable_time,StartTime,DEV_USERS
from pyrogram import filters
from httpx import AsyncClient


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



sites_list = {
    "ᴛᴇʟᴇɢʀᴀᴍ": "https://api.telegram.org",
    "ᴋᴀɪᴢᴏᴋᴜ": "https://animekaizoku.com",
    "ᴋᴀʏᴏ": "https://animekayo.com",
    "ᴊɪᴋᴀɴ": "https://api.jikan.moe/v3",
}


async def ping_func(to_ping: List[str]) -> List[str]:
    ping_result = []

    for each_ping in to_ping:

        start_time = time.time()
        site_to_ping = sites_list[each_ping]
        async with AsyncClient() as client:
            r = await client.get(site_to_ping)
        end_time = time.time()
        ping_time = str(round((end_time - start_time), 2)) + "s"

        pinged_site = f"<b>{each_ping}</b>"

        if each_ping == "ᴋᴀɪᴢᴏᴋᴜ" or each_ping == "Kayo":
            pinged_site = f'<a href="{sites_list[each_ping]}">{each_ping}</a>'
            ping_time = f"<code>{ping_time} (Status: {r.status_code})</code>"

        ping_text = f"{pinged_site}: <code>{ping_time}</code>"
        ping_result.append(ping_text)

    return ping_result


@pgram.on_message(filters.command("pingall") & filters.user(DEV_USERS))
async def _pingall(_, message):
    to_ping = ["ᴋᴀɪᴢᴏᴋᴜ", "ᴋᴀʏᴏ", "ᴛᴇʟᴇɢʀᴀᴍ", "ᴊɪᴋᴀɴ"]
    pinged_list = await ping_func(to_ping)
    pinged_list.insert(2, "")
    uptime = get_readable_time((time.time() - StartTime))

    reply_msg = "⏱ᴘɪɴɢ ʀᴇsᴜʟᴛs ᴀʀᴇ:\n"
    reply_msg += "\n".join(pinged_list)
    reply_msg += f"\nsᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ: {uptime}"

    await message.reply_text(
        reply_msg,
        disable_web_page_preview=True,
    )
    
    
