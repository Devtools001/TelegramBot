import time
from TeleBot import pgram,get_readable_time
from pyrogram import filters, enums 
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import UserStatus
from pyrogram.errors import FloodWait




@pgram.on_message(filters.command("bots") & ~filters.private)
async def _adminlist(_, message):       
    chat_title = message.chat.title 
    chat_id = message.chat.id 
    repl = await message.reply("» ғᴇᴛᴄʜɪɴɢ ʙᴏᴛs ʟɪsᴛ...")                                        
    bots = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
        bots.append(m)
    BOT_LIST = []
    for bot in bots:
        BOT_LIST.append(f"◎ {bot.user.mention}\n")
    header = f"🎣 ʙᴏᴛs ɪɴ {chat_title}:\n"    
    for bumt in BOT_LIST:
        header += bumt
    await repl.edit(f"{header}\n\n")
                  
            
@pgram.on_message(filters.command("kickthefools"))
async def _kickthefools(_,message):      
    text = await message.reply("ᴋɪᴄᴋɪɴɢ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴀ ᴍᴏɴᴛʜ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ")  
    chat_id = message.chat.id
    x = 0
    fools = []    
    ADMINS = []  
    start = time.time()     
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        ADMINS.append(m.user.id)
    
    async for member in pgram.get_chat_members(chat_id) :          
        user = member.user        
        if user.status == UserStatus.RECENTLY:
            if user.id in ADMINS :
               pass
            else:                
                fools.append(member.user.id)  
    if not fools:
       await text.edit("ᴛʜᴇʀᴇ ᴀʀᴇɴ'ᴛ ᴀɴʏ ғᴏᴏʟs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ")
    else:
        for i in ADMINS:
            try:                         
                await pgram.ban_chat_member(chat_id,fools[x])           
                await pgram.unban_chat_member(chat_id,fools[x])  
                x += 1                
            except IndexError:
                pass
            except FloodWait as e:
                asyncio.sleep(e.value)
        end = get_readable_time((time.time() - start))  
        await text.delete()
        await message.reply_text(f"ᴋɪᴄᴋᴇᴅ {len(fools)} ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴀ ᴍᴏɴᴛʜ.\n⏰ ᴛɪᴍᴇ ᴛᴏᴏᴋ : {end}")



