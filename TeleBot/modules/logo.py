import os
import io
import requests
import random
import glob

from TeleBot import pgram,MENTION_BOT,SUPPORT_CHAT,LOG
from pyrogram import filters
from PIL import Image,ImageDraw,ImageFont

from TeleBot.resources.LOGO_LINK.LOGO_LINKS import LOGOES
from telegraph import upload_file
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

key = InlineKeyboardMarkup([[InlineKeyboardButton("❌ ᴄʟᴏsᴇ", callback_data="close")]])

async def logo_vai(link,logo_text):
                randc = link
                logo = Image.open(io.BytesIO(requests.get(randc).content))                
                draw = ImageDraw.Draw(logo) 
                image_widthz, image_heightz = logo.size
                pointsize = 500
                fillcolor = "black"
                shadowcolor = "blue"
                fnt = glob.glob("./TeleBot/resources/Logo_fonts/*")
                randf = random.choice(fnt)
                font = ImageFont.truetype(randf, 120)
                w, h = draw.textsize(logo_text, font=font)
                h += int(h*0.21)
                image_width, image_height = logo.size
                draw.text(((image_widthz-w)/2, (image_heightz-h)/2), logo_text, font=font, fill=(255, 255, 255))
                x = (image_widthz-w)/2
                y = ((image_heightz-h)/2+6)
                draw.text((x, y), logo_text, font=font, fill="white", stroke_width=1, stroke_fill="black")
                final_logo = "friday.png"
                logo.save(final_logo, "png")
                return final_logo



@pgram.on_message(filters.command("logo"))
async def logo_make(_,message):
    if message.sender_chat:
        return 
    chat_id = message.chat.id
    replied = message.reply_to_message
    if len(message.command) < 2: 
        await message.reply_text("`⚗️ ɢɪᴠᴇ ᴀ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ʟᴏɢᴏ.`")
        return
             


    logo_text = message.text.split(None,1)[1]

    text = await message.reply("`ᴍᴀᴋɪɴɢ ʏᴏᴜʀ ʟᴏɢᴏ`")
        
    if not replied:
        try:
            randc = random.choice(LOGOES)
            final = await logo_vai(link=randc,logo_text=logo_text)
            await pgram.send_photo(chat_id,final, caption=f"ʟᴏɢᴏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ {MENTION_BOT}", reply_markup=key)
            await text.delete()
            if os.path.exists(final):
                os.remove(final)                
        except Exception as e:
            await message.reply_text(f"🧪 ᴇʀʀᴏʀ ʀᴇᴘᴏʀᴛ ɪɴ {SUPPORT_CHAT}\nᴇʀʀᴏʀ : {e}")
    
   
    if replied:
        if replied.photo:
            try:
                downloaded = await replied.download()
                uploaded_file = upload_file(downloaded)
                telegraph_link = f"https://graph.org{uploaded_file[0]}" 

                final = await logo_vai(link=telegraph_link,logo_text=logo_text)
                await pgram.send_photo(chat_id,final,caption=f"ʟᴏɢᴏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ {MENTION_BOT}", reply_markup=key)
                await text.delete()
                if os.path.exists(final):
                    os.remove(final) 
                try:
                    os.remove(downloaded)   
                except Exception as e:
                     LOG.print(f"[bold red] {e}")              
            
                
            except Exception as e:
                await message.reply_text(f"🧪 ᴇʀʀᴏʀ ʀᴇᴘᴏʀᴛ ɪɴ {SUPPORT_CHAT}\nᴇʀʀᴏʀ : {e}")
   
__help__ = """
**⸢ᴀ ᴄᴏᴏʟ ʟᴏɢᴏ ᴍᴀᴋᴇʀ ᴍᴏᴅᴜʟᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /logo «ᴛᴇxᴛ» : ɢᴇɴᴇʀᴀᴛᴇᴅ ᴀ ʀᴀɴᴅᴏᴍ ʟᴏɢᴏ ᴡɪᴛʜ ᴀ ᴛᴇxᴛ
๏ /logo «ᴛᴇxᴛ» : ɢᴇɴᴇʀᴀᴛᴇᴅ ᴀ ʟᴏɢᴏ ɪғ ʀᴇᴘʟʏ ᴛᴏ ᴀ ɪᴍᴀɢᴇ.
═───────◇───────═
"""

__mod_name__ = "𝙻ᴏɢᴏ ᴍᴀᴋᴇʀ"


         
