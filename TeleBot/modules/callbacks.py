import time
from pyrogram import filters 
from TeleBot import pgram,StartTime,BOT_NAME,get_readable_time,BOT_USERNAME
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton 
from TeleBot.__main__ import PM_START_TEXT, buttons 


BUTTON = [
    [
        InlineKeyboardButton(
            text="✨ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],    
    [
        InlineKeyboardButton(text="⚡ ʜᴇʟᴘ ⚡", callback_data="help_back"),
        InlineKeyboardButton(text="♻️ sᴛᴀᴛs ♻️", callback_data="bot_ping")
    ],    
]

@pgram.on_callback_query(filters.regex("friday_back"))
async def Friday(_, callback_query : CallbackQuery):
    query= callback_query.message
    first_name=callback_query.from_user.first_name
    uptime= get_readable_time((time.time() - StartTime))
    await query.edit_caption(PM_START_TEXT.format(first_name,BOT_NAME,uptime),
    reply_markup=InlineKeyboardMarkup(BUTTON))
