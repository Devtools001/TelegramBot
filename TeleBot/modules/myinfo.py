import asyncio
from TeleBot import pgram
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery ,InputMediaPhoto
from datetime import datetime


EDIT_TIME = 5

file1 = "https://graph.org/file/d57a4593b6c727a1f7541.jpg"
file2 = "https://graph.org/file/992e2af23414750cfb656.jpg"
file3 = "https://graph.org/file/aae20f536bbaf255a28bd.jpg"
file4 = "https://graph.org/file/3b289f747da34ac4a1103.jpg"
file5 = "https://graph.org/file/7207ff67166b5fab23257.jpg"



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
        caption="🧪 ᴄʟɪᴄᴋ Tʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ Iɴғᴏ.",
        reply_markup=buttons)    
   
    await asyncio.sleep(EDIT_TIME)
    ic = await pgram.edit_message_media(chat_id,steve.id,InputMediaPhoto(file3),reply_markup=buttons)

    await asyncio.sleep(EDIT_TIME)
    ic2 = await pgram.edit_message_media(chat_id,ic.id ,InputMediaPhoto(file1), reply_markup=buttons)

    await asyncio.sleep(EDIT_TIME)
    ic3 = await pgram.edit_message_media(chat_id, ic2.id,InputMediaPhoto(file4),reply_markup=buttons)

    await asyncio.sleep(EDIT_TIME)
    ic4 = await pgram.edit_message_media(chat_id, ic3.id,InputMediaPhoto(file5),reply_markup=buttons)

    await asyncio.sleep(EDIT_TIME)
    ic5 = await pgram.edit_message_media(chat_id,ic4.id,InputMediaPhoto(file2),reply_markup=buttons)

    await asyncio.sleep(EDIT_TIME)
    ic6 = await pgram.edit_message_media(chat_id,ic5.id,InputMediaPhoto(file1),reply_markup=buttons)

    await asyncio.sleep(EDIT_TIME)
    ic7 = await pgram.edit_message_media(chat_id,ic6.id,InputMediaPhoto(file3), reply_markup=buttons)

    await asyncio.sleep(EDIT_TIME)
    ic8 = await pgram.edit_message_media(chat_id,ic7.id,InputMediaPhoto(file4), reply_markup=buttons)

    await asyncio.sleep(EDIT_TIME)
    ic9 = await pgram.edit_message_media(chat_id, ic8.id,InputMediaPhoto(file5), reply_markup=buttons)


@pgram.on_callback_query(filters.regex("info"))
async def _ic(app: Client, query : CallbackQuery):
    print(query)
    print(query.from_user)
    msg = "⚗️ ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜ ᴅᴇᴛᴀɪʟs\n\n"
    msg += f"๏ ғɪʀsᴛ ɴᴀᴍᴇ : {query.from_user.first_name}\n"
    msg += f"๏ ʟᴀsᴛ ɴᴀᴍᴇ : {query.from_user.last_name}\n"
    msg += f"๏ ʏᴏᴜʀ ɪ'ᴅ : {query.from_user.id}\n"
    msg += f"๏ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ : @{query.from_user.username}\n"

    await app.answer_callback_query(
    query.id,
    text=msg,
    show_alert=True)
    
__help__ = """
「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /myinfo : sʜᴏᴡs ʏᴏᴜʀ ɪɴғᴏ ɪɴ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴ.
═───────◇───────═
"""
__mod_name__ = "𝙼ʏ-ɪɴғᴏ"


