import glob
import textwrap
import random 
from os import remove 
from TeleBot import pgram 
from pyrogram import filters
from PIL import Image, ImageFont, ImageDraw


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
                stroke_fill="black",
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="black",
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="black",
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
                stroke_width=3,
                stroke_fill="black",
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
                stroke_fill="black",
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
                stroke_fill="black",
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
                stroke_fill="black",
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
                stroke_fill="black",
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
                stroke_fill="black",
            )
            current_h += u_height + pad

    webp_file = "memify.webp"
    img.save(webp_file, "WebP")
    return webp_file


@pgram.on_message(filters.command("mmf"))
async def memify(client, message):
    replied = message.reply_to_message
    if len(message.command) < 2 or not replied:
        return await message.reply_text("ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴀɴᴅ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴏʀ sᴛɪᴄᴋᴇʀ. 💌")

    if not (replied.photo or replied.sticker):
        return await message.reply_text("ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴍᴇᴍᴏʀʏ ᴘʜᴏᴛᴏs ᴏʀ sᴛɪᴄᴋᴇʀs.")

    msg = await message.reply("ᴍᴇᴍɪғʏɪɴɢ ᴛʜɪs ɪᴍᴀɢᴇ! ✊🏻")

    text = message.text.split(None, 1)[1].strip()

    if "-r" in text:
        text = text.replace("-r","")
        font = glob.glob("./TeleBot/resources/Logo_fonts/*")
        font_path = random.choice(font)

    if "-a" in text :
        text = text.replace("-a","")
        font_path = "./TeleBot/mmf_fonts/AVENGEANCE HEROIC AVENGER BI.otf"

    if "-d" in text :
        text = text.replace("-d","")
        font_path = "./TeleBot/mmf_fonts/Dark Seed.otf"
        
    if "-di" in text:
        text = text.replace("-di","")
        font_path = "./TeleBot/mmf_fonts/digital.ttf"

    if "-h" in text :
        text = text.replace("-h","")
        font_path = "./TeleBot/mmf_fonts/hawkmoon.ttf"

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
        print(er)        
        await message.reply_text("ᴜsᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ /ᴍᴍғ  ᴡɪᴛʜ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴛʜᴇ sᴛɪᴄᴋᴇʀ, sᴇᴘᴀʀᴀᴛᴇᴅ ʙʏ ;  ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ᴛᴇxᴛ ᴘᴏsɪᴛɪᴏɴ ʙᴇʟᴏᴡ.")
    
        

    
