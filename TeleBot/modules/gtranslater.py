from gpytranslate import SyncTranslator
from TeleBot import pgram
from pyrogram import filters, enums 

@pgram.on_message(filters.command(["tr","tl"]))
async def _translate(_, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("📝 ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ɪᴛ!")
    
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
    reply = f"<b>Translated from {source} to {dest}</b>:\n" \
        f"<code>{translation.text}</code>"

    await pgram.send_message(text=reply, chat_id=message.chat.id, parse_mode=enums.ParseMode.HTML)               
