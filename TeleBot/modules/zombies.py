import time
import asyncio
from TeleBot import pgram ,get_readable_time
from pyrogram.errors import FloodWait
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin,
    user_can_ban )
from pyrogram import filters 



@pgram.on_message(filters.command(["zombies","zombies clean") & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _zombies(_,message):      
    text = await message.reply("ғɪɴᴅɪɴɢ ᴢᴏᴍʙɪᴇs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ. 🧟‍♂️")  
    chat_id = message.chat.id
    x = 0
    zombies = []    
    ADMINS = []  
    start = time.time()     
        
    async for member in pgram.get_chat_members(chat_id) :          
        user = member.user        
        if user.is_deleted:                
           Nzombies.append(member.user.id) 

    if message.command[0] == "zombies": 
           await text.edit(f"{len(zombies)} ᴢᴏᴍʙɪᴇs ғᴏᴜɴᴅ ɪɴ {message.chat.title}.")
    if message.command[0] == "zombies clean":
        if len(zombies) == 0:
            return await message.reply_text("ᴛʜᴇʀᴇ ᴀʀᴇɴ'ᴛ ᴀɴʏ ᴢᴏᴍʙɪᴇs ɪɴ {message.chat.title}")
        for i in zombies :
            try:                         
                await pgram.ban_chat_member(chat_id,zombies[x])           
                x += 1                
            except IndexError:
                pass
            except FloodWait as e:
                asyncio.sleep(e.value)
        end = get_readable_time((time.time() - start))  
        await text.delete()
        await message.reply_text(f"ʙᴀɴɴᴇᴅ {len(zombies)} ᴢᴏᴍʙɪᴇs ɪɴ {message.chat.title}.\n⏰ ᴛɪᴍᴇ ᴛᴏᴏᴋ : {ᴇɴᴅ}")
    
