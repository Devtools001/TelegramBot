import time
from TeleBot import pgram,get_readable_time
from pyrogram import filters, enums 
from pyrogram.enums import ChatMemberStatus




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
                  
            
