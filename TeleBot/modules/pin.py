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
        await replied.pin(disable_notification=True)
        await message.reply_text("📝 sᴜᴄᴄᴇss! ᴘɪɴɴᴇᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴏɴ ᴛʜɪs ɢʀᴏᴜᴘ.",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="💌 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ",url=replied.link)],[InlineKeyboardButton(text="❌ ᴄʟᴏsᴇ", callback_data="close")]]))  
    except Exception as er:
        await message.reply_text(er)


@pgram.on_message(filters.command("unpin") & ~filters.private)
@bot_admin
@user_admin
@bot_can_pin
async def _pin(_, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("🚫 ʜᴇʏ ʙᴀʙʏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜɴᴘɪɴ ɪᴛ.")
    try:
        await replied.unpin()
        await message.reply_text("🚫 sᴜᴄᴄᴇss!  ᴜɴᴘɪɴɴᴇᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴏɴ ᴛʜɪs ɢʀᴏᴜᴘ.",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="🎣 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ",url=replied.link)],[InlineKeyboardButton(text="❌ ᴄʟᴏsᴇ", callback_data="close")]]))  
    except Exception as er:
        await message.reply_text(er)

        
