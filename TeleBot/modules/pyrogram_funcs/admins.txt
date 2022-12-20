from functools import wraps
from TeleBot import pgram
from threading import RLock
from cachetools import TTLCache
from pyrogram.types import ChatMember

ADMIN_CACHE = TTLCache(maxsize=512, ttl=60 * 10, timer=perf_counter)
THREAD_LOCK = RLock()
        
def is_user_admin(_, msg) -> bool:
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]
    chat_id = msg.chat.id
    user_id = msg.from_user.id
    member = await app.get_chat_member(chat_id,user_id)
    administrators = []
    async for m in pgram.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)
    if (
        msg.chat.type == "private"       
        or user_id in administrators
        or user_id in {1087968824}
    ): 
        return True
    if member.status in ranks:
        return True
                      
    with THREAD_LOCK:        
        try:
            return user_id in ADMIN_CACHE[chat_id]
        except KeyError:
            pass 

def user_admin(func):
    @wraps(func)
    async def is_admin(_,msg, *args, **kwargs):        
        user = msg.from_user
        chat_id = msg.chat.id
        if user and is_user_admin(chat_id, user):
            return await func(_,msg, *args, **kwargs)
        if not user:
            pass        
        else:
            await msg.reply_text(
                "At Least be an Admin to use these all Commands",
            )

    return is_admin
           
            
            
