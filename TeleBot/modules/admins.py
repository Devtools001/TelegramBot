import os
from TeleBot import pgram,LOG,BOT_ID,DEV_USERS,DRAGONS
from pyrogram import filters,enums
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_change_info,
    user_admin,
    user_can_change_info,
    bot_can_promote,
    user_can_promote )
from TeleBot.modules.pyrogram_funcs.extracting_id import (
    extract_user_id,
    get_id_reason_or_rank,
    get_user_id )

from pyrogram.enums import MessageEntityType, ChatMemberStatus
from pyrogram.types import ChatPrivileges
from pyrogram.errors import BadRequest

COMMANDERS = [ChatMemberStatus.ADMINISTRATOR,ChatMemberStatus.OWNER]
SUPREME_USERS = DEV_USERS + DRAGONS


PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True)

FULL_PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,    
    can_invite_users=True)

DEMOTE = ChatPrivileges(
        can_change_info=False,
        can_invite_users=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=False,
        can_manage_video_chats=False,
    )
    

    
        
@pgram.on_message(filters.command(["promote","fullpromote"]) & ~filters.private)
@bot_admin    
@bot_can_promote    
@user_admin
@user_can_promote
async def _promote(_, message):
    chat_id = message.chat.id
    user_id = await extract_user_id(message)  
    
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
   
    if not user_id:
        await message.reply_text("I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ ʏᴏᴜ'ʀᴇ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ, ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!")
        return
    if user_id == BOT_ID:
        await message.reply_text("ʙʀᴜʜ ʜᴏᴡ ᴄᴀɴ ɪ ᴘʀᴏᴍᴏᴛᴇ ᴍʏsᴇʟғ.")
        return 
    if user_id in administrators :
        await message.reply_text("ʙʀᴜʜ ʜᴏᴡ ᴄᴀɴ ɪ ᴘʀᴏᴍᴏᴛᴇ ᴀɴ ᴀᴅᴍɪɴ. ᴛʜɪɴᴋ ᴀʙᴏᴜᴛ ɪᴛ")
        return

    if message.command[0] == "promote": 
        user_mention = (await pgram.get_users(user_id)).mention
        try : 
            await pgram.promote_chat_member(chat_id,user_id,PROMOTE_POWERS)
            await message.reply_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ {user_mention}")
        except BadRequest as error:
            if error == "USER_NOT_MUTUAL_CONTACT":
                await message.reply_text("» ᴀs ɪ ᴄᴀɴ sᴇᴇ ᴛʜᴀᴛ ᴜsᴇʀ ɪs ɴᴏᴛ ᴩʀᴇsᴇɴᴛ ʜᴇʀᴇ.")
            else:
                await message.reply_text(
                "» sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴍᴀʏʙᴇ sᴏᴍᴇᴏɴᴇ ᴩʀᴏᴍᴏᴛᴇᴅ ᴛʜᴀᴛ ᴜsᴇʀ ʙᴇғᴏʀᴇ ᴍᴇ."
            )
            return

    if message.command[0] == "fullpromote":
        user_mention = (await pgram.get_users(user_id)).mention
        try : 
            await pgram.promote_chat_member(chat_id,user_id,FULL_PROMOTE_POWERS)
            await message.reply_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ғᴜʟʟ ᴘʀᴏᴍᴏᴛᴇᴅ {user_mention}")
        except BadRequest as error:
            if error  == "USER_NOT_MUTUAL_CONTACT":
                await message.reply_text("» ᴀs ɪ ᴄᴀɴ sᴇᴇ ᴛʜᴀᴛ ᴜsᴇʀ ɪs ɴᴏᴛ ᴩʀᴇsᴇɴᴛ ʜᴇʀᴇ.")
            else:
                await message.reply_text(
                "» sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ, ᴍᴀʏʙᴇ sᴏᴍᴇᴏɴᴇ ᴩʀᴏᴍᴏᴛᴇᴅ ᴛʜᴀᴛ ᴜsᴇʀ ʙᴇғᴏʀᴇ ᴍᴇ."
            )
            return
   

