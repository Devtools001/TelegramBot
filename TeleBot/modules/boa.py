
from TeleBot import pgram,DEV_USERS, DRAGONS
from pyrogram import filters, enums 
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import UserStatus
from pyrogram.errors import FloodWait

SUPREME_USERS = DRAGONS + DEV_USERS

@pgram.on_message(filters.command("bots") & ~filters.private)
async def _adminlist(_, message):       
    chat_title = message.chat.title 
    chat_id = message.chat.id 
    repl = await message.reply("» ғᴇᴛᴄʜɪɴɢ ʙᴏᴛs ʟɪsᴛ...")                                        
    bots = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
        bots.append(m)
    BOT_LIST = []
    for bot in bots:
        BOT_LIST.append(f"◎ {bot.user.mention}\n")
    header = f"🎣 ʙᴏᴛs ɪɴ {chat_title}:\n"    
    for bumt in BOT_LIST:
        header += bumt
    await repl.edit(f"{header}\n\n")
                  
            
@pgram.on_message(filters.command("kickthefools"))
async def _kickthefools(_,message):  
    text = await message.reply(f"kicking fools")  
    chat_id = message.chat.id
    fools = []    
    ADMINS = []   
    x = 0
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        ADMINS.append(m.user.id)
    
    async for member in pgram.get_chat_members(chat_id) :          
        user = member.user        
        if user.status == UserStatus.RECENTLY:
            if user.id in ADMINS :
               pass
            else:                
                fools.append(member.user.id)  
    if not fools:
       await message.reply_text("ᴛʜᴇʀᴇ ᴀʀᴇɴ'ᴛ ᴀɴʏ ғᴏᴏʟs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ")
    else:
        try:      
                   
            await pgram.ban_chat_member(chat_id,fools[x])
            await message.reply_text(f"kicking fools")
            await pgram.unban_chat_member(chat_id,member.user.id)  
            x += 1
        except FloodWait as e:
            asyncio.sleep(e.value)
        await text.edit(f"{len(fools)}")



