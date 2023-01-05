import html
from TeleBot import pgram
from pyrogram import filters, enums 
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import BadRequest 

@pgram.on_message(filters.command("bots") & ~filters.private)
async def _adminlist(_, message):       
    chat_title = message.chat.title 
    chat_id = message.chat.id 

    repl = await message.reply(
            "» ғᴇᴛᴄʜɪɴɢ ʙᴏᴛs ʟɪsᴛ...",
            
        )
        
    bots = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
        bots.append(m)

    BOT_LIST = []
    for bot in bots:
        BOT_LIST.append(f"◎ {bot.user.mention}\n")

    admin_header = f"🎣 ʙᴏᴛs ɪɴ {chat_title}:\n"
    
    for admin in BOT_LIST:
        admin_header += admin
    await repl.edit(
        
            f"{admin_header}\n\n"
            )
        
    
        
    
