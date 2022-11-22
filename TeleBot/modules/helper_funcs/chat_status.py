from time import perf_counter
from TeleBot import dispatcher
from telegram import Chat, ChatMember, ParseMode, Update, TelegramError, User
from telegram.ext import CallbackContext
from cachetools import TTLCache
from threading import RLock
from functools import wraps
# stores admemes in memory for 10 min.
ADMIN_CACHE = TTLCache(maxsize=512, ttl=60 * 10, timer=perf_counter)
THREAD_LOCK = RLock()


def is_user_admin(chat: Chat, user_id: int, member: ChatMember = None) -> bool:
    if (
        chat.type == "private"        
        or chat.all_members_are_administrators
        or user_id in {1087968824}
    ):  # Count telegram and Group Anonymous as admin
        return True
    if member:
        return member.status in ("administrator", "creator")

    with THREAD_LOCK:
        # try to fetch from cache first.
        try:
            return user_id in ADMIN_CACHE[chat.id]
        except KeyError:
            # keyerror happend means cache is deleted,
            # so query bot api again and return user status
            # while saving it in cache for future useage...
            chat_admins = dispatcher.bot.getChatAdministrators(chat.id)
            admin_list = [x.user.id for x in chat_admins]
            ADMIN_CACHE[chat.id] = admin_list

            return user_id in admin_list

def user_admin(func):
    @wraps(func)
    def is_admin(update: Update, context: CallbackContext, *args, **kwargs):
        bot = context.bot
        user = update.effective_user
        chat = update.effective_chat

        if user and is_user_admin(chat, user.id):
            return func(update, context, *args, **kwargs)
        if not user:
            pass
        elif DEL_CMDS and " " not in update.effective_message.text:
            try:
                update.effective_message.delete()
            except:
                pass
        else:
            update.effective_message.reply_text(
                "At Least be an Admin to use these all Commands",
            )

    return is_admin