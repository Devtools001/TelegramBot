import requests 
from TeleBot import pgram
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message ,CallbackQuery
from datetime import datetime 

async def get_scheduled(x: int = 9):
    base_url = "https://api.jikan.moe/v4/schedules/"
    day = str(day_(x if x!=9 else datetime.now().weekday())).lower()
    out = f"Scheduled animes for {day.capitalize()}\n\n"
    data = requests.get(base_url+day).json()
    sched_ls =  data["data"]
    for i in sched_ls:
        try:
            title = i['titles'][0]['title']
        except IndexError:
            title = i['title']
        out += f"• `{title}`\n"
    return out, x if x!=9 else datetime.now().weekday()

@pgram.on_message(filters.command("schedule"))
async def _schedule(app : Client, message : Message,data : dict):
    gid = data['chat']['id']     
    x = await client.send_message(
        gid, "<code>Fetching Scheduled Animes</code>"
    )
    try:
        user = data['from_user']['id']
    except KeyError:
        user = data['sender_chat']['id']
    msg = await get_scheduled()
    buttons = get_btns("SCHEDULED", result=[msg[1]], user=user)
    await x.edit_text(msg[0], reply_markup=buttons)


@pgram.on_callback_query(filters.regex(pattern=r"sched_(.*)"))
async def ns_(client: Client, cq: CallbackQuery, cdata: dict):
    kek, day, user = cdata['data'].split("_")
    msg = await get_scheduled(int(day))
    buttons = get_btns("SCHEDULED", result=[int(day)], user=user)
    await cq.edit_message_text(msg[0], reply_markup=buttons)


