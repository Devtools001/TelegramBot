import time
import psutil
from pyrogram import filters , __version__ as pyro , Client 
from TeleBot import pgram,StartTime,BOT_NAME,get_readable_time,BOT_USERNAME
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 


PM_START_TEXT = """
🥀 ʜᴇʏ **{}** ,
        
ᴛʜɪs ɪs **{}**
➖➖➖➖➖➖➖➖➖➖➖➖➖

๏ ɪ'ᴍ ᴜɴᴅᴇʀ ᴄʀᴇᴀᴛɪᴏɴ ʙʏ ⸢[𝚂𝚃𝙰𝚁𝙺](https://t.me/NoobStark_21)⸥
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅsn.

๏ **ᴅɪᴅɴ'ᴛ sʟᴇᴇᴘᴛ sɪɴᴄᴇ** {}

"""

BUTTON = [
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

STATS_MSG="""
ʜɪɪ {},

๏ ʜᴇʀᴇ ɪs ᴍʏ sᴛᴀᴛs:
» ᴜᴘᴛɪᴍᴇ : {}
» ʀᴀᴍ : {}
» ᴅɪsᴋ : {}
» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {}
"""

@pgram.on_callback_query(filters.regex("friday_back"))
async def Friday(_, callback_query : CallbackQuery):
    query= callback_query.message
    await query.message.delete()
    first_name=callback_query.from_user.first_name
    uptime= get_readable_time((time.time() - StartTime))
    await query.reply_text(PM_START_TEXT.format(first_name,BOT_NAME,uptime),
    reply_markup=InlineKeyboardMarkup(BUTTON))

@pgram.on_callback_query(filters.regex("Friday_stats"))
async def Friday(client, callback_query : CallbackQuery):    
    first_name=callback_query.from_user.first_name
    uptime= get_readable_time((time.time() - StartTime))   
    rem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    await client.answer_callback_query(
    callback_query.id,
    text=STATS_MSG.format(first_name, uptime,rem,disk,pyro),
    show_alert=True
)


@pgram.on_callback_query()
async def callback(client : Client, query: CallbackQuery): 
    if query.data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
