import requests
from TeleBot import pgram
from pyrogram import filters
from random import randint

@pgram.on_message(filters.command("wal"))
async def wallpaper (_,msg):
    if len(msg.command) < 2:
         await msg.reply_text("ʜᴇʏ ɴᴏᴏʙ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.")
         return 
    else:
         pass

    query=(
       msg.text.split(None,1)[1]
       if len(msg.command) < 3
       else msg.text.split(None,1)[1].replace(" ","%20")
       )
    
    if not query:
        await msg.reply_text("ʜᴇʏ ɴᴏᴏʙ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.")
    else:
        pass  

    url=f"https://wallhaven.cc/api/v1/search?q={query}"
    re=requests.get(url).json()
    walls = re.get("data")
   # try:
    wall_index = randint(0, len(walls) -1)
    wallpaper = walls[wall_index]
    pic = wallpaper.get("path")
    preview = wallpaper.get("thumbs")
    print(preview("large"))
  #  except Exception:
  #      await msg.reply_text("refine your search")
    
    
    

__help__ = "hii"
__mod_name__ = "sup"
