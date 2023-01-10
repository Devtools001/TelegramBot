from TeleBot import pgram
from pyrogram import filters
from TeleBot.helpers.mac_carbon import make_carbon

@pgram.on_message(filters.command("carbon"))
async def _carbon(_, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ.")
        return
    if not replied.text:
        return await message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴄᴀʀʙᴏɴ."
        )
    text = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ....")
    carbon = await make_carbon(replied.text)  
    await text.edit("ᴜᴘʟᴏᴀᴅɪɴɢ..")  
    await message.reply_photo(carbon)
    await text.delete()
    carbon.close()   

__help__ = """
**⸢ᴍᴀᴋᴇs ᴀ ᴄᴀʀʙᴏɴ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /carbon : ᴍᴀᴋᴇs ᴄᴀʀʙᴏɴ ɪғ ʀᴇᴩʟɪᴇᴅ ᴛᴏ ᴀ ᴛᴇxᴛ
═───────◇───────═
"""
__mod_name__ = "𝙲ᴀʀʙᴏɴ"
