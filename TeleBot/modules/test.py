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
        if owner.user.is_bot:
           ADMINS.remove(owner)
           continue
     
        if owner.user.first_name == "":
            owner_name = "☠ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ"
        else:
            owner_name = owner.user.mention  
        if owner.status == ChatMemberStatus.OWNER:
            text += "\n 🥀 ᴏᴡɴᴇʀ :"
            text += f"\n • {owner_name}\n"

            if owner.custom_title:
                text += f" ┗━ {owner.custom_title}\n"
    print(text)
    text += "\n💫 ᴀᴅᴍɪɴs :"

    custom_admin_list = {}
    normal_admin_list = []

    for admin in ADMINS:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        if user.first_name == "":
            name = "☠ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ"
        else:
            name = user.mention
        
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
            text += f"\n • {custom_admin_list[admin_group][0]} | {admin_group}"
                
            custom_admin_list.pop(admin_group)

    text += "\n"
    for admin_group, value in custom_admin_list.items():
        text += f"\n🔮 {admin_group}"
        for admin in value:
            text += f"\n • {admin}"
        text += "\n"

    try:
        await repl.edit_text(text)
    except BadRequest:  # if original message is deleted
        return
