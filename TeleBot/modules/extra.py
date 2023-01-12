import os
from TeleBot import pgram 
from pyrogram import filters

@pgram.on_message(filters.command("spoiler"))
async def _spoil(_, message):
    text = await message.reply("💘 ᴛʀʏɪɴɢ ᴛᴏ ᴍᴀᴋᴇ ɪᴛ sᴘᴏɪʟᴇʀ......")
    replied = message.reply_to_message
    if not replied:
        return await text.edit("`ɪ ᴛʜɪɴᴋ ʏᴏᴜ sʜᴏᴜʟᴅ ʀᴇᴘʟʏ ᴛᴏ ᴀ ɪᴍᴀɢᴇ.`")
    if not replied.photo:
        return await text.edit("`ʀᴇᴘʟʏ ᴛᴏ ᴀ ɪᴍᴀɢᴇ ᴍғ.`")
    try: 
        file = await replied.download()
        await pgram.send_photo(message.chat.id,photo=file,has_spoiler=True)
        try:
            os.remove(file)
        except Exception as er:
            return await text.edit(er)
        await text.delete()
    except Exception as er:
        await text.edit(er)