@pgram.on_message(filters.command("demote") & ~filters.private)
@bot_admin    
@bot_can_promote    
@user_admin
@user_can_promote
async def _demote(_, message):
    chat_id = message.chat.id
    user_id = await extract_user_id(message)  
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
               
    if not user_id:
        await message.reply_text("I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ ʏᴏᴜ'ʀᴇ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ, ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!")
        return
    if user_id == BOT_ID:
        await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴅᴇᴍᴏᴛᴇ ᴍʏsᴇʟғ..")
        return 
    if user_id in SUPREME_USERS:
        await message.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴇᴍᴏᴛᴇ ᴍʏ ғʀɪᴇɴᴅ ᴏᴋ ʏᴏᴜ ᴍғ.")
        return
    if user_id not in administrators :
        await message.reply_text("ᴛʜɪs ᴜsᴇʀ ɪsɴ'ᴛ  ᴀɴ ᴀᴅᴍɪɴ ᴀɴʏᴡᴀʏ!")
        return
    
    user_mention = (await pgram.get_users(user_id)).mention
    try : 
        await pgram.promote_chat_member(chat_id,user_id,DEMOTE)
        await message.reply_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴍᴏᴛᴇᴅ {user_mention}")
    except BadRequest as error:
        if error == "USER_NOT_MUTUAL_CONTACT":
            await message.reply_text("» ᴀs ɪ ᴄᴀɴ sᴇᴇ ᴛʜᴀᴛ ᴜsᴇʀ ɪs ɴᴏᴛ ᴩʀᴇsᴇɴᴛ ʜᴇʀᴇ.")
        else:
            await message.reply_text(error)  
        return            


