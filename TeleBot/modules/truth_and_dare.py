import requests
from TeleBot import pgram
from pyrogram import filters

@pgram.on_message(filters.command("truth"))
async def true(_, message):
    print(message.command[1])
   # if message.command
    
    url = "https://api.truthordarebot.xyz/v1/dare"
    truth = requests.get(url).json()["question"]
    await message.reply_text(f"`{truth}`")
