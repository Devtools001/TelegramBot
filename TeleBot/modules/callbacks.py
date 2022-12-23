
import time
import random
import psutil
from pyrogram import filters , __version__ as pyro , Client 
from TeleBot import pgram,StartTime,BOT_NAME,get_readable_time,BOT_USERNAME
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from TeleBot.resources.Data import *

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
  #  await query.delete()
    first_name=callback_query.from_user.first_name
    uptime= get_readable_time((time.time() - StartTime))
    await query.reply_photo(photo=random.choice(PM_PHOTOS),caption=PM_START_TEXT.format(first_name,BOT_NAME,uptime),
    reply_markup=InlineKeyboardMarkup(START_BUTTONS))

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
