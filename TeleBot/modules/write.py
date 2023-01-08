import requests
from TeleBot import pgram,BOT_NAME,BOT_USERNAME
from pyrogram import filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 



@pgram.on_message(filters.command("write"))
async def _write(_, message):
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ʙᴀʙʏ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ ɪᴛ ɪɴ ᴍʏ ɴᴏᴛᴇʙᴏᴏᴋ 📒.")
    if replied :
        text = replied.text
    else:
        text = message.text.split(None,1)[1]
    
    msg = await message.reply("`ᴡʀɪᴛɪɴɢ ᴛʜᴇ ᴛᴇxᴛ... 📝`")
    req = requests.get(f"https://api.sdbots.tk/write?text={text}").url  
    try:
        await message.reply_photo(
        photo=req,
        caption=f"""
Successfully Written Text 💘
✨ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **Requested by :** {message.from_user.mention}
❄ **Link :** `{req}`""",
        parse_mode=enums.ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=req),
                    ],
                ]
            ),
        )
        await m.delete() 
    except Exception as er:
        await message.reply_text(er) 
