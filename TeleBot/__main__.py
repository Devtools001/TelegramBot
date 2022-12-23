import re
import asyncio
import importlib
from contextlib import closing, suppress
from uvloop import install

from TeleBot import (
    BOT_NAME,
    BOT_USERNAME,        
    aiohttpsession,
    pgram,
    LOG,
    get_readable_time,
)
from pyrogram import filters,Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.handlers import MessageHandler
from TeleBot.modules import ALL_MODULES
from TeleBot.utilities.misc import paginate_modules
from TeleBot.utilities.constant import MARKDOWN


loop = asyncio.get_event_loop()

START_IMG="https://telegra.ph/file/5381961c760ed435d0fc7.jpg"

PM_PHOTOS = (
"https://telegra.ph/file/9658f5c0f7d448ad4e0bd.jpg",
"https://telegra.ph/file/4a94521e20c40195c9a9a.jpg",
"https://telegra.ph/file/61c9b7921458f31260b0c.jpg",
"https://telegra.ph/file/9e01586796e950cc8ddc6.jpg",
"https://telegra.ph/file/0e068d1357c5a79c191e3.jpg",
"https://telegra.ph/file/13b5bc8b84ee2ac687e3d.jpg",
"https://telegra.ph/file/7517a65cab490e36d681c.jpg"
         )

HELP_IMG=(
"https://telegra.ph/file/74f547d4dd635432ea1b0.jpg",
"https://telegra.ph/file/b846cc2a4326a9dab5a2d.jpg",
"https://telegra.ph/file/1c58b1a72044ba6b6e644.jpg"
   )


PM_START_TEXT = """
🥀 ʜᴇʏ *{}* ,
        
ᴛʜɪs ɪs *{}*
➖➖➖➖➖➖➖➖➖➖➖➖➖
๏ ɪ'ᴍ ᴜɴᴅᴇʀ ᴄʀᴇᴀᴛɪᴏɴ ʙʏ ⸢[𝚂𝚃𝙰𝚁𝙺](https://t.me/NoobStark_21)⸥
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅsn.
๏ *ᴅɪᴅɴ'ᴛ sʟᴇᴇᴘᴛ sɪɴᴄᴇ* {}
"""

buttons = [
    [
        InlineKeyboardButton(
            text="✨ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],    
    [
        InlineKeyboardButton(text="⚡ ʜᴇʟᴘ ⚡", callback_data="help_back"),
        InlineKeyboardButton(text="♻️ sᴛᴀᴛs ♻️", callback_data="Friday_stats")
    ],    
]



HELPABLE = {}

for module in ALL_MODULES:
        imported_module = importlib.import_module("TeleBot.modules." + module)
        if (
                hasattr(imported_module, "__mod_name__")
                and imported_module.__mod_name__
        ):
            imported_module.__mod_name__ = imported_module.__mod_name__
            if (
                    hasattr(imported_module, "__help__")
                    and imported_module.__help__
            ):
                HELPABLE[
                    imported_module.__mod_name__.replace(" ", "_").lower()
                ] = imported_module



#async def send_help(chat_id, text, keyboard=None):
#    if not keyboard:
#        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
#    dispatcher.bot.send_photo(
#        chat_id=chat_id,
#        photo=random.choice(PM_PHOTOS),
#        caption=text,
#        parse_mode=ParseMode.MARKDOWN,      
#        reply_markup=keyboard,
#    )

async def start(client : Client, message: Message):
    await message.reply_text("hii")


def main():
    await pgram.add_handler(MessageHandler(start, filters.command("start")))

if __name__ == "__main__" :
    LOG.print("[yellow] bot started")
    install()
    main()

