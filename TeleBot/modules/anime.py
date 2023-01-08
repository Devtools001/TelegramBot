import random 
import time
import os
import asyncio
import requests 
from TeleBot import pgram,BOT_NAME
from pyrogram import filters,
from types import NoneType
from pyrogram import filters, Client
from pyrogram.types import Message 
from pyrogram.errors import UserNotParticipant, WebpageCurlFailed, WebpageMediaEmpty
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message
)

from TeleBot import (
    ANILIST_CLIENT,
    ANILIST_REDIRECT_URL,
    ANILIST_SECRET,    
)



@pgram.on_message(filters.command("anime"))
async def _anime(client: Client, message: Message, mdata: dict):
    text = mdata['text'].split(" ", 1)
    gid = mdata['chat']['id']
    try:
        user = mdata['from_user']['id']
        auser = mdata['from_user']['id']
    except KeyError:
        user = mdata['sender_chat']['id']
        ufc = await gcc(user)
        if ufc is not None:
            auser = ufc
        else:
            auser = user
    find_gc = await DC.find_one({'_id': gid})
    if find_gc is not None and 'anime' in find_gc['cmd_list'].split():
        return
    if len(text) == 1:
        k = await message.reply_text(
"""Please give a query to search about
example: /anime Ao Haru Ride"""
        )
        await asyncio.sleep(5)
        return await k.delete()
    query = text[1]
    auth = False
    vars_ = {"search": query}
    if query.isdigit():
        vars_ = {"id": int(query)}
    if (await AUTH_USERS.find_one({"id": auser})):
        auth = True
    result = await get_anime(
        vars_,
        user=auser,
        auth=auth,
        cid=gid if gid != user else None
    )
    if len(result) != 1:
        title_img, finals_ = result[0], result[1]
    else:
        k = await message.reply_text(result[0])
        await asyncio.sleep(5)
        return await k.delete()
    buttons = get_btns("ANIME", result=result, user=user, auth=auth)
    if await (
        SFW_GRPS.find_one({"id": gid})
    ) and result[2].pop() == "True":
        await client.send_photo(
            gid,
            no_pic[random.randint(0, 4)],
            caption="This anime is marked 18+ and not allowed in this group"
        )
        return
    try:
        await client.send_photo(
            gid, title_img, caption=finals_, reply_markup=buttons
        )
    except (WebpageMediaEmpty, WebpageCurlFailed):
        await clog('ANIBOT', title_img, 'LINK', msg=message)
        await client.send_photo(
            gid, failed_pic, caption=finals_, reply_markup=buttons
        )
    if title_img not in PIC_LS:
        PIC_LS.append(title_img)
