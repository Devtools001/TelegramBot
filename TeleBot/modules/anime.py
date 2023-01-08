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



manga_query = """
query ($id: Int,$search: String) {
      Media (id: $id, type: MANGA,search: $search) {
        id
        title {
          romaji
          english
          native
        }
        description (asHtml: false)
        startDate{
            year
          }
          type
          format
          status
          siteUrl
          averageScore
          genres
          bannerImage
      }
    }
"""

character_query = """
    query ($query: String) {
        Character (search: $query) {
               id
               name {
                     first
                     last
                     full
               }
               siteUrl
               image {
                        large
               }
               description
        }
    }
"""


anime_query = '''
   query ($id: Int,$search: String) {
      Media (id: $id, type: ANIME,search: $search) {
        id
        title {
          romaji
          english
          native
        }
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          season
          type
          format
          status
          duration
          siteUrl
          studios{
              nodes{
                   name
              }
          }
          trailer{
               id
               site
               thumbnail
          }
          averageScore
          genres
          bannerImage
      }
    }
'''

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
    if 'errors' in json.keys():
        await message.reply_text('🙄 ᴀɴɪᴍᴇ ɴᴏᴛ ғᴏᴜɴᴅ')
        return
    
    if json:        
        json = json['data']['Media']
        print(json['startDate']['year'])
        msg = f"""
**📀 ᴛɪᴛʟᴇ » {json['title']['romaji']}** ┌⁠(⁠・⁠。⁠・⁠)⁠┘⁠♪ **({json['title']['native']})**

**🎣 ᴛʏᴘᴇ »** {json['format']}
**⚡sᴛᴀᴛᴜs »** {json['status']}
**✨ ᴇᴘɪsᴏᴅᴇs »** {json.get('episodes', 'N/A')}

**⏲️ ᴅᴜʀᴀᴛɪᴏɴ »** {json.get('duration', 'N/A')} ᴘᴇʀ ᴇᴘ.
**📆 ʀᴇʟᴇᴀsᴇ ʏᴇᴀʀ »** {json['startDate']['year']}
**🌟 sᴄᴏʀᴇ »**: {json['averageScore']}

**🎭 ɢᴇɴʀᴇs »**: `"""
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
                InlineKeyboardButton("• ᴛʀᴀɪʟᴇʀ •", url=trailer),                
            ]]
        buttons += [[InlineKeyboardButton("• ᴍᴏʀᴇ ɪɴғᴏ •", url=info)]]
    else:
        buttons = [[InlineKeyboardButton("• ᴍᴏʀᴇ ɪɴғᴏ •", url=info)]]
        
         
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

@pgram.on_message(filters.command("manga"))
async def _manga(_, message):
    if len(message.command) < 2 :
        await message.reply_text('ғᴏʀᴍᴀᴛ : /ᴍᴀɴɢᴀ < ᴍᴀɴɢᴀ ɴᴀᴍᴇ >')
        return  
    search = message.text.split(None,1)
    search = search[1]
    variables = {'search': search}
    json = requests.post(
        url, json={
            'query': manga_query,
            'variables': variables
        }).json()
    msg = ''      
    if 'errors' in json.keys():
        await message.reply_text('ᴍᴀɴɢᴀ ɴᴏᴛ ғᴏᴜɴᴅ')
        return
    if json:
        json = json['data']['Media']
        title, title_native = json['title'].get('romaji',
                                                False), json['title'].get(
                                                    'native', False)
        start_date, status, score = json['startDate'].get(
            'year', False), json.get('status',
                                     False), json.get('averageScore', False) 
        if title:
            msg += f"**⦾ ᴛɪᴛʟᴇ »** {title}"
            if title_native:
                msg += f"(`{title_native}`)"
        if start_date:
            msg += f"\n\n**⦾ sᴛᴀʀᴛ ʏᴇᴀʀ »** `{start_date}`"
        if status:
            msg += f"\n**⦾ sᴛᴀᴛᴜs »** `{status}`"
        if score:
            msg += f"\n**⦾ sᴄᴏʀᴇ »** `{score}`"
        msg += '\n**⦾ ɢᴇɴʀᴇs »** '
        for x in json.get('genres', []):
            msg += f"{x}, "
        msg = msg[:-2]
        info = json['siteUrl']       
        buttons = [[InlineKeyboardButton("• ᴍᴏʀᴇ ɪɴғᴏ •", url=info)]]        
        image = json.get("bannerImage", False)
        msg += f"**\n\n⦾ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ »** _{json.get('description', None)}_"
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

@pgram.on_message(filters.command("character"))
async def _character(_, message):
    if len(message.command) < 2 :
        await message.reply_text('ғᴏʀᴍᴀᴛ : /ᴄʜᴀʀᴀᴄᴛᴇʀ < ᴄʜᴀʀᴀᴄᴛᴇʀ ɴᴀᴍᴇ >')
        return   
    search = message.text.split(None,1)  
    search = search[1]
    variables = {'query': search}
    json = requests.post(
        url, json={
            'query': character_query,
            'variables': variables
        }).json()   
    if 'errors' in json.keys():
        await message.reply_text('Character not found')
        return
    if json:
        json = json['data']['Character']
        msg = f"**⦾ ᴄʜᴀʀᴀᴄᴛᴇʀ :** {json.get('name').get('full')}*(`{json.get('name').get('native')}`) \n"
        description = f"{json['description']}"
        site_url = json.get('siteUrl')
        char_name = f"{json.get('name').get('full')}"
        msg += await shorten(description, site_url)
        image = json.get('image', None)
        if image:
            image = image.get('large')
            await message.reply_photo(
                photo=image,
                caption=msg.replace('<b>', '</b>'),               
                parse_mode=ParseMode.MARKDOWN)
        else:
            await message.reply_text(
                msg.replace('<b>', '</b>'), reply_markup=InlineKeyboardMarkup(buttons), parse_mode=ParseMode.MARKDOWN)        