@pgram.on_message(filters.command("title"))
@bot_admin
@bot_can_change_info
@user_admin
@user_can_change_info
async def _title(_, message):
    user = message.from_user
    replied= message.reply_to_message
    chat_id = message.chat.id
    if not user:
        return
    if not replied:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀᴅᴍɪɴ ᴛᴏ sᴇᴛ ʜɪs ᴀᴅᴍɪɴ ᴛɪᴛʟᴇ.")
        return
    if len(message.command) < 2:
        await message.reply_text("ɪᴛ ɪs'ɴᴛ ǫᴜɪᴛᴇ ʀɪɢʜᴛ.ɢɪᴠᴇ ᴀ ᴛᴇxᴛ ᴛᴏᴏ.")
        return
    try:
        title = message.text.split(None, 1)[1]
        await pgram.set_administrator_title(chat_id, replied.from_user.id,title)
        await message.reply_text(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ {replied.from_user.mention} ᴀᴅᴍɪɴ ᴛɪᴛʟᴇ ᴛᴏ {title}.")
    except Exception as e:
        await message.reply_text(e)

                       
        
@pgram.on_message(filters.command(["setgtitle","setgdesc"]) & ~filters.private)
@bot_admin
@bot_can_change_info
@user_admin
@user_can_change_info
async def g_title_desc(_,message):  
    chat_id = message.chat.id
    mention = message.from_user.mention
    replied = message.reply_to_message
    if not message.from_user:
            return   
    if message.command[0] == "setgtitle":       
        if len(message.command) < 2:
            await message.reply_text(f"ʜᴇʏ **{mention}** ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ.")  
            return
        else:
            get_new_title = message.text.split(None,1)[1]
            try:                    
                await pgram.set_chat_title(chat_id,get_new_title)      
                await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ.")
            except Exception:
                pass    
    if message.command[0] == "setgdesc":
        if len(message.command) < 2:
            await message.reply_text(f"ʜᴇʏ **{mention}** ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀ ɢʀᴏᴜᴘ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ.")  
            return 
        else:
            get_new_desc = message.text.split(None,1)[1]   
            try:                    
                await pgram.set_chat_description(chat_id,get_new_desc)      
                await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ.")
            except Exception:
                pass       
    
                                   
@pgram.on_message(filters.command(["setgpic","setgvid","delgpic"]) & ~filters.private)
@bot_admin
@bot_can_change_info
@user_admin
@user_can_change_info
async def g_pic_vid(_,message):
    chat_id = message.chat.id
    replied = message.reply_to_message

    if not message.from_user:
            return   
    if message.command[0] == "setgpic":
        if replied :            
            if replied.photo:
                text = await message.reply_text("ᴊᴜsᴛ ᴀ sᴇᴄ..... ")  
                g_pic = await replied.download()       
                try:                    
                    await pgram.set_chat_photo(chat_id, photo=g_pic)
                    await text.delete()
                    await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴘɪᴄ.")
                    
                except Exception as error:
                    await message.reply_text(error)

                os.remove(g_pic)

            else:
                await message.reply_text("ʜᴇʏ ʙᴀʙʏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀn ɪᴍᴀɢᴇ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. ɪғ ʏᴏᴜ ᴀʀᴇ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴛʜᴇɴ ᴜsᴇ /setgvid ᴄᴏᴍᴍᴀɴᴅ.")
        else:
            await message.reply_text("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ɪᴍᴀɢᴇ.")

    if message.command[0] == "setgvid":
        if replied:
            if replied.video:           
                text = await message.reply_text("ᴡᴀɪᴛᴏᴏ.....") 
                file = replied.video or replied.document or replied.animation 
                if not file:
                    return await message.reply_text(
                    "Reply to a photo or document to set it as chat_photo"
                )
                if file.file_size > 5000000 :
                    await message.reply_text("ғɪʟᴇ ɪs ᴛᴏᴏ ʙᴏɢ. 🙄")
                
                g_vid = await replied.download()                 
                try:                                
                    await pgram.set_chat_photo(chat_id, video=g_vid)
                    await text.delete()
                    await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ɢʀᴏᴜᴘ ᴘɪᴄ.")                    
                except Exception:
                    await message.reply_text("ʜᴇʏ ʜᴇʏ ʜᴇʏ....\nᴛʜᴇʀᴇ ᴀʀᴇ sᴏᴍᴇ ʟɪᴍɪᴛᴀᴛɪᴏɴs\nʏᴏᴜʀ ᴠɪᴅᴇᴏ ʀᴀᴛɪᴏ ᴍᴜsᴛ ʙᴇ 1:1 ᴀɴᴅ sɪᴢᴇ ᴜɴᴅᴇʀ 2ᴍʙ + ʟᴇss ᴛʜᴇɴ 10 sᴇᴄᴏɴs ᴏғ ʟᴇɴɢᴛʜ.")                
                    os.remove(g_vid)
                   
            else:
                await message.reply_text("ʜᴇʏ ʙᴀʙʏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. ɪғ ʏᴏᴜ ᴀʀᴇ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀn ɪᴍᴀɢᴇ ᴛʜᴇɴ ᴜsᴇ /setgpic ᴄᴏᴍᴍᴀɴᴅ.")
        else:
            await message.reply_text("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ.")  
    if message.command[0] == "delgpic":
        try:
            await pgram.delete_chat_photo(chat_id)
            await message.reply_text("sᴜᴄᴄᴇssғᴜʟʟʏ  ʀᴇᴍᴏᴠᴇᴅ ɢʀᴏᴜᴘ ᴘғᴘ.")
        except Exception as e:
            await message.reply_text(e)
            
__help__ = """
**⸢ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ ᴍᴇɴᴛɪᴏɴs ʏᴏᴜ ɪɴ ᴀ ᴄʜᴀᴛ, ᴛʜᴇ ᴜsᴇʀ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ ʏᴏᴜ ᴀʀᴇ AFK. ʏᴏᴜ ᴄᴀɴ ᴇᴠᴇɴ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇᴀsᴏɴ ғᴏʀ ɢᴏɪɴɢ AFK, ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ ᴀs ᴡᴇʟʟ.⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
「𝗔𝗗𝗠𝗜𝗡𝗦 𝗢𝗡𝗟𝗬」
 ๏ /promote <ᴜsᴇʀ> <ʀᴀɴᴋ>: ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴜsᴇʀ.
๏ /fullpromote <ᴜsᴇʀ> <ʀᴀɴᴋ>: ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴜsᴇʀ ᴡɪᴛʜ ғᴜʟʟ ʀɪɢʜᴛs.
๏ /demote <ᴜsᴇʀ>: ᴅᴇᴍᴏᴛᴇ ᴀ ᴜsᴇʀ.
๏ /setgtitle <ᴛɪᴛʟᴇ>: ᴇᴅɪᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴛɪᴛʟᴇ.
๏ /setgpic <ʀᴇᴘʟʏ to image>: sᴇᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ.
๏ /setgdesc <ᴛᴇxᴛ>: ᴇᴅɪᴛ ᴛʜᴇ ɢʀᴏᴜᴘ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ.
๏ /setgsticker <ʀᴇᴘʟʏ ᴛᴏ sᴛɪᴄᴋᴇʀ>: sᴇᴛ ᴛʜᴇ ɢʀᴏᴜᴘ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ.
๏ /adminlist: ʟɪsᴛ ᴛʜᴇ ᴀᴅᴍɪɴs ᴏғ ᴛʜᴇ ᴄʜᴀᴛ.
๏ /bots: ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ʙᴏᴛs ᴏғ ᴛʜᴇ ᴄʜᴀᴛ.
๏ /kickthefools: ᴋɪᴄᴋ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴡʜᴏ ᴡᴇʀᴇ ɪɴᴀᴄᴛɪᴠᴇ ғᴏʀ ᴏᴠᴇʀ ᴀ ᴍᴏɴᴛʜ.
๏ /invitelink: ᴇxᴘᴏʀᴛ ᴛʜᴇ ᴄʜᴀᴛ ɪɴᴠɪᴛᴇ ʟɪɴᴋ..
═───────◇───────═
"""
__mod_name__ = "𝙰ᴅᴍɪɴs"
