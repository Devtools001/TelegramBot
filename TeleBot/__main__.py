import asyncio
import os
import re
import time
import random 
import importlib
from datetime import datetime
from typing import Optional
from sys import argv
from uvloop import install
from contextlib import closing, suppress
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram.errors import BadRequest 
from pyrogram.types import CallbackQuery
from pyrogram import filters,idle

from TeleBot.modules import ALL_MODULES
from TeleBot.utilities.misc import paginate_modules
from TeleBot.resources.Data import *
from TeleBot import (
    BOT_NAME,
    BOT_USERNAME,        
    aiohttpsession,
    pgram,
    LOG,
    StartTime,
    get_readable_time

)
from pyrogram.enums import ParseMode 

loop = asyncio.get_event_loop() 

HELP_STRINGS = """
ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs.
"""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

async def Friday_Robot():
    global IMPORTED,MIGRATEABLE,HELPABLE
    global STATS, USER_INFO,DATA_IMPORT,DATA_EXPORT
    global CHAT_SETTINGS,USER_SETTINGS

    for module_name in ALL_MODULES:
        imported_module = importlib.import_module("TeleBot.modules." +
                                              module_name)
   # all_modules += "⦿ " + module_name + "\n"
        if not hasattr(imported_module, "__mod_name__"):
            imported_module.__mod_name__ = imported_module.__name__

        if not imported_module.__mod_name__.lower() in IMPORTED:
            IMPORTED[imported_module.__mod_name__.lower()] = imported_module
        else:
            raise Exception(
                "Can't have two modules with the same name! Please change one")

        if hasattr(imported_module, "__help__") and imported_module.__help__:
            HELPABLE[imported_module.__mod_name__.lower()] = imported_module

        if hasattr(imported_module, "get_help") and imported_module.get_help:
            HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
        if hasattr(imported_module, "__migrate__"):
            MIGRATEABLE.append(imported_module)

        if hasattr(imported_module, "__stats__"):
            STATS.append(imported_module)

        if hasattr(imported_module, "__user_info__"):
            USER_INFO.append(imported_module)

        if hasattr(imported_module, "__import_data__"):
            DATA_IMPORT.append(imported_module)

        if hasattr(imported_module, "__export_data__"):
            DATA_EXPORT.append(imported_module)

        if hasattr(imported_module, "__chat_settings__"):
            CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

        if hasattr(imported_module, "__user_settings__"):
            USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module
    
    
    bot_modules = ""
    j = 1
    for i in ALL_MODULES:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1
    print("+===============================================================+")
    print("|                              WBB                              |")
    print("+===============+===============+===============+===============+")
    print(bot_modules)
    print("+===============+===============+===============+===============+")

    LOG.print(f"[bold red]BOT STARTED AS {BOT_NAME}!")

    try:
        LOG.print("[yellow]Sending online status")              
        await app.send_message(-1001698076323, "Bot started!")
    except Exception:
        pass
    await idle()
    await aiohttpsession.close()   
    LOG.print("[yello] stopping client") 
    await pgram.stop()
    LOG.print("[yellow]Cancelling asyncio tasks")
    for task in asyncio.all_tasks():
        task.cancel()
    LOG.print("[yello]Dead!")

async def send_help(app,chat, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    await app.send_photo(
        chat_id=chat,
        photo=random.choice(PM_PHOTOS),
        caption=text,
        parse_mode=ParseMode.MARKDOWN,      
        reply_markup=keyboard,
    )

@pgram.on_message(filters.command("start") & filters.group)
async def group_start(_, message):
    chat_id = message.chat.id
    if len(message.text.split()) >= 1:
        args = message.text.split(None,1)[1]
        if args[0].lower() == "help":
            await send_help(app=pgram,chat = chat_id,text=HELP_STRINGS)

        elif args[0].lower().startswith("ghelp_"):
            mod = args[0].lower().split("_", 1)[1]
            if not HELPABLE.get(mod, False):
                return
            await send_help(
                app = pgram
                chat=chat_id,
                HELPABLE[mod].__help__,
                InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back")]]
                ),
            )
                
    else:
        await message.reply_photo(
            START_IMG,
            caption="ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !\n<b>ɪ ᴅɪᴅɴ'ᴛ sʟᴇᴘᴛ sɪɴᴄᴇ:</b> <code>{}</code>".format(
                uptime
            ),
            parse_mode=ParseMode.HTML,
        )
        return                
           


if __name__ == "__main__" :
    install()
    loop.run_until_complete(Friday_Robot())

