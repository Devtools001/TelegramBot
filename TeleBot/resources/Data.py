from pyrogram.types import InlineKeyboardButton
from TeleBot import BOT_NAME,BOT_USERNAME
    
START_IMG="https://telegra.ph/file/5381961c760ed435d0fc7.jpg"

PM_PHOTOS = (
"https://telegra.ph/file/9658f5c0f7d448ad4e0bd.jpg",
"https://telegra.ph/file/4a94521e20c40195c9a9a.jpg",
"https://telegra.ph/file/61c9b7921458f31260b0c.jpg",
"https://telegra.ph/file/9e01586796e950cc8ddc6.jpg",
"https://telegra.ph/file/0e068d1357c5a79c191e3.jpg",
"https://telegra.ph/file/13b5bc8b84ee2ac687e3d.jpg",
"https://telegra.ph/file/7517a65cab490e36d681c.jpg"
         )

PM_START_TEXT = """
🥀 ʜᴇʏ **{}** ,
        
ᴛʜɪs ɪs **{}**
➖➖➖➖➖➖➖➖➖➖➖➖➖
๏ ɪ'ᴍ ᴜɴᴅᴇʀ ᴄʀᴇᴀᴛɪᴏɴ ʙʏ ⸢[𝚂𝚃𝙰𝚁𝙺](https://t.me/NoobStark_21)⸥
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅsn.
๏ **ᴅɪᴅɴ'ᴛ sʟᴇᴇᴘᴛ sɪɴᴄᴇ** {}
"""

START_BUTTONS = [
    [
        InlineKeyboardButton(
            text="✨ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],    
    [
        InlineKeyboardButton(text="⚡ ʜᴇʟᴘ ⚡", callback_data="help_back"),
        InlineKeyboardButton(text="♻️ sᴛᴀᴛs ♻️", callback_data="Friday_stats")
    ],    
]

