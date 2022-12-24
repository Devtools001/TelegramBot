import requests
from TeleBot import pgram
from pyrogram import filters
from random import randint

@pgram.on_message(filters.command("wal"))
async def wallpaper (_,msg):
    url=f"https://api.safone.me/wall?query=Naruto"
    re=requests.get(url).json()
    print(re)

__help__ = "hii"
__mod_name__ = "sup"
