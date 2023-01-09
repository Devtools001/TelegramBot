from TeleBot import pgram
from pyrogram import filters
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

@pgram.on_message(filters.command("mmf"))
async def _memefy(_, message):
    if message.sender_chat:
        return
    if len(message.command) < 2:
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ")
    
    text = message.text.split(None,1)[1].strip()

    print(text)
    replied = message.reply_to_message
    if not (replied.photo or replied.sticker):
        return await message.reply_text("ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ.")

    file = await replied.download()

    msg = await message.reply("```Memifying this image! ✊🏻 ```")

    meme = await drawText(file, text)

    await message.reply_photo(photo=meme)
    
    await msg.delete()
    os.remove(meme)
    
    print(file,meme)
    os.remove(file)
