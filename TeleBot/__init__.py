
import os
import logging
import time 
import sys
import asyncio
import datetime
#import telegram.ext as Fday
from pyrogram import Client,filters
from config import Friday as Config
from rich.table import Table
from rich.console import Console
#from telethon import TelegramClient 
from aiohttp import ClientSession
from redis import StrictRedis
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger("FRIDAY")

LOG = Console()
StartTime = time.time()
loop = asyncio.get_event_loop()
aiohttpsession = ClientSession()
mongo_client = MongoClient("mongodb+srv://GOJO:liyaxlambert*143@cluster0.fhbjzax.mongodb.net/?retryWrites=true&w=majority")
db = mongo_client.FRIDAY
#print(db)


MOD_LOAD = []
MOD_NOLOAD = []

if sys.version_info[0] < 3 and sys.version_info[1] < 6:
    LOG.print("[bold red]ʏᴏᴜ ᴍᴜsᴛ ʜᴀᴠᴇ ᴀ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ᴏғ 3.6. ᴇxɪᴛɪɴɢ.......\n")
    sys.exit(1)

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
    DRAGONS = int(os.environ.get("DRAGONS",None)).split(",")
    DEV_USERS = int(os.environ.get("DEV_USERS",None)).split(",")
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
    DONATION_LINK = Config.DONATION_LINK
    OWNER_ID = Config.OWNER_ID
    PORT = Config.PORT
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    CERT_PATH = Config.CERT_PATH
    WEBHOOK = Config.WEBHOOK
    DRAGONS = Config.DRAGONS
    DEV_USERS = Config.DEV_USERS

#SUDO_USERS = filters.user()

BOT_NAME  = ""
BOT_USERNAME = ""
BOT_ID = 0
MENTION_BOT = ""

pgram = Client (
      "TeleBot",
      api_id=API_ID,
      api_hash=API_HASH,
      bot_token=BOT_TOKEN
      )

testdb = db.test
post = {"owner" : "Steve",
        "user_id" : 29292929,
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}




async def Friday():
    global BOT_NAME,BOT_USERNAME,BOT_ID,MENTION_BOT
    LOG.print("[bold red]starting your bot")
    await pgram.start()
    app = await pgram.get_me()
    BOT_ID = app.id
    BOT_USERNAME = app.username    
    if app.last_name:
        BOT_NAME = app.first_name + " " + app.last_name
    else:
        BOT_NAME = app.first_name

    MENTION_BOT = app.mention

REDIS_URL = "redis://default:Gr7TEJsTmoJ5IoKYXsaa@containers-us-west-157.railway.app:7065"

REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)

try:
    REDIS.ping()
    LOG.print("[bold red]Your redis server is now alive!")

except BaseException:
    raise Exception("Your redis server is not alive, please check again.")

finally:
    REDIS.ping()
    LOG.print("[bold red]Your redis server is now alive!")

    
    
loop.run_until_complete(Friday())    


