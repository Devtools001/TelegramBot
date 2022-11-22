import os
import logging
import time 
import sys
import telegram.ext as Fday
from pyrogram import Client
from config import Friday as Config


logging.basicConfig(
    style="{",format="{asctime} -- {name} -- {levelname} -- {message}",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.DEBUG,
)

LOG=logging.getLogger("Stark-industry")

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOG.error("you must have python version of atleast 3.6, bot quitting")
    quit(1)
else:
  LOG.info("Noice you have python version greater than 3.6")

ENV=bool(os.environ.get("ENV",False))

if ENV:
    API_ID=int(os.environ.get("API_ID",None))
    API_HASH=str(os.environ.get("API_HASH",None))
    BOT_TOKEN=str(os.environ.get("BOT_TOKEN",None))
    WORKERS = int(os.environ.get("WORKERS", 8))
    URL = os.environ.get("URL", "")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()

else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    BOT_TOKEN=Config.BOT_TOKEN
    WORKERS=Config.WORKERS
    URL=Config.URL
    LOAD=Config.LOAD
    NO_LOAD = Config.NO_LOAD

updater=Fday.Updater(BOT_TOKEN,workers=WORKERS,use_context=True)
dispatcher=updater.dispatcher


pgram = Client (
      "TeleBot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
      )
