import bs4
import html
import jikanpy
import datetime
import textwrap
import requests
import json
from pyrogram import filters 
from TeleBot import pgram 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 
from pyrogram.enums import ParseMode 


info_btn = "More Info 📕"
prequel_btn = "⬅️ Prequel"
sequel_btn = "Sequel ➡️"
close_btn = "Close ❌"

url = 'https://graphql.anilist.co'

async def shorten(description, info='anilist.co'):
    msg = ""
    if len(description) > 700:
        description = description[0:500] + '....'
        msg += f"\n**🗒 ᴅᴇsᴄʀɪᴘᴛɪᴏɴ »** `_{description}_`[ʀᴇᴀᴅ ᴍᴏʀᴇ]({info})"
    else:
        msg += f"\n**🗒 ᴅᴇsᴄʀɪᴘᴛɪᴏɴ »**`_{description}_`"
    return msg

async def t(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " Days, ") if days else "") + \
        ((str(hours) + " Hours, ") if hours else "") + \
        ((str(minutes) + " Minutes, ") if minutes else "") + \
        ((str(seconds) + " Seconds, ") if seconds else "") + \
        ((str(milliseconds) + " ms, ") if milliseconds else "")
    return tmp[:-2]




@pgram.on_message(filters.command("anime"))
async def _anime(_, message):
    if len(message.command) < 2 :
        await message.reply_text('ғᴏʀᴍᴀᴛ : /ᴀɴɪᴍᴇ < ᴀɴɪᴍᴇ ɴᴀᴍᴇ >')
        return     
    else:
        search = message.text.split(None,1)
        search = search[1]
    variables = {'search': search}
    json = requests.post(
        url, json={
            'query': anime_query,
            'variables': variables
        }).json()
    print(json)
    print()
    if 'errors' in json.keys():
        await message.reply_text('🙄 ᴀɴɪᴍᴇ ɴᴏᴛ ғᴏᴜɴᴅ')
        return
    
    if json:        
        json = json['data']['Media']
        print(json['startDate']['year'])
        msg = f"**📀 ᴛɪᴛʟᴇ » {json['title']['romaji']}** ┌⁠(⁠・⁠。⁠・⁠)⁠┘⁠♪ **({json['title']['native']})**\n\n**🎣 ᴛʏᴘᴇ »** {json['format']}\n**⚡sᴛᴀᴛᴜs »** {json['status']}\n**✨ ᴇᴘɪsᴏᴅᴇs »** {json.get('episodes', 'N/A')}\n**⏲️ ᴅᴜʀᴀᴛɪᴏɴ »** {json.get('duration', 'N/A')} ᴘᴇʀ ᴇᴘ.\n**🌟 sᴄᴏʀᴇ »**: {json['averageScore']}\n**🎭 ɢᴇɴʀᴇs »**: `"
        for x in json['genres']:
            msg += f"{x}, "
        msg = msg[:-2] + '`\n'
        msg += "**💘 sᴛᴜᴅɪᴏs »**: `"
        for x in json['studios']['nodes']:
            msg += f"{x['name']}, "
        msg = msg[:-2] + '`\n'
        anime_name_w = f"{json['title']['romaji']}"
        info = json.get('siteUrl')
        trailer = json.get('trailer', None)
        anime_id = json['id']
        if trailer:
            trailer_id = trailer.get('id', None)
            site = trailer.get('site', None)
            if site == "youtube":
                trailer = 'https://youtu.be/' + trailer_id
        description = json.get('description', 'N/A').replace('<b>', '').replace(
            '</b>', '').replace('<br>', '')
        msg += await shorten(description, info)
        image = info.replace('anilist.co/anime/', 'img.anili.st/media/')

    if trailer:
        buttons = [[
                InlineKeyboardButton("More Info ➕", url=info),
                InlineKeyboardButton("Trailer 🎬", url=trailer)
            ]]
        buttons += [[InlineKeyboardButton("➕ Add To Watchlist ➕", callback_data=f"xanime_watchlist={anime_name_w}")]]
    else:
        buttons = [[InlineKeyboardButton("More Info", url=info)]]
        buttons += [[InlineKeyboardButton("➕ Add To Watchlist", callback_data=f"xanime_watchlist={anime_name_w}")]]
   
         
    if image:
            try:
                await message.reply_photo(
                    photo=image,
                    caption=msg,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup(buttons))
            except:
                msg += f" [〽️]({image})"
                await message.reply_text(
                    msg,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await message.reply_text(
           msg,
           parse_mode=ParseMode.MARKDOWN,
           reply_markup=InlineKeyboardMarkup(buttons))



