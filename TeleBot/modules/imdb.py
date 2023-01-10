import requests
from TeleBot import pgram
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@pgram.on_message(filters.command("imdb"))
async def _IMDb(_,msg):
    if len(msg.command) < 2:        
        return await msg.reply_text("give me a query to search")
    
    text = msg.text.split(None, 1)[1].replace(" ", "%20")
    
    url=f"https://api.safone.me/tmdb?query={text}%20&limit=1"
    ok=requests.get(url).json()        
    re=ok["results"][0]
    if not re:       
        await msg.reply_text("nothing")
    else:
        title=re["title"]
        poster=re["poster"]
        runtime=re["runtime"]
        rating=re["rating"]
        releaseDate=re["releaseDate"]
        popularity=re["popularity"]
        status=re["status"]
        homepage=re["homepage"]
        imdbId=re["imdbId"]
        imdbLink=re["imdbLink"]
        id=re["id"]        
        overview=re["overview"]     
        genres = ""
        gen=re["genres"]   
        for i in gen:
            genres += i + ","                                   
        await msg.reply_photo(poster,
    caption=f"""
📀 **ᴛɪᴛʟᴇ :** {title}

⏱️ **ʀᴜɴᴛɪᴍᴇ :** {runtime}ᴍɪɴ
🌟 **ʀᴀᴛɪɴɢ :** {rating}/10
🗳️ **ɪᴅ :** {id}

📆 **ʀᴇʟᴇᴀsᴇ ᴅᴀᴛᴇ :** {releaseDate}
🎭 **ɢᴇɴʀᴇ :** {genres}
🥂 **ᴘᴏᴘᴜʟᴀʀɪᴛʏ :** {popularity}

⚡ **sᴛᴀᴛᴜs :** {status}
🎫 **ɪᴍᴅʙ ɪᴅ :** {imdbId}

🗒  **ᴘʟᴏᴛ :** `{overview}`
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🎟️ 𝙸𝙼𝙳ʙ",
                        url=imdbLink,
                    ),
                ],
            ],
        ),
    )
    
       
__help__="""
「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /IMDb «ᴍᴏᴠɪᴇ ɴᴀᴍᴇ» : ɢᴇᴛ ғᴜʟʟ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴀ ᴍᴏᴠɪᴇ ғʀᴏᴍ ɪᴍᴅʙ.ᴄᴏᴍ
═───────◇───────═
"""  
__mod_name__ = "𝙸ᴍᴅʙ"
