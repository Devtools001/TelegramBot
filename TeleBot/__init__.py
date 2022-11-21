import os
import logging
import time 
import sys
import telegram.ext as Fday
from pyrogram import Client
from config import Friday as Config


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG=logging.getLogger("Stark-industry")

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOG.error("you must have python version of atleast 3.6, bot quitting")
    quit(1)


ENV=bool(os.environ.get("ENV",False))

if ENV:
    API_ID=int(os.environ.get("API_ID",None))
    API_HASH=str(os.environ.get("API_HASH",None))
    BOT_TOKEN=str(os.environ.get("BOT_TOKEN",None))
    WORKERS = int(os.environ.get("WORKERS", 8))

else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    BOT_TOKEN=Config.BOT_TOKEN


updater=Fday.Updater(BOT_TOKEN,workers=WORKERS,use_context=True)
dispatcher=updater.dispatcher


pgram = Client (
      "TeleBot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
      )
