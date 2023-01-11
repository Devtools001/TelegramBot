import requests 
from TeleBot import pgram
from pyrogram import filters

@pgram.on_message(filters.command('schedule'))
def schedule(_, message):
    results = requests.get('https://subsplease.org/api/?f=schedule&h=true&tz=Japan').json()
    text = None
    for result in results['schedule']:
        title = result['title']
        time = result['time']
        aired = bool(result['aired'])
        title = f"**[{title}](https://subsplease.org/shows/{result['page']})**" if not aired else f"**~~[{title}](https://subsplease.org/shows/{result['page']})~~**"
        data = f"{title} - **{time}**"
        
        if text:
            text = f"{text}\n{data}"
        else:
            text = data

    await message.reply_text(f"**Today's Schedule:**\nTime-Zone: Tokyo (GMT +9)\n\n{text}")
