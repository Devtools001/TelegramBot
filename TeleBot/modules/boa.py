import html
from TeleBot import pgram
from pyrogram import filters, enums 
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import BadRequest 

@pgram.on_message(filters.command("bots") & ~filters.private)
async def _adminlist(_, message):    
   

    repl = await message.reply(
            "» ғᴇᴛᴄʜɪɴɢ bots ʟɪsᴛ...",
            
        )
    
    chat_title = message.chat.title 
    chat_id = message.chat.id 

    bots = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
        bots.append(m)

    ADMINS_LIST = []
    for bot in bots:
        ADMINS_LIST.append(f"{bot.user.mention}\n")

    admin_header = f"Admins in {html.escape(chat_title)}:\n"
    
    for admin in ADMINS_LIST:
        admin_header += admin
    await repl.edit(
        (
            f"{admin_header}\n\n"
            "__These are the updated values.__"
        
    )
        
    
