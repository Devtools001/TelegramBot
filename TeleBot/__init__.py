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
    level=logging.INFO,
)

LOG=logging.getLogger("Stark-industry")

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOG.error("you must have python version of atleast 3.6, bot quitting")
    quit(1)
else:
  LOG.info("Noice you have python version greater than 3.6")

StartTime = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

ENV=bool(os.environ.get("ENV",False))
if ENV:
    API_ID=int(os.environ.get("API_ID",None))
    API_HASH=str(os.environ.get("API_HASH",None))
    BOT_TOKEN=str(os.environ.get("BOT_TOKEN",None))
    WORKERS = int(os.environ.get("WORKERS", 8))
    URL = os.environ.get("URL", "")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    BOT_NAME = str(os.environ.get("BOT_NAME",None))
    BOT_USERNAME = str(os.environ.get("BOT_USERNAME",None))
    DONATION_LINK = str(os.environ.get("DONATION_LINK",None))
    OWNER_ID = int(os.environ.get("OWNER_ID",None))
    PORT = int(os.environ.get("PORT",None))
    SUPPORT_CHAT = str(os.environ.get("SUPPORT_CHAT",None))
    CERT_PATH = os.environ.get("CERT_PATH")
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
     
else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    BOT_TOKEN=Config.BOT_TOKEN
    WORKERS=Config.WORKERS
    URL=Config.URL
    LOAD=Config.LOAD
    NO_LOAD = Config.NO_LOAD
    BOT_NAME = Config.BOT_NAME
    BOT_USERNAME = Config.BOT_USERNAME
    DONATION_LINK = Config.DONATION_LINK
    OWNER_ID = Config.OWNER_ID
    PORT = Config.PORT
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    CERT_PATH = Config.CERT_PATH
    WEBHOOK = Config.WEBHOOK

updater=Fday.Updater(BOT_TOKEN,workers=WORKERS,use_context=True)
dispatcher=updater.dispatcher

telethn = TelegramClient("TelegramBot", API_ID, API_HASH)


pgram = Client (
      "TeleBot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
      )
