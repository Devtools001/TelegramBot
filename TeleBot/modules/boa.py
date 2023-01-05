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
    
    username=0
    usertext = ''
    async for m in pgram.get_chat_members(message.chat.id,filter=enums.ChatMembersFilter.BOTS):
        username += 1
        usertext += f"\n✨ [{m.user.first_name}](tg://user?id={m.user.id})"
    await repl.edit(f"🤖bots in message.chat.title\n{usertext})    
