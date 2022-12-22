import asyncio
import os
import re
import time
import random 
from datetime import datetime
import importlib
from platform import python_version as y
from sys import argv
from typing import Optional
from pyrogram import filters, __version__ as pyrover
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram import __version__ as telever
from pyrogram.types import CallbackQuery 
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown

from TeleBot import (
    BOT_NAME,
    BOT_USERNAME,
    CERT_PATH,
    DONATION_LINK,
    LOG,
    OWNER_ID,
    PORT,    
    SUPPORT_CHAT,
    BOT_TOKEN as TOKEN,
    URL,
    WEBHOOK,
    StartTime,
    dispatcher,
    pgram,
    telethn,    
    updater,
    get_readable_time
)


from TeleBot.modules import ALL_MODULES
#from TeleBot.modules.helper_funcs.chat_status import is_user_admin
from TeleBot.modules.helper_funcs.misc import paginate_modules
from pyrogram import filters

#loop = asyncio.get_event_loop()

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

HELP_STRINGS = """
ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs.
"""

DONATE_STRING = """ʜᴇʏ ʙᴀʙʏ,
  ʜᴀᴩᴩʏ ᴛᴏ ʜᴇᴀʀ ᴛʜᴀᴛ ʏᴏᴜ ᴡᴀɴɴᴀ ᴅᴏɴᴀᴛᴇ.

ʏᴏᴜ ᴄᴀɴ ᴅɪʀᴇᴄᴛʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ [ᴅᴇᴠᴇʟᴏᴩᴇʀ](https://t.me/anonymous_was_bot) ғᴏʀ ᴅᴏɴᴀᴛɪɴɢ ᴏʀ ʏᴏᴜ ᴄᴀɴ ᴠɪsɪᴛ ᴍʏ [sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ](https://t.me/DevilsHeavenMF) ᴀɴᴅ ᴀsᴋ ᴛʜᴇʀᴇ ᴀʙᴏᴜᴛ ᴅᴏɴᴀᴛɪᴏɴ."""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}
#all_modules = ""
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




# do not async
def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    dispatcher.bot.send_photo(
        chat_id=chat_id,
        photo=random.choice(PM_PHOTOS),
        caption=text,
        parse_mode=ParseMode.MARKDOWN,      
        reply_markup=keyboard,
    )



def start(update: Update, context: CallbackContext):
    args = context.args    
    uptime = get_readable_time((time.time() - StartTime))    
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back")]]
                    ),
                )

            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name            
            update.effective_message.reply_photo(
                photo=random.choice(PM_PHOTOS),
                caption=PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME,uptime),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
                
            )
    else:
        update.effective_message.reply_photo(
            START_IMG,
            caption="ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !\n<b>ɪ ᴅɪᴅɴ'ᴛ sʟᴇᴘᴛ sɪɴᴄᴇ​:</b> <code>{}</code>".format(
                uptime
            ),
            parse_mode=ParseMode.HTML,
        )


def error_handler(update, context):
    """Log the error and send a telegram message to notify the developer."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    LOG.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    message = (
        "An exception was raised while handling an update\n"
        "<pre>update = {}</pre>\n\n"
        "<pre>{}</pre>"
    ).format(
        html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False)),
        html.escape(tb),
    )

    if len(message) >= 4096:
        message = message[:4096]
    # Finally, send the message
    context.bot.send_message(chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML)


# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors




def help_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "» *ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ​​* *{}* :\n".format(
                    HELPABLE[module].__mod_name__
                )
                + HELPABLE[module].__help__
            )
            query.message.edit_caption(
                text,
                parse_mode=ParseMode.MARKDOWN,                
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back")]]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.edit_caption(
                HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, HELPABLE, "help")
                ),
            )

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.edit_caption(
                HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, HELPABLE, "help")
                ),
            )

        elif back_match:
            query.message.edit_caption(
                HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")
                ),
            )

        context.bot.answer_callback_query(query.id)

    except BadRequest:
        pass


def get_help(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
            module = args[1].lower()
            update.effective_message.reply_photo(
                photo=random.choice(HELP_IMG),
                caption=f"ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪsᴛ ᴏғ {module.capitalize()}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ʜᴇʟᴘ​",
                                url="https://t.me/{BOT_USERNAME}?start=help"
                                ),
                            
                        ]
                    ]
                ),
            )
            return
        update.effective_message.reply_photo(
            photo=random.choice(HELP_IMG),
            caption="» ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴘᴏssɪʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs..",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴏᴩᴇɴ ɪɴ ᴩʀɪᴠᴀᴛᴇ",
                            url="https://t.me/{}?start=help".format(
                                context.bot.username
                            ),
                        )
                    ],
                    
                ]
            ),
        )
        return

    elif len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        text = (
            "Here is the available help for the *{}* module:\n".format(
                HELPABLE[module].__mod_name__
            )
            + HELPABLE[module].__help__
        )
        send_help(
            chat.id,
            text,
            InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back")]]
            ),
        )

    else:
        send_help(chat.id, HELP_STRINGS)


def migrate_chats(update: Update, context: CallbackContext):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOG.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOG.info("Successfully migrated!")
    raise DispatcherHandlerStop


    
def main():
    @app.on_message(filters.sticker)
    async def my_handler(client, message):
        print(message)       



    
    
    LOG.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
    for all_module in ALL_MODULES:    
        LOG.print(
                f"✨ [bold cyan]sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ: [green]{all_module}.py"
            )

    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.send_photo(
                f"@{SUPPORT_CHAT}",
                photo=START_IMG,
                caption=f"""
ㅤ🥀 {BOT_NAME} ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ...

┏•❅────✧❅✦❅✧────❅•┓
ㅤ★ **ᴘʏᴛʜᴏɴ :** `{y()}`
ㅤ★ **ʟɪʙʀᴀʀʏ :** `{telever}`
ㅤ★ **ᴩʏʀᴏɢʀᴀᴍ :** `{pyrover}`
┗•❅────✧❅✦❅✧────❅•┛""",
                parse_mode=ParseMode.MARKDOWN,
            )
        except Unauthorized:
            LOG.print(
                f"[bold red]ʙᴏᴛ ɪs'ɴᴛ ᴀʙʟᴇ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴛᴏ @{SUPPORT_CHAT} !"
            )
        except BadRequest as e:
            LOG.print(f"[bold red]{e.message}")
    
    
    start_handler = CommandHandler("start", start,run_async=True)
    help_handler = CommandHandler("help", get_help,run_async=True)
    help_callback_handler = CallbackQueryHandler(help_button, pattern=r"help_.*",run_async=True)             
    migrate_handler = MessageHandler(Filters.status_update.migrate, migrate_chats)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)            
    dispatcher.add_handler(help_callback_handler)    
    dispatcher.add_handler(migrate_handler)
    

    dispatcher.add_error_handler(error_callback)

    if WEBHOOK:
        LOG.print("[bold yellow]ᴜsɪɴɢ ᴡᴇʙʜᴏᴏᴋs.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN, certificate=open(CERT_PATH, "rb"))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOG.print("[bold yellow]ᴜsɪɴɢ ʟᴏɴɢ ᴘᴏʟʟɪɴɢ.")
        updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
   
    
  
    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()



if __name__ == "__main__": 
    telethn.start(bot_token=TOKEN)       
    main()

    
