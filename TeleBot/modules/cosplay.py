
import requests
from TeleBot import pgram,BOT_USERNAME
from pyrogram import filters 
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BUTTONS = [
    [
        InlineKeyboardButton(
            text="✨ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘʀɪᴠᴀᴛᴇ ✨",
            url=f"https://t.me/{BOT_USERNAME}?start=true",
        ),
    ],    
]

@pgram.on_message(filters.command("cosplay"))
async def _cosplay(_, message):
    pic = requests.get("https://waifu-api.vercel.app").json() 
    await message.reply_photo(pic)
         
  
@pgram.on_message(filters.command("lewd"))
async def _lewd(_, message):
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text("**ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ ᴘʀɪᴠᴀᴛᴇ**", reply_markup=InlineKeyboardMarkup(BUTTONS)) 
        return   
    pic = requests.get("https://waifu-api.vercel.app/items/1").json()
    await message.reply_photo(pic)

__help__ = """
**⸢ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀɴɪᴍᴇ ᴄᴏsᴘʟᴀʏ sғᴡ/ɴsғᴡ⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /cosplay : ɢᴇᴛ ʀᴀɴᴅᴏᴍ sғᴡ ᴀɴɪᴍᴇ ᴄᴏsᴘʟᴀʏ
๏ /lewd : ɢᴇᴛ ɴsғᴡ ᴀɴɪᴍᴇ ᴄᴏsᴘʟᴀʏ.  
═───────◇───────═"""

__mod_name__ = "𝙲ᴏsᴘʟᴀʏ"
