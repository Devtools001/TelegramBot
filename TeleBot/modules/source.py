from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 

from TeleBot import pgram 


STEVE = "https://graph.org/file/30d016d2a54094e4e860c.jpg"


@pgram.on_message(filters.command(["repo", "source"]))
async def repo(_, message):
    await message.reply_photo(
        photo=STEVE,
        caption=f"""✨ **ʜᴇʏ {message.from_user.mention},**
**ʀᴇᴘᴏ ᴏᴡɴᴇʀ  : [sᴛᴇᴠᴇ](https://t.me/STEVE_R0GERS_101)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
**ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ :** `1.0`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    
                    InlineKeyboardButton(
                        "• ɢɪᴛʜᴜʙ •", callback_data="gihub"
                    ),
                ]
            ]
        ),
    )

@pgram.on_callback_query(filters.regex("github"))
async def _git(client, callback_query : CallbackQuery):
    await client.answer_web_app_query(
    callback_query.id,
    "https://github.com/NotStark")

__help__ = """
**⸢ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /repo | /source : sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏғ ᴍʏ ʀᴇᴘᴏ.
═───────◇───────═
"""
__mod_name__ = "𝚂ᴏᴜʀᴄᴇ"
    
