from TeleBot import pgram
from pyrogram import filters, enums 
from pyrogram.types import ChatMemberStatus

@pgram.on_message(filters.command("adminlist") & ~filters.private)
async def _adminlist(_, message):
    chat_id = message.chat.id
    chat_title = message.chat.title
    msg = await message.reply("ғᴇᴛᴄʜɪɴɢ ᴀᴅᴍɪɴs ʟɪsᴛ...")
    administrators = []
    async for m in pgram.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):        
        administrators.append(m)
    
    text = f"ᴀᴅᴍɪɴs ɪɴ {message.chat.title}"

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        
        if user.first_name == "":
            name = "☠ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ"
        else:
            name = f'{user.first_name + " " + user.last_name or ""}'
        if user.is_bot:
            administrators.remove(admin)
            continue

        if status == ChatMemberStatus.OWNER:
            text += "\n🥀 ᴏᴡɴᴇʀ :"
            text += f"\n{name}"
            if custom_title:
                text += f"┗━ {custom_title}"

    text += "\n💫 ᴀᴅᴍɪɴs :"
    custom_admin_list = {}
    normal_admin_list = [] 
    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title
        
        if user.first_name == "":
            name = "☠ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ"
        else:
            name = f"{user.first_name + " " + (user.last_name or "")}"
        if status == ChatMemberStatus.ADMINISTRATOR:
            if custom_title:
                try:
                    custom_admin_list[custom_title].append(name)
                except KeyError:
                    custom_admin_list.update({custom_title: [name]})
            else:
                normal_admin_list.append(name)

    
    for admin in normal_admin_list:
        text += f"\n • {admin}"

    for admin_group in custom_admin_list.copy():
        if len(custom_admin_list[admin_group]) == 1:
            text += "\n • {custom_admin_list[admin_group][0]} | {admin_group}"
                
            custom_admin_list.pop(admin_group)

    text += "\n"
    for admin_group, value in custom_admin_list.items():
        text += f"\n🔮 {admin_group}"
        for admin in value:
            text += "\n• {admin}"
        text += "\n"

    try:
        msg.edit_text(text)
    except BadRequest:  # if original message is deleted
        return













