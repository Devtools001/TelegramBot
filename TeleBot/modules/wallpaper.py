from random import randint
import requests
from TeleBot import pgram
from pyrogram import filters

@pgram.on_message(filters.command("wall"))
async def wall(_,msg):
    if len(msg.command) < 2:
        await msg.reply_text("give something to search")
    else:
        pass
    query=(
       msg.text.split(None,1)[1]
       if len(msg.command) < 3
       else msg.text.split(None,1)[1].replace(" ","%20")
       )
    url=f"https://api.safone.me/wall?query={query}"
    re=requests.get(url).json()
    walls = re.get("results")
    wall_index = randint(0, len(walls) -1)
    wallpaper = walls[wall_index]
    pic = wallpaper.get("imageUrl")
    preview=wallpaper.get("thumbUrl") 
    title = wallpaper.get("title")
    try:
        await pgram.send_photo(msg.chat.id,preview, caption="⚡ ᴘʀɪᴠɪᴇᴡ")
        await pgram.send_document(msg.chat.id,pic, caption=f"⚡ ᴛɪᴛʟᴇ - {title}")
    except Exception :
        await msg.reply_text("No results found!")            
    
