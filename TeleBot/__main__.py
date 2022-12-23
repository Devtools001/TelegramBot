import time
import asyncio
import importlib
import re
import random
from contextlib import closing, suppress

from uvloop import install
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from TeleBot import (
    BOT_NAME,
    BOT_USERNAME,        
    aiohttpsession,
    pgram as app,
    LOG,
    StartTime,
    get_readable_time
)
from TeleBot.modules import ALL_MODULES
from TeleBot.utilities.misc import paginate_modules
from TeleBot.utilities.constant import MARKDOWN
from pyrogram.enums import ChatType, ParseMode 
from TeleBot.resources.Data import *

loop = asyncio.get_event_loop()
uptime = get_readable_time((time.time() - StartTime))

HELP_STRINGS = """
ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs.
"""

HELPABLE = {}
async def start_bot():
    global HELPABLE, IMPORTED
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
    await app.stop()
    LOG.print("[yellow]Cancelling asyncio tasks")
    for task in asyncio.all_tasks():
        task.cancel()
    LOG.print("[yello]Dead!")


home_keyboard_pm = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Commands ❓", callback_data="bot_commands"
            ),
            InlineKeyboardButton(
                text="Repo 🛠",
                url="https://github.com/thehamkercat/WilliamButcherBot",
            ),
        ],
        [
            InlineKeyboardButton(
                text="System Stats 🖥",
                callback_data="stats_callback",
            ),
            InlineKeyboardButton(
                text="Support 👨", url="http://t.me/WBBSupport"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Add Me To Your Group 🎉",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
    ]
)

home_text_pm = (
        f"Hey there! My name is {BOT_NAME}. I can manage your "
        + "group with lots of useful features, feel free to "
        + "add me to your group."
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

async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """Hello {first_name}, My name is {bot_name}.
I'm a group management bot with some useful features.
You can choose an option below, by clicking a button.
Also you can ask anything in Support Group.
""".format(
            first_name=name,
            bot_name=BOT_NAME,
        ),
        keyboard,
    )

@app.on_message(filters.command("start") & filters.group)
async def start(_, message):       
    print(message.chat.type)    
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name == "mkdwn_help":
            await message.reply(
                MARKDOWN, parse_mode="html", disable_web_page_preview=True
            )
        elif "_" in name:
            module = name.split("_", 1)[1]
            text = (
                    f"Here is the help for **{HELPABLE[module].__mod_name__}**:\n"
                    + HELPABLE[module].__help__
            )
            await message.reply(text, disable_web_page_preview=True)
        elif name == "help":
            text, keyb = await help_parser(message.from_user.first_name)
            await message.reply(
                text,
                reply_markup=keyb,
            )
    else:
        await message.reply_photo(
            START_IMG,
            caption="ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !\n<b>ɪ ᴅɪᴅɴ'ᴛ sʟᴇᴘᴛ sɪɴᴄᴇ​:</b> <code>{}</code>".format(
                uptime
            ),
            parse_mode=ParseMode.HTML,
        )
    return

@app.on_message(filters.command("start") & filters.private)
async def start(_, message):
    first_name = message.from_user.first_name                        
    await app.send_photo(
    message.chat.id,    
    photo=random.choice(PM_PHOTOS),
    caption=PM_START_TEXT.format(first_name,BOT_NAME,uptime),
    reply_markup=InlineKeyboardMarkup(START_BUTTONS),
    parse_mode=ParseMode.MARKDOWN,
                    
            )     
                  

@app.on_message(filters.command("help") & filters.group)
async def help_command(_, message):
    if len(message.command) >= 2:
            name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
            if str(name) in HELPABLE:
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Click here",
                                url=f"t.me/{BOT_USERNAME}?start=help",
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
    return        
    

@app.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    if len(message.command) >= 2:
            name = (message.text.split(None, 1)[1]).replace(" ", "_").lower()
            if str(name) in HELPABLE:
                text = (
                        f"Here is the help for {HELPABLE[name].mod_name}:\n"
                        + HELPABLE[name].help
                )
                await message.reply(text, disable_web_page_preview=True)
            else:
                text, help_keyboard = await help_parser(
                    message.from_user.first_name
                )
                await message.reply(
                    text,
                    reply_markup=help_keyboard,
                    disable_web_page_preview=True,
                )
    else:
        text, help_keyboard = await help_parser(
        message.from_user.first_name
            )
        await message.reply(
                text, reply_markup=help_keyboard, disable_web_page_preview=True
            )        
    return        
    


@app.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=text,
        reply_markup=keyboard,
    )
    await CallbackQuery.message.delete()





@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""
Hello {query.from_user.first_name}, My name is {BOT_NAME}.
I'm a group management bot with some usefule features.
You can choose an option below, by clicking a button.
Also you can ask anything in Support Group.

General command are:
 - /start: Start the bot
 - /help: Give this message
 """
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = (
                "{} **{}**:\n".format(
                    "Here is the help for", HELPABLE[module].__mod_name__
                )
                + HELPABLE[module].__help__
        )

        await query.message.edit_caption(
            caption=HELP_STRINGS,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("back", callback_data="help_back")]]
            ),
            
        )
    elif home_match:
        await app.send_message(
            query.from_user.id,
            text=HELP_STRINGS,
            reply_markup=home_keyboard_pm,
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit_caption(
            caption=HELP_STRINGS,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit_caption(
            caption=HELP_STRINGS,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            
        )

    elif back_match:
        await query.message.edit_caption(
            caption=HELP_STRINGS,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit_caption(
            caption=HELP_STRINGS,
            reply_markup=keyboard,
            
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    install()
    loop.run_until_complete(start_bot())
        
            
        
