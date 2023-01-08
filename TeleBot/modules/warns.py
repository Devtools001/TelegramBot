from TeleBot import pgram, BOT_ID,DRAGONS,DEV_USERS,db
from TeleBot.modules.pyrogram_funcs.status import (
    bot_admin,
    bot_can_ban,
    user_admin,
    user_can_ban )

from pyrogram import filters
from TeleBot.modules.pyrogram_funcs.extracting_id import get_id_reason_or_rank
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery 

BUTTONS = [
    [
        InlineKeyboardButton(
            text="🚨  Remove Warn  🚨",
            callback_data=f"unwarn_{user_id}",
        ),
    ],       
]

SUPREME_USERS = DRAGONS,DEV_USERS
from typing import Dict,Union
from string import ascii_lowercase
warnsdb = db.warns

async def int_to_alpha(user_id : int) -> str:
    alphabet = list(ascii_lowercase)[:10]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text        

async def get_warns(chat_id : int) Dict[str,int]:
    warns = await warnsdb.find_one({"chat_id": chat_id})
    if not warns:
        return {}
    return warns["warns"]


async def get_warn(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    warns = await get_warns(chat_id)
    if name in warns:
        return warns[name]


async def add_warn(chat_id: int, name: str, warn: dict):
    name = name.lower().strip()
    warns = await get_warns(chat_id)
    warns[name] = warn

    await warnsdb.update_one(
        {"chat_id": chat_id}, {"$set": {"warns": warns}}, upsert=True
    )


async def remove_warns(chat_id: int, name: str) -> bool:
    warnsd = await get_warns(chat_id)
    name = name.lower().strip()
    if name in warnsd:
        del warnsd[name]
        await warnsdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"warns": warnsd}},
            upsert=True,
        )
        return True
    return False


async def get_warns_count() -> dict:
    chats_count = 0
    warns_count = 0
    async for chat in warnsdb.find({"chat_id": {"$lt": 0}}):
        for user in chat["warns"]:
            warns_count += chat["warns"][user]["warns"]
        chats_count += 1
    return {"chats_count": chats_count, "warns_count": warns_count}


@pgram.on_message(filters.command(["warn","dwarn"]) & ~filters.private)
@bot_admin
@bot_can_ban
@user_admin
@user_can_ban
async def _warns(_, message):
    user_id , reason = await get_id_reason_or_rank(message)
    chat_id = message.chat.id
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)
    if not user_id:
        await message.reply_text("I ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴡʜᴏ ʏᴏᴜ'ʀᴇ ᴛᴀʟᴋɪɴɢ ᴀʙᴏᴜᴛ, ʏᴏᴜ'ʀᴇ ɢᴏɪɴɢ ᴛᴏ ɴᴇᴇᴅ ᴛᴏ sᴘᴇᴄɪғʏ ᴀ ᴜsᴇʀ...!")
        return 
    if user_id == BOT_ID:
        await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴡᴀʀɴ ᴍʏsᴇʟғ, ɪ ᴄᴀɴ ʟᴇᴀᴠᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ.")
        return 
    if user_id in SUPREME_USERS:
        await message.reply_text("ʜᴇ ɪs ᴍʏ ʙʀᴀ, ɪ ᴄᴀɴ'ᴛ ɢᴇᴛ ᴀɢᴀɪɴsᴛ ᴍʏ ʙʀᴀ ᴏᴋ ᴍᴏᴛʜᴇʀ ғ*ᴋᴇʀ")
        return
    if user_id in administrators:
        await message.reply_text(f"ʜᴏᴡ ᴀᴍ I sᴜᴘᴘᴏsᴇᴅ ᴛᴏ ʙᴀɴ ᴀɴ ᴀᴅᴍɪɴ. ᴛʜɪɴᴋ {message.from_user.mention} ᴛʜɪɴᴋ.")
    
    user, warns = await asyncio.gather(
        pgram.get_users(user_id),
        get_warn(chat_id, await int_to_alpha(user_id)),
    ) 
    if warns:
        warns = warns["warns"]
    else:
        warns = 0
    
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if warns >= 2:
        await pgram.ban_chat_member(chat_id,user_id)
        await message.reply_text(
            f"Number of warns of {mention} exceeded, BANNED!"
        )
        await remove_warns(chat_id, await int_to_alpha(user_id))
    else:
        warn = {"warns": warns + 1}
        msg = f"""
**Warned User:** {mention}
**Warned By:** {message.from_user.mention if message.from_user else 'Anon'}
**Reason:** {reason or 'No Reason Provided.'}
**Warns:** {warns + 1}/3"""
        await message.reply_text(msg, reply_markup=InlineKeyboardMarkup(BUTTONS))
        await add_warn(chat_id, await int_to_alpha(user_id), warn)
 

@pgram.on_callback_query(filters.regex("unwarn_"))
async def remove_warning(_, cq: CallbackQuery):
    from_user = cq.from_user
    chat_id = cq.message.chat.id
    permissions = await member_permissions(chat_id, from_user.id)
    permission = "can_restrict_members"
    if permission not in permissions:
        return await cq.answer(
            "You don't have enough permissions to perform this action.\n"
            + f"Permission needed: {permission}",
            show_alert=True,
        )
    user_id = cq.data.split("_")[1]
    warns = await get_warn(chat_id, await int_to_alpha(user_id))
    if warns:
        warns = warns["warns"]
    if not warns or warns == 0:
        return await cq.answer("User has no warnings.")
    warn = {"warns": warns - 1}
    await add_warn(chat_id, await int_to_alpha(user_id), warn)
    text = cq.message.text.markdown
    text = f"~~{text}~~\n\n"
    text += f"__Warn removed by {from_user.mention}__"
    await cq.message.edit(text)


@pgram.on_message(
    filters.command("rmwarns") & ~filters.private
)

async def remove_warnings(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Reply to a message to remove a user's warnings."
        )
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    chat_id = message.chat.id
    warns = await get_warn(chat_id, await int_to_alpha(user_id))
    if warns:
        warns = warns["warns"]
    if warns == 0 or not warns:
        await message.reply_text(f"{mention} have no warnings.")
    else:
        await remove_warns(chat_id, await int_to_alpha(user_id))
        await message.reply_text(f"Removed warnings of {mention}.")    





       
    
