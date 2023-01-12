from os import remove 
from TeleBot import pgram
from pyrogram import filters
from gtts import gTTS,gTTSError


@pgram.on_message(filters.command("tts"))
async def _tts(_, message):
    replied = message.reply_to_message
    if message.sender_chat:
        return
    if len(message.command) < 2 and not replied:
        await message.reply_text(" ɢɪᴠᴇ ᴍᴇ ᴀ ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ.")
    if replied:
        text = replied.text
    else:
        text = message.text.split(None,1)[1]

   
    if "|" in text:
        lan, text = text.split("|")
    elif "|" not in text:
        lan = "en"
    else:
        await message.reply_text("Iɴᴠᴀʟɪᴅ Sʏɴᴛᴀx\ɴFᴏʀᴍᴀᴛ /ᴛᴛs ʟᴀɴɢ | ᴛᴇxᴛ\ɴFᴏʀ ᴇɢ: /ᴛᴛs ᴇɴ | ʜᴇʟʟᴏ")
    text = text.strip()
    lan = lan.strip()
    try:
        tts = gTTS(text, tld="com", lang=lan)
        tts.save("Friday.mp3")
    except AssertionError:
        await message.reply_text("ᴛʜᴇ ᴛᴇxᴛ ɪs ᴇᴍᴘᴛʏ.\nɴᴏᴛʜɪɴɢ ʟᴇғᴛ ᴛᴏ sᴘᴇᴀᴋ ᴀғᴛᴇʀ ᴘʀᴇ-ᴘʀᴇᴄᴇssɪɴɢ,\nᴛᴏᴋᴇɴɪᴢɪɴɢ ᴀɴᴅ ᴄʟᴇᴀɴɪɴɢ.")
    
    except ValueError:
        await message.reply_text("ʟᴀɴɢᴜᴀɢᴇ ɪs ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ.")
        return
    except RuntimeError:
        await message.reply_text("ᴇʀʀᴏʀ ʟᴏᴀᴅɪɴɢ ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇs ᴅɪᴄᴛɪᴏɴᴀʀʏ.")
        return
    except gTTSError:
        await message.reply_text("ᴇʀʀᴏʀ ɪɴ Gᴏᴏɢʟᴇ Tᴇxᴛ-ᴛᴏ-Sᴘᴇᴇᴄʜ API ʀᴇǫᴜᴇsᴛ!")
        return
    with open("Friday.mp3", "r"):
        await message.reply_audio("Friday.mp3")
        
        remove("Friday.mp3")
