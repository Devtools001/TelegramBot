import requests
from TeleBot import pgram
from pyrogram import filters
from random import randint

@pgram.on_message(filters.command("wallpaper"))
async def wallpaper (_,msg):  
    try:
        url=f"https://wallhaven.cc/api/v1/search"
        re=requests.get(url).json()    
        stark=re["data"]
        wall = randint(0, len(stark) -1)
        main = stark[wall]["path"]
        preview = stark[wall]["path"]
        url = stark[wall]["url"]
        category = stark[wall]["category"]
        await msg.reply_photo(preview, caption="⚡ ᴘʀɪᴠɪᴇᴡ")
        await msg.reply_document(main, caption=f"💫 ᴄᴀᴛᴇɢᴏʀʏ :- {category}")

    except Exception:
        pass
    
    

__help__ = "hii"
__mod_name__ = "sup"
