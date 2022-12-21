from TeleBot import pgram
from pyrogram import filters 
from telegraph import upload_file



@pgram.on_message(filters.command("tgm"))
async def telegraph(app, message):
    replied = message.reply_to_message
    if replied.photo:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ɢᴇᴛ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ telegra.ph link")
