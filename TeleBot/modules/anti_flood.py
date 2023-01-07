from TeleBot import pgram
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin    
    )
from TeleBot.modules.mongo.flood_mongo import (
    get_antiflood_mode,
    get_flood,
    get_floodlimit)

from TeleBot.helpers.time_checker import time_string_helper

@pgram.on_message(filters.command("flood"))
@bot_admin
@bot_can_ban
@user_admin
async def _flood(_, message):
    chat_id = message.chat.id
    if not await get_flood(chat_id):
        return await message.reply_text("Tʜɪs ᴄʜᴀᴛ ɪsɴ'ᴛ ᴄᴜʀʀᴇɴᴛʟʏ ᴇɴғᴏʀᴄɪɴɢ ғʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ")

    FLOOD_LIMIT = await get_floodlimit(chat_id)
    FLOOD_MODE, FLOOD_TIME = await get_antiflood_mode(chat_id)
    text = f"Tʜɪs ᴄʜᴀᴛ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴇɴғᴏʀᴄɪɴɢ ғʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ ᴀғᴛᴇʀ {FLOOD_LIMIT} ᴍᴇssᴀɢᴇs." 
    if FLOOD_MODE == 1:
        text += "Aɴʏ ᴜsᴇʀ ᴛʜᴀᴛ sᴇɴᴅs ᴍᴏʀᴇ ᴛʜᴀɴ ᴛʜᴀᴛ ᴀᴍᴏᴜɴᴛ ᴏғ ᴍᴇssᴀɢᴇs ᴡɪʟʟ ʙᴇ ʙᴀɴɴᴇᴅ." 
    elif FLOOD_MODE == 2:
        text += "Any user that sends more than that amount of messages will be muted."
    elif FLOOD_MODE == 3:
        text += "Any user that sends more than that amount of messages will be kicked."
    elif FLOOD_MODE == 4:
        time_limit, time_format = time_string_helper(FLOOD_TIME)
        text += f"Any user that sends more than that amount of messages will be temporarily banned for {time_limit} {time_format}."
    elif FLOOD_MODE == 5:
        time_limit, time_format = time_string_helper(FLOOD_TIME)
        text += f"Any user that sends more than that amount of messages will be temporarily muted for {time_limit} {time_format}."

    await message.reply_text(text)   

__help__ = """
⸢*ᴀɴᴛɪғʟᴏᴏᴅ* ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴏɴ ᴜsᴇʀs ᴛʜᴀᴛ sᴇɴᴅ ᴍᴏʀᴇ ᴛʜᴀɴ x ᴍᴇssᴀɢᴇs ɪɴ ᴀ ʀᴏᴡ. ᴇxᴄᴇᴇᴅɪɴɢ ᴛʜᴇ sᴇᴛ ғʟᴏᴏᴅ ᴡɪʟʟ ʀᴇsᴜʟᴛ ɪɴ ʀᴇsᴛʀɪᴄᴛɪɴɢ ᴛʜᴀᴛ ᴜsᴇʀ.
 ᴛʜɪs ᴡɪʟʟ ᴍᴜᴛᴇ ᴜsᴇʀs ɪғ ᴛʜᴇʏ sᴇɴᴅ ᴍᴏʀᴇ ᴛʜᴀɴ 10 ᴍᴇssᴀɢᴇs ɪɴ ᴀ ʀᴏᴡ, ʙᴏᴛs ᴀʀᴇ ɪɢɴᴏʀᴇᴅ.⸥

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
「𝗔𝗗𝗠𝗜𝗡𝗦 𝗢𝗡𝗟𝗬」
๏ /flood*:* ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ғʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ sᴇᴛᴛɪɴɢ
• *ᴀᴅᴍɪɴs ᴏɴʟʏ:*
๏ /setflood <ɪɴᴛ/'ɴᴏ/'ᴏғғ>*:* ᴇɴᴀʙʟᴇs ᴏʀ ᴅɪsᴀʙʟᴇs ғʟᴏᴏᴅ ᴄᴏɴᴛʀᴏʟ
 *ᴇxᴀᴍᴘʟᴇ:* /setflood 10
๏ /setfloodmode <ban/kick/mute/tban/tmute> <value>*:* ᴀᴄᴛɪᴏɴ ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴡʜᴇɴ ᴜsᴇʀ ʜᴀᴠᴇ ᴇxᴄᴇᴇᴅᴇᴅ ғʟᴏᴏᴅ ʟɪᴍɪᴛ. ʙᴀɴ/ᴋɪᴄᴋ/ᴍᴜᴛᴇ/ᴛᴍᴜᴛᴇ/ᴛʙᴀɴ
═───────◇───────═
• *ɴᴏᴛᴇ:*
 • ᴠᴀʟᴜᴇ ᴍᴜsᴛ ʙᴇ ғɪʟʟᴇᴅ ғᴏʀ ᴛʙᴀɴ ᴀɴᴅ ᴛᴍᴜᴛᴇ!!
 ɪᴛ ᴄᴀɴ ʙᴇ:
 5ᴍ = 5 ᴍɪɴᴜᴛᴇs
 6ʜ = 6 ʜᴏᴜʀs
 3ᴅ = 3 ᴅᴀʏs
 1ᴡ = 1 ᴡᴇᴇᴋ
"""
__mod_name__ = "𝙰ɴᴛɪ-ғʟᴏᴏᴅ"
