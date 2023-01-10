from TeleBot import pgram
from pyrogram import filters 
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    user_admin,
    bot_can_pin)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
@pgram.on_message(filters.command("pin") & ~filters.private)
@bot_admin
@user_admin
@bot_can_pin
async def _pin(_, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("💌 ʜᴇʏ ʙᴀʙʏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘɪɴ ɪᴛ.")
    try:
        await replied.pin()
        await message.reply_text("💌 sᴜᴄᴄᴇss! ᴘɪɴɴᴇᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴏɴ ᴛʜɪs ɢʀᴏᴜᴘ.",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(📝 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ,url=replied.link)]]))
    
