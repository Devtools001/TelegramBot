import os
from TeleBot import pgram, BOT_NAME
from pyrogram import filters , Client 
from telegraph import upload_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery
from telegraph import Telegraph

telegraph = Telegraph()
new_user = telegraph.create_account(short_name=short_name)
auth_url = new_user["auth_url"]

@pgram.on_message(filters.command(["tgm","tgt"]))
async def telegraph(app, message):
    replied = message.reply_to_message          
    if message.command[0] == "tgm":        
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
        reply_markup=InlineKeyboardMarkup( [
            [
            InlineKeyboardButton(text="Open Link", url=f"https://graph.org{downloaded_file[0]}"),
            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{downloaded_file[0]}")
            ],
            [
            InlineKeyboardButton(text="✗ Close ✗", callback_data="close")
            ],
          ]
        )
      )
    if message.command[0] == "tgt":        
        if not replied:
            await message.reply_text("reply to a text")
            return 
    
        elif replied.text:
            text = await message.reply("Downloading to My Server")
            response = telegraph.create_page(title=BOT_NAME,html_content=(replied.text.html).replace("\n", "<br>"),author_name=str(message.from_user.first_name),author_url = f'https://telegram.dog/{message.from_user.username}' if m.from_user.id else None)
)
                                
            
        await text.edit("https://telegra.ph/{}".format(response["path"]))
