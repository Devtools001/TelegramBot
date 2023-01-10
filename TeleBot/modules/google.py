import re
import os
from TeleBot import pgram
from pyrogram import filters
from GoogleSearch import Search
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from GoogleSearch import Search
from pyrogram.errors import BadRequest
from geniuses import GeniusClient
from httpx import AsyncClient
from bs4 import BeautifulSoup
from requests import get, post

@pgram.on_message(filters.command(["pp","p","grs","reverse"]))
async def _reverse(_, message):
    if len(message.command) == 2:
        url = message.text.split(None,1)[1]
        if url.startswith(("https://", "http://")):
            msg = await message.reply_text("ᴜᴘʟᴏᴀᴅɪɴɢ ᴜʀʟ ᴛᴏ ɢᴏᴏɢʟᴇ..")
            result = Search(url=url)
            name = result["output"]
            link = result["similar"]
            try:
                await msg.edit_text("ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ɢᴏᴏɢʟᴇ, ғᴇᴛᴄʜɪɴɢ ʀᴇsᴜʟᴛs...")
                await msg.edit_text(
                    text=f"{name}",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="sɪᴍɪʟᴀʀ",
                                    url=link,
                                ),
                            ],
                        ],
                    ),
                )
            except BadRequest as er :
                await message.reply_text(er)     
            return
        else:
            await message.reply_text(
                "ᴄᴏᴍᴍᴀɴᴅ ᴍᴜsᴛ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sʜᴏᴜʟᴅ ɢɪᴠᴇ ᴜʀʟ"
            )   
    replied = message.reply_to_message

    if replied and (replied.photo or replied.sticker)  :
        try:
            edit = await message.reply_text("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɪᴍᴀɢᴇ")
        except BadRequest:
            return
        if replied.photo :
            photo = await pgram.download_media(replied.photo.file_id,file_name = "reverse.jpg")
        else:
            photo = await pgram.download_media(replied.sticker.file_id,file_name = "reverse.jpg")
        await edit.edit_text("ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪᴍᴀɢᴇ, ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ɢᴏᴏɢʟᴇ...")
        result = Search(file_path=photo)
        await edit.edit_text("ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ɢᴏᴏɢʟᴇ, ғᴇᴛᴄʜɪɴɢ ʀᴇsᴜʟᴛs...")
        name = result["output"]
        link = result["similar"]

        await edit.edit_text(
            text=f"{name}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sɪᴍɪʟᴀʀ",
                            url=link,
                        ),
                    ],
                ],
            ),
        )
        return
        os.remove(photo)
    else:
        await message.reply_text(
            "ᴄᴏᴍᴍᴀɴᴅ sʜᴏᴜʟᴅ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ ᴜʀʟ sʜᴏᴜʟᴅ ɢɪᴠᴇɴ."
        )
    

@pgram.on_message(filters.command("lyrics"))
async def _lyrics(_, message):
    if len(message.command) < 2 :
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ sᴏɴɢ ɴᴀᴍᴇ ᴛᴏ ғɪɴᴅ ɪᴛ's ʟʏʀɪᴄs. 💘")
    GENIUSES_API_KEY = (
        "gIgMyTXuwJoY9VCPNwKdb_RUOA_9mCMmRlbrrdODmNvcpslww_2RIbbWOB8YdBW9"
    )  
    q = message.text.split(None,1)[1]
    g_client = GeniusClient(GENIUSES_API_KEY) 
    songs = g_client.search(q)
    if len(songs) == 0:
        return await e.reply(
            "ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ ᴛʜᴇ ɢɪᴠᴇɴ sᴏɴɢ ɴᴀᴍᴇ!",
        )
    song = songs[0]
    name = song.title
    song.header_image_thumbnail_url
    lyrics = song.lyrics
    for x in ["Embed", "Share URL", "Copy"]:
        if x in lyrics:
            lyrics = lyrics.replace(x, "")
    pattern = re.compile("\n+")
    lyrics = pattern.sub("\n", lyrics)
    out_str = f"**{name}**\n__{lyrics}__"
    await message.reply_text(out_str)     



@pgram.on_message(filters.command("ud"))
async def _ud(_, message):
    if len(message.command) < 2 :
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴛᴇxᴛ ᴛᴏᴏ. 🎣")

    text = message.text.split(None,1)[1]
    async with AsyncClient() as client:
        r = await client.get(f"https://api.urbandictionary.com/v0/define?term={text}")
    results = r.json()    
                   
    try:
        reply_text = f'**💘 {text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        link = results["list"][0]["permalink"]
        
    
        await message.reply_text(reply_text,reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(
                            text="• ʟɪɴᴋ •",
                            url=link,
                        ),
                    ],
                ],))
    except Exception:
        await message.reply_text("ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ.")
               
            
@pgram.on_message(filters.command("google"))
async def _google(_, message):
    try:
        query = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply(
            "ᴛʜᴇ ǫᴜᴇʀʏ ᴛᴇxᴛ ʜᴀs ɴᴏᴛ ʙᴇᴇɴ ᴘʀᴏᴠɪᴅᴇᴅ.",
        )   
    url = f"https://www.google.com/search?&q={query}&num=5"
    usr_agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/61.0.3163.100 Safari/537.36"
    }
    r = get(url, headers=usr_agent)
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all("div", attrs={"class": "g"})
    final = f"sᴇᴀʀᴄʜ ʀᴇsᴜʟᴛs for <b>{query}</b>:"
    if not results or len(results) == 0:
        return await e.reply(
            "ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ!",
        )
    for x in results:
        link = (x.find("a", href=True))["href"]
        name = x.find("h3")
        if link and name:
            if not name == "Images" and not name == "Description":
                final += f"\n- <a href='{link}'>{name}</a>"
    await message.reply_text(final, disable_web_page_preview=True)
    
         


__help__ = """
**⸢ᴀ ɢᴏᴏɢʟᴇ ᴍᴏᴅᴜʟᴇ⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /google <ᴛᴇxᴛ>: ᴘᴇʀғᴏʀᴍ ᴀ ɢᴏᴏɢʟᴇ sᴇᴀʀᴄʜ.

๏ /reverse | /pp | /p | /grs: ᴅᴏᴇs ᴀ ʀᴇᴠᴇʀsᴇ ɪᴍᴀɢᴇ sᴇᴀʀᴄʜ ᴏғ ᴛʜᴇ ᴍᴇᴅɪᴀ ᴡʜɪᴄʜ ɪᴛ ᴡᴀs ʀᴇᴘʟɪᴇᴅ ᴛᴏ.

๏ /lyrics : sᴇᴀʀᴄʜ ᴀ sᴏɴɢ ʟʏʀɪᴄs.
═───────◇───────═
"""

        
__mod_name__ = "𝙶ᴏᴏɢʟᴇ"

