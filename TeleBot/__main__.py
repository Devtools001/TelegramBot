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

from pyrogram.errors import BadRequest,Unauthorized 
from pyrogram import filters,idle
from TeleBot.utilities.misc import paginate_modules
from TeleBot import (
    BOT_NAME,
    BOT_USERNAME,  
    SUPPORT_CHAT,      
    aiohttpsession,
    pgram,
    LOG,
    StartTime,
    get_readable_time,
    DONATION_LINK,
    OWNER_ID)

from rich.table import Table
from pyrogram.enums import ParseMode,ChatType
from pyrogram import __version__ as pyrover
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
        await pgram.send_photo(f"@{SUPPORT_CHAT}",
        photo=START_IMG,
        caption=SUPPORT_SEND_MSG.format(BOT_NAME,pyrover)
       )
    except Exception as e:
        print(e)
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

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Help ❓",
                url=f"t.me/{BOT_USERNAME}?start=help",
            ),
            InlineKeyboardButton(
                text="Repo 🛠",
                url="https://github.com/thehamkercat/WilliamButcherBot",
            ),
        ],
        [
            InlineKeyboardButton(
                text="System Stats 💻",
                callback_data="stats_callback",
            ),
            InlineKeyboardButton(text="Support 👨", url="t.me/WBBSupport"),
        ],
    ]
)

@pgram.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def group_start(_, message):    
    uptime = get_readable_time((time.time() - StartTime))
    chat_id = message.chat.id  
    if message.chat.type != ChatType.PRIVATE : 
        if len(message.text.split()) > 1:
            args = message.text.split(None,1)[1].lower()
            print(args)
            if args == "help":
                app,chat,text, keyboard = await send_help(pgram,chat_id,HELP_STRINGS)
                await pgram.send_message(
                    chat_id,
                    HELP_STRINGS,
                    reply_markup=keyboard,
                )
            elif "_" in args:
                module = args.split("_", 1)[1]
                text = (
                        f"Here is the help for **{HELPABLE[module].__mod_name__}**:\n"
                        + HELPABLE[module].__help__
                )
                await message.reply(text, disable_web_page_preview=True)                
        else:
            await message.reply_photo(
                START_IMG,
                caption="ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !\n<b>ɪ ᴅɪᴅɴ'ᴛ sʟᴇᴘᴛ sɪɴᴄᴇ:</b> <code>{}</code>".format(
                    uptime
                ),
            parse_mode=ParseMode.HTML,
            )
            return     
    else:
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

@pgram.on_message(filters.command(["help",f"help@{BOT_USERNAME}"]))
async def get_help(_, message):
    if message.chat.type != ChatType.PRIVATE:
        if len(message.command) >= 2:
            name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
            if str(name) in HELPABLE:
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Click here",
                                url=f"t.me/{BOT_USERNAME}?start=help_{name}",
                            )
                        ],
                    ]
                )
                await message.reply(
                    f"Click on the below button to get help about {name}",
                    reply_markup=key,
                )
            else:
                await message.reply(
                    "PM Me For More Details.", reply_markup=keyboard
                )
        else:
            await message.reply(
                "Pm Me For More Details.", reply_markup=keyboard
            )
    else:
        if len(message.command) >= 2:
            name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
            if str(name) in HELPABLE:
                text = (
                        f"Here is the help for **{HELPABLE[name].__MODULE__}**:\n"
                        + HELPABLE[name].__HELP__
                )
                await message.reply(text, disable_web_page_preview=True)
            else:
                text, help_keyboard = await send_help(
                    pgram,message.chat.id,text
                )
                await message.reply(
                    HELP_STRINGS,
                    reply_markup=help_keyboard,
                    disable_web_page_preview=True,
                )
        else:
            text, help_keyboard = await send_help(
                    pgram,message.chat.id,HELP_STRINGS
                )
            await message.reply(
                text, reply_markup=help_keyboard, disable_web_page_preview=True
            )
    return
                      
                
                     
@pgram.on_message(filters.command("donate"))  
async def donate(_, message):
    if message.chat.type == ChatType.PRIVATE:
        if message.from_user.id == OWNER_ID:
            await message.reply_text("ɪ ᴀᴍ ғʀᴇᴇ ᴛᴏ ᴜsᴇ ┌⁠(⁠・⁠。⁠・⁠)⁠┘⁠♪") 
        else:
            await message.reply_text(f"Yᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴅᴏɴᴀᴛᴇ ᴛᴏ ᴛʜᴇ ᴘᴇʀsᴏɴ ᴄᴜʀʀᴇɴᴛʟʏ ʀᴜɴɴɪɴɢ ᴍᴇ [ʜᴇʀᴇ]({DONATION_LINK})")                                                
    else:
        if message.from_user.id == OWNER_ID:
            await message.reply_text("ɪ ᴀᴍ ғʀᴇᴇ ᴛᴏ ᴜsᴇ ┌⁠(⁠・⁠。⁠・⁠)⁠┘⁠♪") 
        else:
            await message.reply_text("I'ᴠᴇ PM'ᴇᴅ ʏᴏᴜ ᴀʙᴏᴜᴛ ᴅᴏɴᴀᴛɪɴɢ ᴛᴏ ᴍʏ ᴄʀᴇᴀᴛᴏʀ!")
            try:
                await pgram.send_message(message.from_user.id,text=f"[ʜᴇʀᴇ ɪs ᴛʜᴇ ᴅᴏɴᴀᴛɪᴏɴ ʟɪɴᴋ]({DONATION_LINK})")
            except Unauthorized:                
                await message.reply_text("Cᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ PM ғɪʀsᴛ ᴛᴏ ɢᴇᴛ ᴅᴏɴᴀᴛɪᴏɴ ɪɴғᴏʀᴍᴀᴛɪᴏɴ")
                                
 

    
                    
                        
                    
                                                                    
         
if __name__ == "__main__" :
    uvloop.install()
    loop.run_until_complete(Friday_Robot())

