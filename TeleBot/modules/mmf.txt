#ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
#ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

from PIL import Image, ImageFont, ImageDraw
import textwrap
import os
from TeleBot import LOG as LOGGER    
from TeleBot import pgram
from pyrogram import filters 

TEMP_DOWNLOAD_DIRECTORY ="./"

Credit = "SIXTH_H0KAGE" 


@pgram.on_message(filters.command("mmf"))
async def mmf_mod(_,msg):

    if not msg.reply_to_message.id:

        await msg.reply_text("Provide Some Text To Draw!")

        return

    reply_message = msg.reply_to_message.photo.file_id

    if not msg.reply_to_message.media.PHOTO:

        await msg.reply_text("```Reply to a image/sticker.```")

        return

    file = await pgram.download_media(reply_message)

    msg = await msg.reply_text("```Memifying this image! ```")

    if "SIXTH_H0KAGE" in Credit:
       pass

    else: 
       await msg.reply_text("DON'T REMOVE CREDIT LINE MF")


    text = str(msg.pattern_match.group(1)).strip()

    if len(msg.command) < 2:

        return await msg.reply_text("You might want to try `/mmf text`")

    meme = await drawText(file, text)

    await pgram.send_photo(msg.chat.id, file=meme, force_document=False)
    
    await msg.delete() 
    
    os.remove(meme)


async def drawText(image_path, text):

    img = Image.open(image_path)

    os.remove(image_path)

    shadowcolor = "black"

    i_width, i_height = img.size

    if os.name == "nt":

        fnt = "ariel.ttf"

    else:

        fnt = "./TeleBot/resources/FontRemix.ttf"

    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))

    if ";" in text:

        upper_text, lower_text = text.split(";")

    else:

        upper_text = text

        lower_text = ''

    draw = ImageDraw.Draw(img)

    current_h, pad = 10, 5

    if upper_text:

        for u_text in textwrap.wrap(upper_text, width=15):

            u_width, u_height = draw.textsize(u_text, font=m_font)

            draw.text(xy=(((i_width - u_width) / 2) - 2, int((current_h / 640)

                                                             * i_width)), text=u_text, font=m_font, fill=(0, 0, 0))

            draw.text(xy=(((i_width - u_width) / 2) + 2, int((current_h / 640)

                                                             * i_width)), text=u_text, font=m_font, fill=(0, 0, 0))

            draw.text(xy=((i_width - u_width) / 2,

                          int(((current_h / 640) * i_width)) - 2),

                      text=u_text,

                      font=m_font,

                      fill=(0,

                            0,

                            0))

            draw.text(xy=(((i_width - u_width) / 2),

                          int(((current_h / 640) * i_width)) + 2),

                      text=u_text,

                      font=m_font,

                      fill=(0,

                            0,

                            0))



            draw.text(xy=((i_width - u_width) / 2, int((current_h / 640)

                                                       * i_width)), text=u_text, font=m_font, fill=(255, 255, 255))

            current_h += u_height + pad

    if lower_text:

        for l_text in textwrap.wrap(lower_text, width=15):

            u_width, u_height = draw.textsize(l_text, font=m_font)

            draw.text(

                xy=(((i_width - u_width) / 2) - 2, i_height -

                    u_height - int((20 / 640) * i_width)),

                text=l_text, font=m_font, fill=(0, 0, 0))

            draw.text(

                xy=(((i_width - u_width) / 2) + 2, i_height -

                    u_height - int((20 / 640) * i_width)),

                text=l_text, font=m_font, fill=(0, 0, 0))

            draw.text(

                xy=((i_width - u_width) / 2, (i_height -

                                              u_height - int((20 / 640) * i_width)) - 2),

                text=l_text, font=m_font, fill=(0, 0, 0))

            draw.text(

                xy=((i_width - u_width) / 2, (i_height -

                                              u_height - int((20 / 640) * i_width)) + 2),

                text=l_text, font=m_font, fill=(0, 0, 0))



            draw.text(

                xy=((i_width - u_width) / 2, i_height -

                    u_height - int((20 / 640) * i_width)),

                text=l_text, font=m_font, fill=(255, 255, 255))

            current_h += u_height + pad          

    image_name = "memify.webp"

    webp_file = os.path.join(image_name)

    img.save(webp_file, "webp")

    return webp_file


__mod_name__ = "Memify"
