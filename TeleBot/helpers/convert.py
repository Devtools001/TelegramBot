import math
from datetime import datetime,timedelta 
from pyrogram.types import Message
 
async def time_converter(message: Message, time_value: str) -> int:
    unit = ["m", "h", "d"]  # m == minutes | h == hours | d == days
    check_unit = "".join(list(filter(time_value[-1].lower().endswith, unit)))
    currunt_time = datetime.now()
    time_digit = time_value[:-1]
    if not time_digit.isdigit():
        return await message.reply_text("ɪɴᴄᴏʀʀᴇᴄᴛ ᴛɪᴍᴇ sᴘᴇᴄɪғɪᴇᴅ.")
    if check_unit == "m":
        temp_time = currunt_time + timedelta(minutes=int(time_digit))
    elif check_unit == "h":
        temp_time = currunt_time + timedelta(hours=int(time_digit))
    elif check_unit == "d":
        temp_time = currunt_time + timedelta(days=int(time_digit))
    else:
        return await message.reply_text("ɪɴᴄᴏʀʀᴇᴄᴛ ᴛɪᴍᴇ sᴘᴇᴄɪғɪᴇᴅ.")
    return int(datetime.timestamp(temp_time))


async def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
