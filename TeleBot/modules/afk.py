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
    user_id = message.from_user.id
    user_verify, user_reason = await is_afk(user_id) 
    print(user_verify)
    if user_verify:
        print("ok")
      #  await remove_afk(user_id)

          
    
    
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
