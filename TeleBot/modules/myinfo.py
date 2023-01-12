import asyncio
from TeleBot import pgram
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery ,InputMediaPhoto
from datetime import datetime


EDIT_TIME = 5
""" =======================CONSTANTS====================== """
file1 = "https://graph.org/file/d57a4593b6c727a1f7541.jpg"
file2 = "https://graph.org/file/992e2af23414750cfb656.jpg"
file3 = "https://graph.org/file/aae20f536bbaf255a28bd.jpg"
file4 = "https://graph.org/file/3b289f747da34ac4a1103.jpg"
file5 = "https://graph.org/file/7207ff67166b5fab23257.jpg"
""" =======================CONSTANTS====================== """



@pgram.on_message(filters.command("myinfo"))
async def _minfo(_, message):
    if message.sender_chat:
        return
    chat_id = message.chat.id
    user_name = message.from_user
    datetime.utcnow()
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton("💌 ᴄʟɪᴄᴋ ʜᴇʀᴇ", callback_data="info")]])  
    steve = await pgram.send_photo(
        chat_id,
        photo=file2,
        reply_markup=buttons)    
    print(steve) 
    await asyncio.sleep(EDIT_TIME)
    await pgram.edit_message_media(chat_id,steve,InputMediaPhoto(file3),reply_markup=buttons)
