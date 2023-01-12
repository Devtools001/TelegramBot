import requests
import json
import asyncio
from TeleBot import pgram,BOT_USERNAME,BOT_ID, BOT_NAME
from pyrogram import filters,enums
from pyrogram.types import Message , InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 
from TeleBot.modules.pyrogram_funcs.chat_actions import send_action


buttons = InlineKeyboardMarkup([[ InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="add_chat({})"),InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="rm_chat({})")]])
            
        
    

@pgram.on_message(filters.command("chatbot"))
async def _check_bot(_, message):
    await message.reply_photo(photo="https://graph.org/file/1e810f699ea60b2962c61.jpg",
    caption="ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ"
    reply_markup=buttons)

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
@send_action(enums.ChatAction.TYPING)
async def chatbot(_, message):        
    if message.text and not message.document:
        if not await friday_message(message):
            return        
        url = f"https://kora-api.vercel.app/chatbot/2d94e37d-937f-4d28-9196-bd5552cac68b/{BOT_NAME}/Anonymous/message={message.text}"
        request = requests.get(url)
        results = json.loads(request.text)
        await asyncio.sleep(0.5)
        await message.reply_text(results["reply"])
