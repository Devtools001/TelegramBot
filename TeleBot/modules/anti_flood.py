from TeleBot import pgram
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin,
    user_can_ban
    )
from TeleBot.modules.mongo.flood_mongo import (
    get_antiflood_mode,
    get_flood,
    get_floodlimit)



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
