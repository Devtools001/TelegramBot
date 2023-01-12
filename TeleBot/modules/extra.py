import os
from TeleBot import pgram 
from pyrogram import filters

@pgram.on_message(filters.command("spoiler"))
async def _spoil(_, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("`ɪ ᴛʜɪɴᴋ ʏᴏᴜ sʜᴏᴜʟᴅ ʀᴇᴘʟʏ ᴛᴏ ᴀ ɪᴍᴀɢᴇ.`")
    if not replied.photo:
        return await message.reply_text("`ɪ sᴀɪᴅ ʀᴇᴘʟʏ ᴛᴏ ᴀ ɪᴍᴀɢᴇ ᴍғ.`")
    try: 
        file = await replied.download()
        await pgram.send_photo(message.chat.id,photo=file,has_spoiler=True)
        try:
            os.remove(file)
        except Exception as er:
            return await message.reply_text(er)
    except Exception as er:
        await message.reply_text(er)
