import html
from TeleBot import pgram
from pyrogram import filters, enums 
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import BadRequest 

@pgram.on_message(filters.command("adminlist") & ~filters.private)
async def _adminlist(_, message):    
   # chat_id = message.chat.id
   # $chat_name = message.chat.title
    
   # repl = await message.reply(
   #         "» ғᴇᴛᴄʜɪɴɢ ᴀᴅᴍɪɴs ʟɪsᴛ...",
            
    #    )
    
    chat_title = message.chat.title 
    chat_id = message.chat.id 

    data_list = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        data_list.append(m)

    ADMINS_LIST = []
    
    for admin in data_list:
        user = admin.user
        status = admin.status
        if user.is_bot:
            administrators.remove(admin)
            continue
        if user.first_name == "":
            ADMINS_LIST.append("☠ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ")
        else:
            ADMINS_LIST.append(f"{user.mention}\n")


    admin_header = f"Admins in {html.escape(chat_title)}:\n"
    
    for admin in ADMINS_LIST:
        admin_header += admin
    await message.reply(
        (
            f"{admin_header}\n\n"
            "__These are the updated values.__"
        ),
        quote=True
    )
        
