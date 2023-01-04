import requests
from TeleBot import pgram
from pyrogram import filters

@pgram.on_message(filters.command(["truth","htruth"]))
async def true(_, message):
    if message.command[0] == "truth":
        url = "https://api.truthordarebot.xyz/v1/dare"
        truth = requests.get(url).json()["question"]
        await message.reply_text(f"`{truth}`")
        return 
    if message.command[0] == "htruth":
        url = "https://api.truthordarebot.xyz/v1/dare"
        truth = requests.get(url).json()["translations"]["hi"]
        await message.reply_text(f"`{truth}`")
        return     
