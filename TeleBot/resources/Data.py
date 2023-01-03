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

HELP_IMG=(
"https://telegra.ph/file/74f547d4dd635432ea1b0.jpg",
"https://telegra.ph/file/b846cc2a4326a9dab5a2d.jpg",
"https://telegra.ph/file/1c58b1a72044ba6b6e644.jpg"
   )

PM_START_TEXT = """
🥀 ʜᴇʏ **{}** ,
        
ᴛʜɪs ɪs **{}**
➖➖➖➖➖➖➖➖➖➖➖➖➖
๏ ɪ'ᴍ ᴜɴᴅᴇʀ ᴄʀᴇᴀᴛɪᴏɴ ʙʏ ⸢[sᴛᴇᴠᴇ](https://t.me/STEVE_R0GERS_101)⸥
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅsn.
๏ **ᴅɪᴅɴ'ᴛ sʟᴇᴇᴘᴛ sɪɴᴄᴇ** {}
"""

HELP_STRINGS = """
ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs.
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


LOG_MSG = "●▬▬▬▬▬▬▬▬▬▬▬▬๑۩ ғʀɪᴅᴀʏ ʀᴏʙᴏᴛ ۩๑▬▬▬▬▬▬▬▬▬▬▬●\n"
LOG_MSG += "ғʀɪᴅᴀʏ sᴛᴀʀᴛɪɴɢ ...... \n\n"
LOG_MSG += "⊙ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴘʏʀᴏɢʀᴀᴍ ʙᴀsᴇᴅ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ + ᴍᴜsɪᴄ ʙᴏᴛ\n\n"
LOG_MSG += "⊙ ᴘʀᴏɪᴇᴄᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ʜᴛᴛᴘs://ɢɪᴛʜᴜʙ.ᴄᴏᴍ/NᴏᴛSᴛᴀʀᴋ\n\n"
LOG_MSG += "⊙ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ:\n"
LOG_MSG+= "  @sᴛᴇᴠᴇ_ʀᴏɢᴇʀs_𝟷𝟶𝟷\n"
LOG_MSG += "●▬▬▬▬▬▬▬▬▬▬▬▬๑۩ ғʀɪᴅᴀʏ ʀᴏʙᴏᴛ ۩๑▬▬▬▬▬▬▬▬▬▬▬●"

SUPPORT_SEND_MSG = """
🥀 {} ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ...
┏•❅────✧❅✦❅✧────❅•┓
  **★ ʙᴏᴛ ᴠᴇʀsɪᴏɴ :** `1.0`
  **★ ᴩʏʀᴏɢʀᴀᴍ :** `{}`
┗•❅────✧❅✦❅✧────❅•┛
"""
