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
    url=f"https://api.safone.me/wall?query={query}&limit=1"
    re=requests.get(url).json()
    results=re["results"]
    index = randint(0, len(results) - 1)
    wallpaper = wallpapers[index]    
    wallpaper = wallpaper["imageUrl"]    
    preview=wallpaper["thumbUrl"]
    title=wallpaper["title"]
    await pgram.send_photo(msg.chat.id,preview)
    await pgram.send_document(msg.chat.id,pic)
        
