import time
from TeleBot import pgram,StartTime,BOT_NAME,get_readable_time
from pyrogram.types import CallbackQuery 


PM_START_TEXT = """
🥀 ʜᴇʏ *{}* ,
        
ᴛʜɪs ɪs *{}*
➖➖➖➖➖➖➖➖➖➖➖➖➖
๏ ɪ'ᴍ ᴜɴᴅᴇʀ ᴄʀᴇᴀᴛɪᴏɴ ʙʏ ⸢[𝚂𝚃𝙰𝚁𝙺](https://t.me/NoobStark_21)⸥
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅsn.
๏ *ᴅɪᴅɴ'ᴛ sʟᴇᴇᴘᴛ sɪɴᴄᴇ* {}
"""
@pgram.on_callback_query(filters.regex("friday_back"))
async def Friday(_, callback_query : CallbackQuery):
    query= callback_query.message
    first_name=callback_query.from_user.first_name
    uptime= get_readable_time(time.time() - StartTime))
    await query.edit_caption(PM_START_TEXT.format(first_name,BOT_NAME,uptime))
