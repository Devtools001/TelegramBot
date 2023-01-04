from TeleBot import pgram
from pyrogram import filters, enums 


@pgram.on_message(filters.command("adminlist") & ~filters.private)
async def _adminlist(_, message):
    chat_id = message.chat.id
    chat_title = message.chat.title
    text = await message.reply("ғᴇᴛᴄʜɪɴɢ ᴀᴅᴍɪɴs ʟɪsᴛ...")
    administrators = []
    async for m in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):        
        administrators.append(m)
    

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title
        print(custom_title)
