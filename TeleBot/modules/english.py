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
    await message.reply_text(got)
