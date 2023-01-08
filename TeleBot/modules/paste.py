import os
import re

import aiofiles
from pyrogram import filters

from inspect import getfullargspec
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from TeleBot import pgram

BASE = "https://batbin.me/"



async def paste(content: str):
    resp = await post(f"{BASE}api/v2/paste", data=content)
    if not resp["success"]:
        return
    return BASE + resp["message"]

async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})


pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")

@pgram.on_message(filters.command("paste"))
async def _paste(_, message):
    replied = message.reply_to_message
    if not replied:
        return await eor(message,text = "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ /ᴘᴀsᴛᴇ")
    
    if not replied.text and not replied.document:
        return await eor(
            message, text="ᴏɴʟʏ ᴛᴇxᴛ ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛs ᴀʀᴇ sᴜᴘᴘᴏʀᴛᴇᴅ.")
    
    m = await eor(message, text="ᴘᴀsᴛɪɴɢ....")
     
    
    if replied.text:
        content = str(r.text)
    elif replied.document:
        if replied.document.file_size > 40000:
            return await m.edit("You can only paste files smaller than 40KB.")

        if not pattern.search(replied.document.mime_type):
            return await m.edit("oɴʟʏ ᴛᴇxᴛ ғɪʟᴇs ᴄᴀɴ ʙᴇ ᴘᴀsᴛᴇᴅ.")

        doc = await replied.download()

        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()

        os.remove(doc)

    link = await paste(content)
    BUTTONS = [[InlineKeyboardButton(text="ᴘᴀsᴛᴇ Lɪɴᴋ",url=link)]]
    try:
        if m.from_user.is_bot:
            await message.reply_photo(
                photo=link,
                quote=False,
                reply_markup=BUTTONS,
            )
        else:
            await message.reply_photo(
                photo=link,
                quote=False,
                caption=f"**ᴘᴀsᴛᴇ ʟɪɴᴋ :** [Here]({link})",
            )
        await m.delete()
    except Exception:
        await m.edit("ʜᴇʀᴇ's ʏᴏᴜʀ ᴘᴀsᴛᴇ", reply_markup=BUTTONS)
    
