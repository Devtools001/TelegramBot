import speedtest 
from TeleBot import pgram,DEV_USERS

from pyrogram import filters, Client ,enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 


buttons = [
        [
            InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="speedtest_image"),
            InlineKeyboardButton("ᴛᴇxᴛ", callback_data="speedtest_text"),
        ]
    ]


async def convert(speed):
    return round(int(speed) / 1048576, 2)

@pgram.on_message(filters.command("speedtest") & filters.user(DEV_USERS))
async def _speed(_, message):
    await message.reply_text("sᴩᴇᴇᴅᴛᴇsᴛ ᴍᴏᴅᴇ", reply_markup=InlineKeyboardMarkup(buttons))
    

@pgram.on_callback_query(filters.user(DEV_USERS))
async def _speedtest(app : Client,callback_query: CallbackQuery): 
    #if callback_query.message.from_user.id in DEV_USERS :   
    text = await callback_query.message.edit("ʀᴜɴɴɪɴɢ ᴀ sᴩᴇᴇᴅᴛᴇsᴛ...")
    speed = speedtest.Speedtest()
    speed.get_best_server()
    speed.download()
    speed.upload()
    msg = "sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛ"
    query = callback_query.data.lower()
    if query == "speedtest_image":
        speedtest_image = speed.results.share()
        await callback_query.message.reply_photo(
                photo=speedtest_image, caption=msg
            )
        await text.delete()

    if query == "speedtest_text":
        result = speed.results.dict()
        msg += f"\n**⦾ ᴘɪɴɢ »** `{result['ping']}`\n**⦾ ᴜᴘʟᴏᴀᴅ »** `{await convert(result['upload'])}Mb/s`\n**⦾ ᴅᴏᴡɴʟᴏᴀᴅ »** `{await convert(result['download'])}Mb/s"
        await text.edit(msg, parse_mode=enums.ParseMode.MARKDOWN)
 
__help__ = """
**⸢ᴄʜᴇᴄᴋ ᴍʏ sᴘᴇᴇᴅ⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /speedtest : ʀᴜɴs ᴀ sᴘᴇᴇᴅᴛᴇsᴛ ᴀɴᴅ ᴄʜᴇᴄᴋ ᴛʜᴇ sᴇʀᴠᴇʀ sᴘᴇᴇᴅ.
═───────◇───────═
"""   
__mod_name__ = "𝚂ᴘᴇᴇᴅᴛᴇsᴛ"
