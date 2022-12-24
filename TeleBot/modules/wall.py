import requests
from TeleBot import pgram
from pyrogram import filters
from random import randint

@pgram.on_message(filters.command("wal"))
async def wallpaper (_,msg):
    url=f"https://wallhaven.cc/api/v1/search?q=Naruto"
    re=requests.get(url).json()
    print(re)

__help__ = "hii"
__mod_name__ = "sup"
