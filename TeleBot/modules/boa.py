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
    
    chat_name = message.chat.title 
    chat_id = message.chat.id 

    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
        administrators.append(m)

    text = "ᴀᴅᴍɪɴs ɪɴ <b>{}</b>:".format(html.escape(chat_name))



                    
            
    text += "\n💫 BOTS's :"

    custom_admin_list = {}
    normal_admin_list = []

    for admin in administrators:
        user = admin.user
        status = admin.status
        custom_title = admin.custom_title

        if user.first_name == "":
            name = "☠ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ"
        else:
            name = user.mention

        # if user.username:
        #    name = escape_markdown("@" + user.username)
        
        if custom_title:
            try:
                custom_admin_list[custom_title].append(name)
            except KeyError:
                custom_admin_list.update({custom_title: [name]})
        else:
            normal_admin_list.append(name)

    for admin in normal_admin_list:
        text += "\n<code> • </code>{}".format(admin)

    for admin_group in custom_admin_list.copy():
        if len(custom_admin_list[admin_group]) == 1:
            text += "\n<code> • </code>{} | <code>{}</code>".format(
                custom_admin_list[admin_group][0],
                html.escape(admin_group),
            )
            custom_admin_list.pop(admin_group)

    text += "\n"
    for admin_group, value in custom_admin_list.items():
        text += "\n🔮 <code>{}</code>".format(admin_group)
        for admin in value:
            text += "\n<code> • </code>{}".format(admin)
        text += "\n"

    try:
        await repl.edit_text(text, parse_mode=enums.ParseMode.HTML)
    except BadRequest:  # if original message is deleted
        return    
    
        
