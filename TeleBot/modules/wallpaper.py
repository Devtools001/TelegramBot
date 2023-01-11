import requests
from .. import pgram
from random import randint
from pyrogram import filters,enums
from TeleBot.modules.pyrogram_funcs.chat_actions import send_action



@pgram.on_message(filters.command("wall"))
@send_action(enums.ChatAction.UPLOAD_PHOTO)
async def wall(_,msg):
    if len(msg.command) < 2:
         await msg.reply_text("ʜᴇʏ ɴᴏᴏʙ ɢɪᴠᴇ sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ sᴇᴀʀᴄʜ.")
         return 
    
    query= msg.text.split(None,1)[1].replace(" ","%20")
                    
    url=f"https://api.safone.me/wall?query={query}"
    re=requests.get(url).json()
    walls = re.get("results")
    if not walls:
        await msg.reply_text("ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ! ")
        return 
    wall_index = randint(0, len(walls) -1)
    wallpaper = walls[wall_index]
    pic = wallpaper.get("imageUrl")
    preview=wallpaper.get("thumbUrl") 
    title = wallpaper.get("title")
    try: 
        #await pgram.send_chat_action(msg.chat.id, enums.ChatAction.UPLOAD_PHOTO)        
        await msg.reply_photo(preview, caption="⚡ ᴘʀɪᴠɪᴇᴡ")
        await msg.reply_document(pic, caption=f"⚡ ᴛɪᴛʟᴇ - {title}")
    except Exception as error :
        await msg.reply_text(f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ.\n {error}")  

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

    except Exception as a:
        await message.reply_text(a)
    
    
          
    
__help__ = """
「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /wall «ǫᴜᴇʀʏ» : ɢᴇᴛ ᴡᴀʟʟᴘᴀᴘᴇʀs ғʀᴏᴍ ᴀʟᴘʜᴀᴄᴏᴅᴇʀs.
๏ /wallpaper sᴇɴᴅ ʀᴀɴᴅᴏᴍ ᴡᴀʟʟᴘᴀᴘᴇʀs.
═───────◇───────═
"""
__mod_name__ = "𝚆ᴀʟʟᴘᴀᴘᴇʀ"
