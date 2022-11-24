from TeleBot import pgram
from pyrogram import filters


@pgram.on_message(filters.command("tagall"))
async def tag_all(_,msg):
    async for m in pgram.get_chat_members(msg.chat.id):
        await msg.reply_text(f"hey {m.user.mention}")
