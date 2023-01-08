from TeleBot import pgram
import json
import requests
from PyDictionary import PyDictionary
from pyrogram import filters 

dictionary = PyDictionary()

API_KEY = "6ae0c3a0-afdc-4532-a810-82ded0054236"
URL = "http://services.gingersoftware.com/Ginger/correct/json/GingerTheText"

@pgram.on_message(filters.command("define"))
async def _define(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ɢɪᴠᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ᴅᴇғɪɴᴇ ɪᴛ.")
    text = message.text.split(None,1)[1]
    let = dictionary.meaning(text)
    set = str(let)
    jet = set.replace("{", "")
    net = jet.replace("}", "")
    got = net.replace("'", "")
    await message.reply_text(f"`{got}`")

@pgram.on_message(filters.command("antonyms"))
async def _atony(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴜsᴀɢᴇ : /ᴀɴᴛᴏɴʏᴍs <ᴡᴏʀᴅ>: ғɪɴᴅ ᴛʜᴇ ᴀɴᴛᴏɴʏᴍs ᴏғ ᴀ ᴡᴏʀᴅ")
    text = message.text.split(None,1)[1]  
    let = dictionary.antonym(text)
    set = str(let)
    jet = set.replace("{", "")
    net = jet.replace("}", "")
    got = net.replace("'", "")
    await message.reply_text(f"`{got}`") 


@pgram.on_message(filters.command("synonyms"))
async def _atony(_, message):
    if len(message.command) < 2:
        return await message.reply_text("ᴜsᴀɢᴇ :  /sʏɴᴏɴʏᴍs <ᴡᴏʀᴅ>: ғɪɴᴅ ᴛʜᴇ sʏɴᴏɴʏᴍs ᴏғ ᴀ ᴡᴏʀᴅ")
    text = message.text.split(None,1)[1]  
    let = dictionary.synonym(text)
    set = str(let)
    jet = set.replace("{", "")
    net = jet.replace("}", "")
    got = net.replace("'", "")
    await event.reply_text(f"`{got}`")


@pgram.on_message(filters.command("spell"))
async def _spell(_, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ʙᴀʙʏ.")
    if not replied.text:
        return await message.reply_text("ʙʀᴜʜ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ..")
    ctext = replied
    msg = ctext.text
    print(msg)
    params = dict(lang="US", clientVersion="2.0", apiKey=API_KEY, text=msg)

    res = requests.get(URL, params=params)
    changes = json.loads(res.text).get("LightGingerTheTextResult")
    curr_string = ""
    prev_end = 0

    for change in changes:
        start = change.get("From")
        end = change.get("To") + 1
        suggestions = change.get("Suggestions")
        if suggestions:
            sugg_str = suggestions[0].get("Text")
            curr_string += msg[prev_end:start] + sugg_str
            prev_end = end

    curr_string += msg[prev_end:]
    await message.reply_text(curr_string)



     
