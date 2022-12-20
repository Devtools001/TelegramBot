import requests
from .. import pgram
from random import randint
from pyrogram import filters,enums
from functools import wraps

def typing_action(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    async def command_func(_,msg):
        await pgram.send_chat_action(msg.chat.id, enums.ChatAction.UPLOAD_PHOTO)
        return await func(_,msg)

    return command_func

def send_action(action):   
    def decorator(func):
        @wraps(func)
        async def command_func(_,msg, *args, **kwargs):
            await pgram.send_chat_action(
                chat_id=msg.chat.id, action=action
            )
            return await func(_,msg, *args, **kwargs)

        return command_func

    return decorator

@pgram.on_message(filters.command("wall"))
@send_action(enums.ChatAction.TYPING)
async def wall(_,msg):
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
    
__help__ = """
「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /wall «ǫᴜᴇʀʏ» : ɢᴇᴛ ᴡᴀʟʟᴘᴀᴘᴇʀs ғʀᴏᴍ ᴀʟᴘʜᴀᴄᴏᴅᴇʀs.
═───────◇───────═
"""
__mod_name__ = "𝚆ᴀʟʟᴘᴀᴘᴇʀ"
