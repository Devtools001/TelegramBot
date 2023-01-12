import requests
import json
import asyncio
from gtts import gTTS,gTTSError
from TeleBot import pgram,BOT_USERNAME,BOT_ID, BOT_NAME,db
from pyrogram import filters,enums, Client
from pyrogram.types import Message , InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 
from TeleBot.modules.pyrogram_funcs.chat_actions import send_action

chatbotdb = db.chatbot


async def addchat_bot(chat_id : int):
    return await chatbotdb.insert_one({"chat_id" : chat_id})
    
async def rmchat_bot(chat_id : int):    
    return await chatbotdb.delete_one({"chat_id" : chat_id})        


buttons = InlineKeyboardMarkup([[ InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="add_chat"),InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="rm_chat")]])
                        
@pgram.on_message(filters.command("chatbot"))
async def _check_bot(_, message):
    if message.sender_chat:
        return
    chat_id = message.chat.id
    user_id = message.from_user.id
    if message.chat.type != enums.ChatType.PRIVATE:
        administrators = []
        async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            administrators.append(m.user.id)
        if user_id in administrators:           
            return await message.reply_photo(photo="https://graph.org/file/1e810f699ea60b2962c61.jpg",
            caption="ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ",
            reply_markup=buttons)
        else:
            return await message.reply_text("**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʙᴇᴄᴏᴍᴇ ᴀᴅᴍɪɴ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ.**")
    else:
        return await message.reply_photo(photo="https://graph.org/file/1e810f699ea60b2962c61.jpg",
            caption="ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ",
            reply_markup=buttons)
    

@pgram.on_callback_query(filters.regex("add_chat"))
async def _addchat(app : Client, query : CallbackQuery):
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    check_chat = await chatbotdb.find_one({"chat_id" : chat_id})
  
    if query.message.chat.type != enums.ChatType.PRIVATE:
        administrators = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            administrators.append(m.user.id)
        if user_id in administrators:
            if not check_chat:  
                await addchat_bot(chat_id)           
                return await query.message.edit_caption("ᴇɴᴀʙʟᴇᴅ ᴄʜᴀᴛʙᴏᴛ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.")      
                
            elif check_chat:
                await query.message.edit_caption("ᴄʜᴀᴛʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.")
            
   
        else:
            await client.answer_callback_query(
            query.id,
            text = "❌ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴡᴏʀᴛʜʏ sᴏɴ.",
            show_alert = True)
    else:
        if not check_chat:
            await addchat_bot(user_id)                     
            return await query.message.edit_caption("ᴇɴᴀʙʟᴇᴅ ᴄʜᴀᴛʙᴏᴛ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.") 
        elif check_chat:
            await query.message.edit_caption("ᴄʜᴀᴛʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.")   
             
@pgram.on_callback_query(filters.regex("rm_chat"))
async def _rmchat(app : Client, query : CallbackQuery):
    user_id = query.from_user.id
    chat_id = query.message.chat.id
    check_chat = await chatbotdb.find_one({"chat_id" : chat_id})
  
    if query.message.chat.type != enums.ChatType.PRIVATE:
        administrators = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            administrators.append(m.user.id)
        if user_id in administrators:
            if check_chat:  
                await rmchat_bot(chat_id)           
                return await query.message.edit_caption("ᴅɪsᴀʙʟᴇᴅ ᴄʜᴀᴛʙᴏᴛ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.")      
                
            elif not check_chat:
                await query.message.edit_caption("ᴄʜᴀᴛʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.")
            
   
        else:
            await client.answer_callback_query(
            query.id,
            text = "❌ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴡᴏʀᴛʜʏ sᴏɴ.",
            show_alert = True)
    else:
        if check_chat:
            await rmchat_bot(user_id)                     
            return await query.message.edit_caption("ᴅɪsᴀʙʟᴇᴅ ᴄʜᴀᴛʙᴏᴛ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.") 
        elif not check_chat:
            await query.message.edit_caption("ᴄʜᴀᴛʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.")   
                 


async def friday_message(message : Message):
    reply_message = message.reply_to_message
    if message.text.lower() == "friday":
        return True
    elif BOT_USERNAME in message.text.upper():
        return True
    elif reply_message:
        if reply_message.from_user.id == BOT_ID:
            return True
    else:
        return False

@pgram.on_message(filters.text  & ~filters.bot,group=2)
async def chatbot(_, message): 
    chat_id = message.chat.id
    check_chat = await chatbotdb.find_one({"chat_id" : chat_id})
    if not check_chat:
        return        
    if message.text and not message.document:
        if not await friday_message(message):
            return  
        await pgram.send_chat_action(chat_id, enums.ChatAction.TYPING)      
        url = f"https://kora-api.vercel.app/chatbot/2d94e37d-937f-4d28-9196-bd5552cac68b/{BOT_NAME}/Anonymous/message={message.text}"
        request = requests.get(url)
        results = json.loads(request.text)
        await asyncio.sleep(0.5)
        text = results["reply"]
        await message.reply_text(text)
        try:
            tts = gTTS(text, tld="com", lang="en")
            tts.save("Friday.mp3")
        except gTTSError:
            await message.reply_text("ᴇʀʀᴏʀ ɪɴ Gᴏᴏɢʟᴇ Tᴇxᴛ-ᴛᴏ-Sᴘᴇᴇᴄʜ API ʀᴇǫᴜᴇsᴛ!")
            return
        with open("Friday.mp3", "r"):
            await message.reply_audio("Friday.mp3")        
        os.remove("Friday.mp3")
 
