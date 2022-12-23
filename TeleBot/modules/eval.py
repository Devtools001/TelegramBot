import os
from TeleBot import pgram
from pyrogram import filters



namespaces = {}


async def namespace_of(chat, message, bot):
    if chat not in namespaces:
        namespaces[chat] = {
            "__builtins__": globals()["__builtins__"],
            "bot": bot,
            "effective_message": message,
            "effective_user": message.from_user,
            "effective_chat": message.from_chat,
            "update": update,
        }

    return namespaces[chat]


@pgram.on_message(filters.command("eval"))
async def eval(_, message):
    print(message.text)
    print(message.from_chat)    
    
