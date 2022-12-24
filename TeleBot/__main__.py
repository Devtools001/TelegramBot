import os
import asyncio
import re
import time
import uvloop
import random 
import importlib
from contextlib import closing, suppress
from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup,
    CallbackQuery)

from pyrogram.errors import BadRequest 
from pyrogram import filters,idle
from TeleBot.utilities.misc import paginate_modules
from TeleBot import (
    BOT_NAME,
    BOT_USERNAME,        
    aiohttpsession,
    pgram,
    LOG,
    StartTime,
    get_readable_time,
    StartTime)

from rich.table import Table
from pyrogram.enums import ParseMode 
from TeleBot.modules import ALL_MODULES
from TeleBot.resources.Data import *

loop = asyncio.get_event_loop() 

IMPORTED = {}
HELPABLE = {}
async def Friday_Robot():
    global IMPORTED,HELPABLE
    for module_name in ALL_MODULES:
        imported_module = importlib.import_module("TeleBot.modules." +
                                              module_name)
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

    
    os.system("clear")
    await asyncio.sleep(2)
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(LOG_MSG)
    LOG.print(header)
    await asyncio.sleep(2)       
    LOG.print("ғᴏᴜɴᴅ {} ᴍᴏᴅᴜʟᴇs".format(len(ALL_MODULES)) + "\n")
    for all_module in ALL_MODULES:    
        LOG.print(
                f"✨ [bold cyan]sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ: [green]{all_module}.py"
            )
    print()
    LOG.print(f"[bold red] ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ᴀs {BOT_NAME}!")   
    try:                    
        await pgram.send_photo(f@{SUPPORT_CHAT},
        photo=START_IMG,
        caption=f"""
        🥀 {BOT_NAME} ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ...
        ┏•❅────✧❅✦❅✧────❅•┓
        ㅤ★ **ᴘʏᴛʜᴏɴ :** `{y()}`
        ㅤ★ **ʟɪʙʀᴀʀʏ :** `{telever}`
        ㅤ★ **ᴩʏʀᴏɢʀᴀᴍ :** `{pyrover}`
        ┗•❅────✧❅✦❅✧────❅•┛
 """
       )
    except Exception:
        LOG.print("[bold red]ʙᴏᴛ ɪs'ɴᴛ ᴀʙʟᴇ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ @{SUPPORT_CHAT} !")
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
    uptime = get_readable_time((time.time() - StartTime))
    chat_id = message.chat.id    
    if len(message.text.split()) > 1:
        args = message.text.split(None,1)[1].lower()
        if args == "help":
            await send_help(app=pgram,chat = chat_id,text = HELP_STRINGS)
        elif args.startswith("ghelp_"):
            mod = args.lower().split("_", 1)[1]
            if not HELPABLE.get(mod, False):
                return
            await send_help(
                pgram,
                chat_id,
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
            
@pgram.on_message(filters.command("start") & filters.private)
async def start(_, message):
    uptime = get_readable_time((time.time() - StartTime))  
    first_name = message.from_user.first_name                        
    await pgram.send_photo(
    message.chat.id,    
    photo=random.choice(PM_PHOTOS),
    caption=PM_START_TEXT.format(first_name,BOT_NAME,uptime),
    reply_markup=InlineKeyboardMarkup(START_BUTTONS),
    parse_mode=ParseMode.MARKDOWN,                   
            )
    return 
@pgram.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(app,query):    
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data) 
               
    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "» **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ** **{}** :\n".format(
                    HELPABLE[module].__mod_name__
                )
                + HELPABLE[module].__help__
            )
            await query.message.edit_caption(
                text,
                parse_mode=ParseMode.MARKDOWN,                
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back")]]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match.group(1))
            await query.message.edit_caption(
                HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(paginate_modules(curr_page - 1, HELPABLE, "help")
             ),
          )
                                   
        elif next_match:
            next_page = int(next_match.group(1))
            await query.message.edit_caption(
                HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, HELPABLE, "help")
                ),
            )                   

        elif back_match:
           await query.message.edit_caption(
                HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")
                ),
            )            

        return await app.answer_callback_query(query.id)

    except BadRequest:
        pass

@pgram.on_message(filters.command("help") & filters.group)
async def get_help(_, message):
    if len(message.command) >= 2:
        mod_name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
        if str(mod_name) in HELPABLE:
            key = InlineKeyboardMarkup(
               [[InlineKeyboardButton(
                            text="Click here",
                            url=f"t.me/{BOT_USERNAME}?start=help_{mod_name}")]])                                                                        
            await message.reply(
                f"ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴀʙᴏᴜᴛ {mod_name}",
                reply_markup=key,
             )

        else:
            await message.reply_text(
             text = "Pᴍ ᴍᴇ ғᴏʀ ᴛʜɪs",reply_markup=keyboard)                                                                                                                                   
            return            
    else:
      await message.reply_photo(  
       photo=random.choice(HELP_IMG),
       caption=f" ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴘᴏssɪʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs..",
       reply_markup=InlineKeyboardMarkup(
                   [[InlineKeyboardButton(
                        text="ʜᴇʟᴘ",
                        url=f"https://t.me/{BOT_USERNAME}?start=help")
                     ]]))
                     
@pgram.on_message(filters.command("help") & filters.private)  
async def private_help(_, message):
    chat = message.chat
    await send_help(app=pgram,chat=chat.id,text=HELP_STRINGS)                       
            
                    
                        
                    
                                                                    
         
if __name__ == "__main__" :
    uvloop.install()
    loop.run_until_complete(Friday_Robot())

