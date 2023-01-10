from TeleBot import pgram
from pyrogram import filters 
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    user_admin,
    bot_can_pin)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 
from pyrogram import Client,enums


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
        InlineKeyboardMarkup([[InlineKeyboardButton(text="💌 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ",url=replied.link),InlineKeyboardButton(text="💘 ᴜɴᴘɪɴ", callback_data="_unpin")],[InlineKeyboardButton(text="❌ ᴄʟᴏsᴇ", callback_data="close")]]))  
    except Exception as er:
        await message.reply_text(er)


@pgram.on_message(filters.command(["unpin","unpinall"]) & ~filters.private)
@bot_admin
@user_admin
@bot_can_pin
async def _unpinmsg(_, message):
    if message.command[0] == "unpin":
        replied = message.reply_to_message
        if not replied:
            return await message.reply_text("🚫 ʜᴇʏ ʙᴀʙʏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜɴᴘɪɴ ɪᴛ.")
        try:
            await replied.unpin()
            await message.reply_text("🚫 sᴜᴄᴄᴇss!  ᴜɴᴘɪɴɴᴇᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴏɴ ᴛʜɪs ɢʀᴏᴜᴘ.",reply_markup=
            InlineKeyboardMarkup([[InlineKeyboardButton(text="🎣 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ",url=replied.link)],[InlineKeyboardButton(text="❌ ᴄʟᴏsᴇ", callback_data="close")]]))  
        except Exception as er:
            await message.reply_text(er)
    if message.command[0] == "unpinall":
        await pgram.unpin_all_chat_messages(message.chat.id)
        await message.reply_text("🎣 ᴜɴᴘɪɴɴᴇᴅ ᴀʟʟ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.", reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton("❌ ᴄʟᴏsᴇ", callback_data="close")]]))

@pgram.on_callback_query(filters.regex("_unpin"))
async def _unpinc(app : Client , callback_query : CallbackQuery):    
    chat_id = callback_query.message.chat.id
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)
    user_id = callback_query.message.from_user.id
    replied = callback_query.message.reply_to_message    
    if user_id in administrators:
        await replied.unpin()
    
        
