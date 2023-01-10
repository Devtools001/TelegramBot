import os
from TeleBot import pgram, DRAGONS,BOT_ID,DEV_USERS
from pyrogram import filters ,enums
from typing import Optional
import json
from TeleBot.modules.pyrogram_funcs.extracting_id import extract_user_id

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "TeleBot/elevated_users.json")


async def chech_user_id(user_id : int) -> Optional[str]:
    if not user_id:
        reply = "That...is a chat! baka ka omae?"

    elif user_id == BOT_ID:
        reply = "This does not work that way."

    else:
        reply = None
    return 

@pgram.on_message(filters.command("addsudo"))
async def _addsudo(_, message):
    user_id = await extract_user_id(message)
    member = await app.get_chat_member(message.chat.id, user_id)
    reply = await check_user_id(user_id)
    rt = ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if reply:
        await message.reply_text(reply)
        return ""
    if  user_id in DRAGONS:
        await message.reply_text("This member is already a Dragon Disaster")
    if  user_id in DEV_USERS:
        await message.reply_text("This member is already a dev Disaster")

    data["sudos"].append(user_id)
    DRAGONS.append(user_id)
    
    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    await message.reply_text(
        ʀᴛ
        + "\nsᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛ ᴅɪsᴀsᴛᴇʀ ʟᴇᴠᴇʟ ᴏғ {} ᴛᴏ ᴅʀᴀɢᴏɴ!".format(
            member.mention,
        ),
    )
    
        
