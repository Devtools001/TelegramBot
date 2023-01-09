from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
                        "•ᴍᴜꜱɪᴄ•", url="https://github.com/Abishnoi69/AsuXMusic"
                    ),
                    InlineKeyboardButton(
                        "•ʀᴏʙᴏᴛ•", url="https://github.com/Abishnoi69/ExonRobot"
                    ),
                ]
            ]
        ),
    )
