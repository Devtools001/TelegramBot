import time
from TeleBot import pgram
from pyrogram import filters 
from TeleBot import REDIS, get_readable_time

async def start_afk(userid, reason):
    REDIS.set(f'is_afk_{userid}', reason)
    
async def is_user_afk(userid):
    rget = REDIS.get(f'is_afk_{userid}')
    if rget:
        return True
    else:
        return False

async def end_afk(userid):
    REDIS.delete(f'is_afk_{userid}')
    return True

def strb(redis_string):
    return str(redis_string)

@pgram.on_message(filters.command("afk"))
async def afk(_, message):
    user = message.from_user
    if not user:
        return
    if user.id == 777000:
        return    
    args = message.text.split(None, 1)
    start_time = time.time()
    if len(args) >= 2:
        reason=args[1]
    else:
        reason = "none"

    await start_afk(user.id, reason)

    REDIS.set(f'afk_time_{user.id}', start_time)

    fname = user.first_name

    try:
        await message.reply_text(
            "{} is now away!".format(fname))

    except Exception:
        pass

@pgram.on_message(filters.all & filters.group)
async def afk(_, message):
    user = message.from_user
    #message = update.effective_message
    if not user:  # ignore channels
        return

    if not await is_user_afk(user.id):  #Check if user is afk or not
        return

    end_afk_time = get_readable_time((time.time() - float(REDIS.get(f'afk_time_{user.id}'))))

    REDIS.delete(f'afk_time_{user.id}')
    res = await end_afk(user.id)
    if res:
        if message.new_chat_members:  #dont say msg
            return
        firstname = user.first_name

        try:
            await message.reply_text(
                "{} is back online!\n\nYou were gone for {}.".format(firstname, end_afk_time))
        except Exception:
            return
    
    
    

    

        
    
    
__help__ = """
⸢ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ ᴍᴇɴᴛɪᴏɴs ʏᴏᴜ ɪɴ ᴀ ᴄʜᴀᴛ, ᴛʜᴇ ᴜsᴇʀ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ ʏᴏᴜ ᴀʀᴇ AFK. ʏᴏᴜ ᴄᴀɴ ᴇᴠᴇɴ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇᴀsᴏɴ ғᴏʀ ɢᴏɪɴɢ AFK, ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ ᴀs ᴡᴇʟʟ.⸥

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /afk - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ.

๏ /afk [ʀᴇᴀsᴏɴ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ ᴡɪᴛʜ ᴀ ʀᴇᴀsᴏɴ.

๏ /afk [ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ/ᴘʜᴏᴛᴏ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sᴛɪᴄᴋᴇʀ.

๏ /afk [ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ/ᴘʜᴏᴛᴏ] [ʀᴇᴀsᴏɴ] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴀғᴋ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴀɴᴅ ʀᴇᴀsᴏɴ ʙᴏᴛʜ.
═───────◇───────═
"""
__mod_name__ = "𝙰ғᴋ"
