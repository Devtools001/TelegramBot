import speedtest 
from TeleBot import pgram,DEV_USERS

from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 


 buttons = [
        [
            InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="speedtest_image"),
            InlineKeyboardButton("ᴛᴇxᴛ", callback_data="speedtest_text"),
        ]
    ]



@pgram.on_message(filters.command("speedtest") & filters.user(DEV_USERS))
async def _speed(_, message):
    await message.reply_text("sᴩᴇᴇᴅᴛᴇsᴛ ᴍᴏᴅᴇ", reply_markup=InlineKeyboardMarkup(buttons))
    

@pgram.on_callback_query()
async def _speedtest(app : Client,callback_query: CallbackQuery):
    query = callback_query.message
    text = await message.edit("ʀᴜɴɴɪɴɢ ᴀ sᴩᴇᴇᴅᴛᴇsᴛ...")
