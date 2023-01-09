import time 
import asyncio
from TeleBot import pgram,get_readable_time
from pyrogram import filters, enums 
from TeleBot.modules.pyrogram_funcs.status import user_admin


SPAM_CHATS = []

@pgram.on_message(filters.command("tagall") & ~filters.private)
@user_admin
async def tag_all_users(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.") 
        return                  
    if replied:
        SPAM_CHATS.append(message.chat.id)
        start = time.time()        
        usernum= 0
        usertxt = ""
        async for m in pgram.get_chat_members(message.chat.id): 
            if message.chat.id not in SPAM_CHATS:
                break       
            usernum += 1
            usertxt += f"\t✨ [{m.user.first_name}](tg://user?id={m.user.id})"
            if usernum == 5:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        end = get_readable_time((time.time() - start))
        await message.reply_text(f"**ᴍᴇɴᴛɪᴏɴᴇᴅ ᴜsᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ\n🕜 ᴛɪᴍᴇ ᴛᴀᴋᴇɴ »** `{end}`")
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = (
            message.text.split(None, 1)[1]
            if len(message.command) < 3
            else message.text.split(None, 1)[1]
        )  
        SPAM_CHATS.append(message.chat.id)
        start = time.time()
        usernum= 0
        usertxt = ""
        async for m in pgram.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f"\t✨ [{m.user.first_name}](tg://user?id={m.user.id})"
            if usernum == 5:
                await pgram.send_message(message.chat.id,f'{usertxt}\n{text}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""            
        end = get_readable_time((time.time() - start))
        await message.reply_text(f"**ᴍᴇɴᴛɪᴏɴᴇᴅ ᴜsᴇʀs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ\n🕜 ᴛɪᴍᴇ ᴛᴀᴋᴇɴ »** `{end}`")                
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass        
           

@pgram.on_message(filters.command("atag") & ~filters.private)
async def tag_all_admins(_,message):
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("ʜᴇʏ ʙᴀʙʏ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇɴᴛɪᴏɴ **ᴀᴅᴍɪɴs**.") 
        return  
    if replied:                   
        username=0
        usertext = ''
        async for m in pgram.get_chat_members(message.chat.id,filter=enums.ChatMembersFilter.ADMINISTRATORS):
            username += 1
            usertext += f"\n✨ [{m.user.first_name}](tg://user?id={m.user.id})"
        await replied.reply_text(usertext)
    else:
        text = (
            message.text.split(None, 1)[1]
            if len(message.command) < 3
            else message.text.split(None, 1)[1]
        ) 
        username=0
        usertext = ''
        async for m in pgram.get_chat_members(message.chat.id,filter=enums.ChatMembersFilter.ADMINISTRATORS):
            username += 1
            usertext += f"\n✨ [{m.user.first_name}](tg://user?id={m.user.id})"
        await pgram.send_message(message.chat.id,f'{text}\n{usertext}')        

@pgram.on_message(filters.command("cancel") & ~filters.private)
@user_admin
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("sᴛᴏᴘᴘᴇᴅ ᴛʜᴇ ᴘʀᴏᴄᴇss.")     
                                     
    else :
        await message.reply_text("**ᴛʜᴇʀᴇ ɪs ɴᴏ ᴘʀᴏᴄᴇss ɢᴏɪɴɢ ᴏɴ ʙᴀʙʏ.**")  
        return       
    

    
