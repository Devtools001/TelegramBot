import requests
from TeleBot import pgram
from pyrogram import filters

@pgram.on_message(filters.command(["truth","htruth"]))
async def true(_, message):
    if message.command[0] == "truth":
        url = "https://api.truthordarebot.xyz/v1/truth"
        truth = requests.get(url).json()["question"]
        await message.reply_text(f"`{truth}`")
        return 
    if message.command[0] == "htruth":
        url = "https://api.truthordarebot.xyz/v1/truth"
        truth = requests.get(url).json()["translations"]["hi"]
        await message.reply_text(f"`{truth}`")
        return     

@pgram.on_message(filters.command(["dare","hdare"]))
async def _dare(_, message):
    if message.command[0] == "dare":
        url = "https://api.truthordarebot.xyz/v1/dare"
        dare = requests.get(url).json()["question"]
        await message.reply_text(f"`{dare}`")
        return 
    if message.command[0] == "hdare":
        url = "https://api.truthordarebot.xyz/v1/dare"
        dare = requests.get(url).json()["translations"]["hi"]
        await message.reply_text(f"`{dare}`")
        return 

__mod_name__ = "𝚃ʀᴜᴛʜ ᴅᴀʀᴇ"
__help__ = """
**⸢ᴘʟᴀʏ ᴡɪᴛʜ ʏᴏᴜʀ ғʀɪᴇɴᴅs⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /truth: : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.

๏ /htruth :  sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ ɪɴ ʜɪɴᴅɪ.

๏ /dare : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.

๏ /hdare : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ ɪɴ ʜɪɴᴅɪ.
═───────◇───────═
"""
