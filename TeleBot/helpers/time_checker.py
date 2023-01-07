from TeleBot.helpers.convert import convert_time


async def check_time(message, args) -> bool:
    if len(args) == 0:
        await message.reply(
            f"failed to get specified time: You didn't provide me time"
        )
        return
        
    if len(args) == 1:           
        await message.reply(
            (
                f"ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ sᴘᴇᴄɪғɪᴇᴅ ᴛɪᴍᴇ:: '{args[-1]}' ᴅᴏᴇs ɴᴏᴛ ғᴏʟʟᴏᴡ ᴛʜᴇ ᴇxᴘᴇᴄᴛᴇᴅ ᴛɪᴍᴇ ᴘᴀᴛᴛᴇʀɴs.\nExᴀᴍᴘʟᴇ ᴛɪᴍᴇ ᴠᴀʟᴜᴇs: 𝟺ᴍ = 𝟺 ᴍɪɴᴜᴛᴇs, 𝟹ʜ = 𝟹 ʜᴏᴜʀs, 𝟼ᴅ = 𝟼 ᴅᴀʏs, 𝟻ᴡ = 𝟻 ᴡᴇᴇᴋs".)
                
            
        
        return False

    elif len(args) > 1:
        if not args[-2].isdigit():
            await message.reply(
                f"failed to get specified time: '{args[-2]}' is not a valid number"
            )
            return False

        elif args[-1] in ['w', 'd', 'h', 'm']:
            check_time_limit = convert_time(int(args[:-1]), args[-1])
            if check_time_limit >= 31622400: #  31622400 ( seconds ) is 366 days 
                await message.reply(
                    "failed to get specified time: temporary actions have to be between 1 minute and 366 days"
                )
                return False
            return True
        else:
            await message.reply(
                    f"ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ sᴘᴇᴄɪғɪᴇᴅ ᴛɪᴍᴇ:: '{args[-1]}'ɪs ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ᴛɪᴍᴇ ᴄʜᴀʀ; ᴇxᴘᴇᴄᴛᴇᴅ ᴏɴᴇ ᴏғ ᴡ/ᴅ/ʜ/ᴍ (ᴡᴇᴇᴋs, ᴅᴀʏs, ʜᴏᴜʀs, ᴍɪɴᴜᴛᴇs)"
                )
            return False

async def get_time(message):
    if message.reply_to_message:    
        if not len(message.command) >= 2
                    
            await message.reply(
                "Yᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴘᴇᴄɪғɪᴇᴅ ᴀ ᴛɪᴍᴇ ᴛᴏ ᴍᴜᴛᴇ ᴛʜɪs ᴜsᴇʀ ғᴏʀ!"
            )
            return

        args = message.command[1]
        if await check_time(message, args):
            return args

    elif not message.reply_to_message :
        if not len(message.command) >= 3:
            await message.reply(
                "Yᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴘᴇᴄɪғɪᴇᴅ ᴀ ᴛɪᴍᴇ ᴛᴏ ᴍᴜᴛᴇ ᴛʜɪs ᴜsᴇʀ ғᴏʀ!"
            )
            return

        args = message.command[2]
        if await check_time(message, args):
            return args      


async def time_string_helper(time_args):
    time_limit = int(time_args[:-1])
    if time_args[-1] == 'w':
        time_format = 'weeks'
    elif time_args[-1] == 'd':
        time_format = 'days'
    elif time_args[-1] == 'h':
        time_format = 'hours'
    elif time_args[-1] == 'm':
        time_format = 'mintues'
    return time_limit, time_format 

 
