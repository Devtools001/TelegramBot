import os
from TeleBot import pgram
from pyrogram import filters , Client 
from telegraph import upload_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
#from TeleBot.utils.shit import TELEGRAPH

TELEGRAPH = InlineKeyboardMarkup( [
            [
            InlineKeyboardButton(text="Open Link", url=f"https://graph.org{downloaded_file[0]}"),
            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{downloaded_file[0]}")
            ],
            [
            InlineKeyboardButton(text="✗ Close ✗", callback_data="close")
            ],
          ]
        )

@pgram.on_message(filters.command("tgm"))
async def telegraph(app, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ɢᴇᴛ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ telegra.ph link")
        return 
    
    elif replied.media:
        text = await message.reply("Downloading to My Server")
        media = await replied.download()
        await text.edit_text(text="<code>Downloading Completed. Now I am Uploading to telegra.ph Link ...</code>", disable_web_page_preview=True)
        try:
            downloaded_file = upload_file(media)
        except Exception as error:
            print(error)
            await text.edit(text=f"Error :- {error}", disable_web_page_preview=True)       
            return    
        try:
            os.remove(media)
        except Exception as error:
            print(error)
            return  
        await text.edit(
        text=f"<b>Link :-</b>\n\n<code>https://graph.org{downloaded_file[0]}</code>",
        disable_web_page_preview=False,
        reply_markup=TELEGRAPH)
