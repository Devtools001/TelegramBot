from TeleBot import pgram
from pyrogram import filters 
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    user_admin,
    bot_can_pin)

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 
from pyrogram import Client,enums
from pyrogram.handlers import CallbackQueryHandler

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
        InlineKeyboardMarkup([[InlineKeyboardButton(text="💌 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ",url=replied.link)],[InlineKeyboardButton(text="❌ ᴄʟᴏsᴇ", callback_data="admin_close")]]))  
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
            InlineKeyboardMarkup([[InlineKeyboardButton(text="🎣 ᴠɪᴇᴡ ᴍᴇssᴀɢᴇ",url=replied.link)],[InlineKeyboardButton(text="❌ ᴄʟᴏsᴇ", callback_data="admin_close")]]))  
        except Exception as er:
            await message.reply_text(er)
    if message.command[0] == "unpinall":
        await pgram.unpin_all_chat_messages(message.chat.id)
        await message.reply_text("🎣 ᴜɴᴘɪɴɴᴇᴅ ᴀʟʟ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.", reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton("❌ ᴄʟᴏsᴇ", callback_data="admin_close")]]))

#@pgram.on_callback_query()
#async def cb(app: Client, query : CallbackQuery):
#    id = query.data.split(":")
#    await app.unpin_chat_message(query.message.chat.id,int(id[1]))
        
__help__ = """
**⸢ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
「𝗔𝗗𝗠𝗜𝗡𝗦 𝗢𝗡𝗟𝗬」
๏ /pin : ᴘɪɴ ᴀ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ.
๏ /unpin : ᴜɴᴘɪɴ ᴀ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ.
═───────◇───────═
"""


__mod_name__ = "𝙿ɪɴ"
