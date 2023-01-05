import html
from TeleBot import pgram
from pyrogram import filters, enums 
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import BadRequest 

@pgram.on_message(filters.command("adminlist") & ~filters.private)
async def _adminlist(_, message):    
    chat_id = message.chat.id
    chat_name = message.chat.title
    
    repl = await message.reply(
            "» ғᴇᴛᴄʜɪɴɢ ᴀᴅᴍɪɴs ʟɪsᴛ...",
            
        )
    
    ADMINS = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        ADMINS.append(m)        
    text = f"ᴀᴅᴍɪɴs ɪɴ {message.chat.title}"

    for owner in ADMINS  :
        if owner.user.first_name == "":
            owner_name = "☠ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ"
        else:
            name = owner.user.mention  
        if owner.status == ChatMemberStatus.OWNER:
            text += "\n 🥀 ᴏᴡɴᴇʀ :"
            text += f"\n • {name}\n"

            if owner.custom_title:
                text += f" ┗━ {custom_title}\n"

    await repl.edit(text)
    print(text)

  
