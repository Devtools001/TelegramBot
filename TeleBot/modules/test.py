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
    for user in data_list:
        if user.user.username is not None:
            ADMINS_LIST.append(user.user.mention)
        else:
            ADMINS_LIST.append(f'- <a href=tg://user?id={user.user.id}>{user.user.first_name}</a> id `{user.user.id}`\n')


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
        
