from gpytranslate import SyncTranslator
from TeleBot import pgram
from pyrogram import filters, enums 

trans = SyncTranslator()

@pgram.on_message(filters.command(["tr","tl"]))
async def _translate(_, message):
    text = await message.reply("📝 ᴛʀᴀɴsʟᴀᴛɪɴɢ......")
    replied = message.reply_to_message
    if not replied:
        return await text.edit("📝 ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ɪᴛ!")
    
    if replied.caption:
        to_translate = replied.caption
    elif replied.text:
        to_translate = replied.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = trans.detect(to_translate)
            dest = args    
    
    except IndexError:
        source = trans.detect(to_translate)
        dest = "en"
    translation = trans(to_translate,
                        sourcelang=source, targetlang=dest)
    reply = f"**📒 ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} ᴛᴏ {dest} :**\n" \
        f"`{translation.text}`"

    await text.edit(reply)  

__help__ = """
**⸢ᴀ sɪᴍᴘʟᴇ ʟᴀɴɢᴜᴀɢᴇ ᴛʀᴀɴsʟᴀᴛᴏʀ.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /tr (ᴏʀ /tl): ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ᴛʀᴀɴsʟᴀᴛᴇs ɪᴛ ᴛᴏ ᴇɴɢʟɪsʜ.

๏ /tl <ʟᴀɴɢ>: ᴛʀᴀɴsʟᴀᴛᴇs ᴛᴏ <ʟᴀɴɢ>
ᴇɢ: /tl ɪᴀ: ᴛʀᴀɴsʟᴀᴛᴇs ᴛᴏ ɪᴀᴘᴀɴᴇsᴇ.

๏ /tl //<ᴅᴇsᴛ>: ᴛʀᴀɴsʟᴀᴛᴇs ғʀᴏᴍ  ᴛᴏ <ʟᴀɴɢ>.
ᴇɢ: /tl jᴀ//ᴇɴ: ᴛʀᴀɴsʟᴀᴛᴇs ғʀᴏᴍ Jᴀᴘᴀɴᴇsᴇ ᴛᴏ Eɴɢʟɪsʜ.

[ʟɪsᴛ ᴏғ sᴜᴘᴘᴏʀᴛᴇᴅ ʟᴀɴɢᴜᴀɢᴇs ғᴏʀ ᴛʀᴀɴsʟᴀᴛɪᴏɴ](https://telegra.ph/Lang-Codes-03-19-3)
═───────◇───────═
"""   

__mod_name__ = "𝚃ʀᴀɴsʟᴀᴛᴏʀ"          
