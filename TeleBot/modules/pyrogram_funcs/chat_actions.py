from functools import wraps
from TeleBot import pgram

def send_action(action):   
    def decorator(func):
        @wraps(func)
        async def command_func(_,msg, *args, **kwargs):
            await pgram.send_chat_action(
                chat_id=msg.chat.id, action=action
            )
            return await func(_,msg, *args, **kwargs)

        return command_func

    return decorator
