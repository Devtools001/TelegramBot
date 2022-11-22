import importlib
from TeleBot import (
    pgram,
    LOG,
    URL,
    updater,
    dispatcher
    )
from pyrogram import filters


IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in FRIDAY_MODULES:
    imported_module = importlib.module_name("TeleBot.modules."+module_name)   
             
@pgram.on_message(filters.command("start"))
async def start_cmd(_, message):
    
    


if __name__ == "__main__":
    LOG.info("started")
    pgram.run()

