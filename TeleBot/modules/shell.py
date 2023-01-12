import subprocess
from TeleBot import pgram,DEV_USERS,LOG
from pyrogram import filters,enums


@pgram.on_message(filters.command(["sh","shell"]) & filters.user(DEV_USERS))
async def _sh(_, message):
    if len(message.command) < 2:
        return await message.reply_text("`ɴᴏ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴇxᴇᴄᴜᴛᴇ ᴡᴀs ɢɪᴠᴇɴ.`")
    cmd = message.text.split(None,1)[1]
    process = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    stdout, stderr = process.communicate()
    reply = ""
    stderr = stderr
    if stdout := stdout.decode():
        reply += f" --sᴛᴅᴏᴜᴛ-- \n`{stdout}`\n"
        LOG.print(f"[bold yellow]Shell - {cmd} - {stdout}")
    if stderr:
        reply += f" --sᴛᴅᴇʀʀ-- \n`{stderr}`\n"
        LOG.print(f"[bold yellow]Shell - {cmd} - {stderr}")
    
    if len(reply) > 3000:
        with open("shell_output.txt", "w") as file:
            file.write(reply)
        with open("shell_output.txt", "rb") as doc:
            await message.reply_document(doc,caption=doc.name)
    
    else:
        await message.reply_text(f"""
📒 **ǫᴜᴇʀʏ :**
`{cmd}`   

`{reply}`
    """, parse_mode=enums.ParseMode.MARKDOWN)                
                
    
