from TeleBot import pgram
import json
import requests
from PyDictionary import PyDictionary
from pyrogram import filters 

dictionary = PyDictionary()

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
    await message.reply_text(f"`{got}`")


