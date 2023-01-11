import io
import aiohttp
from TeleBot import pgram
from pyrogram import filters




@pgram.on_message(filters.command("weather"))
async def _weather(_, message):
    if message.sender_chat :
        return
    if len(message.command) < 2 :
        return await message.reply_text("ɢɪᴠᴇ ᴀ ᴘʟᴀᴄᴇ ɴᴀᴍᴇ ᴛᴏᴏ.")
    url = "https://wttr.in/{}.png"  
    place = message.text.split(None,1)[1]   
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(url.format(place))
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await message.reply_photo(out_file)
    
__help__ = """
**⸢ᴋɴᴏᴡ ᴡᴇᴀᴛʜᴇʀ 🌡️⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /weather «ᴘʟᴀᴄᴇ ɴᴀᴍᴇ» :  ᴋɴᴏᴡ ᴡᴇᴀᴛʜᴇʀ ᴏғ ᴀ ɢɪᴠᴇɴ ᴘʟᴀᴄᴇ.
═───────◇───────═
"""
__mod_name__ = "𝚆ᴇᴀᴛʜᴇʀ"
