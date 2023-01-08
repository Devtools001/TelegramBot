import os
from TeleBot import pgram
from pyrogram import filters
from GoogleSearch import Search
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from GoogleSearch import Search
from pyrogram.errors import BadRequest

@pgram.on_message(filters.command(["pp","p","grs","reverse"]))
async def _reverse(_, message):
    if len(message.command) == 2:
        url = message.text.split(None,1)[1]
        if url.startswith(("https://", "http://")):
            msg = await message.reply_text("ᴜᴘʟᴏᴀᴅɪɴɢ ᴜʀʟ ᴛᴏ ɢᴏᴏɢʟᴇ..")
            result = Search(url=url)
            name = result["output"]
            link = result["similar"]
            try:
                await msg.edit_text("ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ɢᴏᴏɢʟᴇ, ғᴇᴛᴄʜɪɴɢ ʀᴇsᴜʟᴛs...")
                await msg.edit_text(
                    text=f"{name}",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text="sɪᴍɪʟᴀʀ",
                                    url=link,
                                ),
                            ],
                        ],
                    ),
                )
            except BadRequest as er :
                await message.reply_text(er)     
            return
        else:
            await message.reply_text(
                "ᴄᴏᴍᴍᴀɴᴅ ᴍᴜsᴛ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sʜᴏᴜʟᴅ ɢɪᴠᴇ ᴜʀʟ"
            )   
    replied = message.reply_to_message

    if replied and replied.photo:
        try:
            edit = await message.reply_text("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɪᴍᴀɢᴇ")
        except BadRequest:
            return

        photo = await pgram.download_media(replied.photo.file_id,file_name = "reverse.jpg")
        await edit.edit_text("ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ɪᴍᴀɢᴇ, ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ɢᴏᴏɢʟᴇ...")
        result = Search(file_path="reverse.jpg")
        await edit.edit_text("ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ɢᴏᴏɢʟᴇ, ғᴇᴛᴄʜɪɴɢ ʀᴇsᴜʟᴛs...")
        name = result["output"]
        link = result["similar"]

        await edit.edit_text(
            text=f"{name}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="sɪᴍɪʟᴀʀ",
                            url=link,
                        ),
                    ],
                ],
            ),
        )
        return
        os.remove(photo)
    else:
        await message.reply_text(
            "ᴄᴏᴍᴍᴀɴᴅ sʜᴏᴜʟᴅ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ ᴜʀʟ sʜᴏᴜʟᴅ ɢɪᴠᴇɴ."
        )
    








        
