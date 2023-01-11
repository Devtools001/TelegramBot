import requests 
from .. import pgram as app 
from pyrogram import filters 

@app.on_message(filters.command("waifu"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/waifu"
    re=requests.get(url)
    e=re.json()
    waifu=e["url"]
    await msg.reply_photo(waifu, caption="""
     **ᴀ ᴡᴀɪғᴜ ᴀᴘᴘᴇᴀᴅᴇᴅ!**
ᴀᴅᴅ ᴛʜᴇᴍ ᴛᴏ ʏᴏᴜʀ ʜᴀʀᴇᴍ ʙʏ sᴇɴᴅɪɴɢ /wprotecc ᴄʜᴀʀᴀᴄᴛᴇʀ ɴᴀᴍᴇ.""")

@app.on_message(filters.command("wprotecc"))
async def waifu_protecc(_,msg):
    await msg.reply_text("OᴡO ʏᴏᴜ ᴘʀᴏᴛᴇᴄᴄ'ᴅ ᴀ Wᴀɪғᴜ ᴛʜɪs ᴡᴀɪғᴜ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ʜᴀʀᴇᴍ.")

@app.on_message(filters.command("wharem"))
async def waifu_harem(_,msg):
    await msg.reply_text("ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴘʀᴏᴛᴇᴄᴄ'ᴅ ᴀɴʏ ᴡᴀɪғᴜ ʏᴇᴛ...")


__help__ = """
**⸢ᴡᴀɪғᴜ⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═
๏ /waifu :  sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴡᴀɪғᴜ.

Ⓙ︎Ⓤ︎Ⓢ︎Ⓣ︎ Ⓕ︎Ⓞ︎Ⓡ︎ Ⓕ︎Ⓤ︎Ⓝ︎
๏ /wprotecc
๏ /wharem
═───────◇───────═
"""
__mod_name__ = "𝚆ᴀɪғᴜ"
