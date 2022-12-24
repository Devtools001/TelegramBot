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
    
    red=re["data"]
    wall = randint(0, len(red) -1)
    print(red[wall]["path"])
    print(red[wall]["thumbs"]["large"]

  #  except Exception:
  #      await msg.reply_text("refi sone your search")
    
    
    

__help__ = "hii"
__mod_name__ = "sup"
