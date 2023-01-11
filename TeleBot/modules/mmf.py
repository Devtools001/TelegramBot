import glob
import textwrap
import random 
from os import remove 
from TeleBot import pgram 
from pyrogram import filters
from PIL import Image, ImageFont, ImageDraw



@pgram.on_message(filters.command("mmf"))
async def memify(client, message):
    msg = await message.reply("`ᴍᴇᴍɪғʏɪɴɢ ᴛʜɪs ɪᴍᴀɢᴇ! ✊🏻`")

    replied = message.reply_to_message

    if len(message.command) < 2 or not replied:
        return await msg.edit("ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴀɴᴅ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ sᴛɪᴄᴋᴇʀ. 💌")

    if not (replied.photo or replied.sticker):
        return await msg.edit("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴍᴇᴍɪғʏ ᴘʜᴏᴛᴏs ᴏʀ sᴛɪᴄᴋᴇʀs.")
    
    text = message.text.split(None, 1)[1].strip()

    if "-r" in text:
        text = text.replace("-r","")
        font = glob.glob("./TeleBot/resources/Logo_fonts/*")
        font_path = random.choice(font)

    elif "-a" in text :
        text = text.replace("-a","")
        font_path = "./TeleBot/resources/mmf_fonts/a.otf"

    elif "-d" in text :
        text = text.replace("-d","")
        font_path = "./TeleBot/resources/mmf_fonts/d.otf"
        
    elif "-l" in text:
        text = text.replace("-l","")
        font_path = "./TeleBot/resources/mmf_fonts/di.ttf"

    elif "-h" in text :
        text = text.replace("-h","")
        font_path = "./TeleBot/resources/mmf_fonts/h.ttf"

    else:         
        font_path = "./TeleBot/resources/FontRemix.ttf"

    try:        
        file = await replied.download()
        res = await draw_meme_text(file,text,font_path)
        await message.reply_sticker(res)
        try:
           await msg.delete()
           remove(res)
        except:
            pass
    except Exception as er:                           
        await msg.edit("ᴜsᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ /ᴍᴍғ  ᴡɪᴛʜ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ sᴛɪᴄᴋᴇʀ, sᴇᴘᴀʀᴀᴛᴇᴅ ʙʏ ;  ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ᴛᴇxᴛ ᴘᴏsɪᴛɪᴏɴ ʙᴇʟᴏᴡ.")
    
        

    

async def draw_meme_text(image_path, text,font_path):
    img = Image.open(image_path)
    remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype(font_path, int((70 / 640) * i_width))
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)

            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="gray",
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="gray",
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="gray",
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="gray",
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="gray",
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="gray",
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="gray",
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="gray",
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
                stroke_width=3,
                stroke_fill="gray",
            )
            current_h += u_height + pad

    webp_file = "memify.webp"
    img.save(webp_file, "WebP")
    return webp_file

__help__ = """
**⸢ᴅʀᴀᴡ ᴛᴇxᴛ ᴏɴ ɪᴍᴀɢᴇs ᴏʀ sᴛɪᴄᴋᴇʀ ᴡɪᴛʜ ᴄᴏᴏʟ ғᴏɴᴛs.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /mmf «ᴛᴇxᴛ» : ᴅʀᴀᴡ ᴀ ᴛᴇxᴛ ᴏɴ ᴀ ᴘʜᴏᴛᴏ ᴏʀ sᴛɪᴄᴋᴇʀ

Ⓣ︎Ⓡ︎Ⓨ︎ Ⓦ︎Ⓘ︎Ⓣ︎Ⓗ︎ Ⓓ︎Ⓘ︎Ⓕ︎Ⓕ︎Ⓡ︎Ⓔ︎Ⓑ︎Ⓣ︎ Ⓕ︎Ⓞ︎Ⓝ︎Ⓣ︎Ⓢ︎
๏ /mmf  -r «ᴛᴇxᴛ»
๏ /mmf -a «ᴛᴇxᴛ»
๏ /mmf -d «ᴛᴇxᴛ»
๏ /mmf -l «ᴛᴇxᴛ»
๏ /mmf -h «ᴛᴇxᴛ»
═───────◇───────═
"""
__mod_name__ = "𝙼ᴇᴍɪғʏ"

