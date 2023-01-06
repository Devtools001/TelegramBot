import time
from TeleBot import pgram
from pyrogram import filters 
from TeleBot import db, get_readable_time

afkmod = db.afk_users



async def add_afk(user_id : int,mode):
    await afkmod.update_one({"user_id": user_id},{"$set":{"reason": mode}},upsert=True)


async def rm_afk(user_id : int):
    is_user_afk = await afkmod.find_one({"user_id",user_id})
    if is_user_afk :
        return await afkmod.delete_one({"user_id":user_id})
 
async def is_afk(user_id : int) -> bool:
    user = await afkmod.find_one({"user_id":user_id}) 
    if user :
        return True,user["reason"]
    else:
        return False,{}              

@pgram.on_message(filters.command("afk", prefixes=["/", ".", "!"]))
async def _afk(_, message):
    if message.sender_chat :
        return
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    replied = message.reply_to_message
    user_verify, user_reason = await is_afk(user_id) 
    print(user_verify)
    if user_verify:        
        await rm_afk(user_id)
        try:
            afktype = user_reason["type"]
            timeafk = user_reason["time"]
            data = user_reason["data"]
            reasonafk = user_reason["reason"]
            total_time = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                send = await message.reply_text(
                    f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {total_time}",
                    disable_web_page_preview=True,
                )

            if afktype == "text_reason":
                send = await message.reply_text(
                    f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`",
                    disable_web_page_preview=True,
                ) 
 
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {total_time}",
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {total_time}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`",
                    ) 
 
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {total_time}",
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴀɴᴅ ᴡᴀs ᴀᴡᴀʏ ғᴏʀ {total_time}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`",
                    )    
        except Exception:
            send = await message.reply_text(
                f"**{user_name}** ɪs ʙᴀᴄᴋ ᴏɴʟɪɴᴇ",
                disable_web_page_preview=True,
            ) 
               
             
    if len(message.command) == 1 and not replied:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }                
    elif len(message.command) > 1 and not replied:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and replied.animation:
        _data = replied.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }

    elif len(message.command) > 1 and replied.animation:
        _data = replied.animation.file_id
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }

    elif len(message.command) == 1 and replied.photo:
        await pgram.download_media(replied, file_name=f"{user_id}.jpg")
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and replied.photo:
        await pgram.download_media(replied, file_name=f"{user_id}.jpg")
        _reason = message.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }

    elif len(message.command) == 1 and replied.sticker:
        if replied.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await pgram.download_media(
                replied, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }          
    elif len(message.command) > 1 and replied.sticker:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        if replied.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await pgram.download_media(
                replied, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }    

    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    await add_afk(user_id, details)    
    await message.reply_text(f"{user_name} ɪs ɴᴏᴡ ᴀғᴋ!")
    
    
    
__help__ = """
**⸢ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ ᴍᴇɴᴛɪᴏɴs ʏᴏᴜ ɪɴ ᴀ ᴄʜᴀᴛ, ᴛʜᴇ ᴜsᴇʀ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ ʏᴏᴜ ᴀʀᴇ AFK. ʏᴏᴜ ᴄᴀɴ ᴇᴠᴇɴ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇᴀsᴏɴ ғᴏʀ ɢᴏɪɴɢ AFK, ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ ᴀs ᴡᴇʟʟ.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /afk - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ.

๏ /afk [ʀᴇᴀsᴏɴ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ ᴡɪᴛʜ ᴀ ʀᴇᴀsᴏɴ.

๏ /afk [ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ/ᴘʜᴏᴛᴏ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sᴛɪᴄᴋᴇʀ.

๏ /afk [ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ/ᴘʜᴏᴛᴏ] [ʀᴇᴀsᴏɴ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴀғᴋ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴀɴᴅ ʀᴇᴀsᴏɴ ʙᴏᴛʜ.
═───────◇───────═
"""
__mod_name__ = "𝙰ғᴋ"
