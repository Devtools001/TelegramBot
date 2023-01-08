import wikipedia 
from TeleBot import pgram
from pyrogram import filters,enums
from wikipedia.exceptions import DisambiguationError, PageError

@pgram.on_message(filters.command("wiki"))
async def _wiki(_, message):
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ǫᴜᴇʀʏ.")
    if replied :
        search = replied.text
    else :
        search = message.text.split(None,1)[1]
    
    res = ""
    try:
        res = wikipedia.summary(search)
    except DisambiguationError as e:
        await message.reply_text(
            "Dɪsᴀᴍʙɪɢᴜᴀᴛᴇᴅ ᴘᴀɢᴇs ғᴏᴜɴᴅ! Aᴅɪᴜsᴛ ʏᴏᴜʀ ǫᴜᴇʀʏ ᴀᴄᴄᴏʀᴅɪɴɢʟʏ.\n<i>{}</i>".format(
                e
            ),
            parse_mode=enums.ParseMode.HTML,
        )
    except PageError as e:
        await message.reply_text(
            "<code>{}</code>".format(e), parse_mode=ParseMode.HTML
        )
    if res:
        result = f"<b>{search}</b>\n\n"
        result += f"<i>{res}</i>\n"
        result += f"""<a href="https://en.wikipedia.org/wiki/{search.replace(" ", "%20")}">ʀᴇᴀᴅ ᴍᴏʀᴇ...</a>"""
        if len(result) > 4000:
            with open("result.txt", "w") as f:
                f.write(f"{result}\n\nUwU OwO OmO UmU")
            with open("result.txt", "rb") as f:
                await pgram.send_document(
                    message.chat.id,
                    document=f,
                    caption=f.name,
                    parse_mode=ParseMode.HTML,
                )
        else:
            await message.reply_text(
                result, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            )    
