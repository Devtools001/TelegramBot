import requests 
from TeleBot import pgram as app 
from pyrogram import filters 

@app.on_message(filters.command("waifu"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/waifu"
    re=requests.get(url)
    e=re.json()
    waifu=e["url"]
    await msg.reply_photo(waifu)

@app.on_message(filters.command("neko"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/neko"
    re=requests.get(url).json()    
    neko=re["url"]
    await msg.reply_photo(neko)

@app.on_message(filters.command("shinobu"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/shinobu"
    re=requests.get(url).json()    
    shinobu=re["url"]
    await msg.reply_photo(shinobu)

@app.on_message(filters.command("megumin"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/megumin"
    re=requests.get(url).json()    
    megumin=re["url"]
    await msg.reply_photo(megumin)

@app.on_message(filters.command("bully"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/bully"
    re=requests.get(url).json()    
    bully=re["url"]
    await msg.reply_video(bully)

@app.on_message(filters.command("cuddle"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/cuddle"
    re=requests.get(url).json()    
    cuddle=re["url"]
    await msg.reply_video(cuddle)


@app.on_message(filters.command("cry"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/cry"
    re=requests.get(url).json()    
    cry=re["url"]
    await msg.reply_video(cry)

@app.on_message(filters.command("hug"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/hug"
    re=requests.get(url).json()    
    hug=re["url"]
    await msg.reply_video(hug)


@app.on_message(filters.command("awoo"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/awoo"
    re=requests.get(url).json()    
    awoo=re["url"]
    await msg.reply_photo(awoo)

@app.on_message(filters.command("kiss"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/kiss"
    re=requests.get(url).json()    
    kiss=re["url"]
    await msg.reply_video(kiss)

@app.on_message(filters.command("lick"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/lick"
    re=requests.get(url).json()    
    lick=re["url"]
    await msg.reply_video(lick)

@app.on_message(filters.command("pat"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/pat"
    re=requests.get(url).json()    
    pat=re["url"]
    await msg.reply_video(pat)

@app.on_message(filters.command("smug"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/smug"
    re=requests.get(url).json()    
    smug=re["url"]
    await msg.reply_video(smug)

@app.on_message(filters.command("bonk"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/bonk"
    re=requests.get(url).json()    
    bonk=re["url"]
    await msg.reply_video(bonk)

@app.on_message(filters.command("yeet"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/yeet"
    re=requests.get(url).json()    
    yeet=re["url"]
    await msg.reply_video(yeet)

@app.on_message(filters.command("blush"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/blush"
    re=requests.get(url).json()    
    blush=re["url"]
    await msg.reply_video(blush)

@app.on_message(filters.command("smile"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/smile"
    re=requests.get(url).json()    
    smile=re["url"]
    await msg.reply_video(smile)

@app.on_message(filters.command("wave"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/wave"
    re=requests.get(url).json()    
    wave=re["url"]
    await msg.reply_video(wave)

@app.on_message(filters.command("highfive"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/highfive"
    re=requests.get(url).json()    
    highfive=re["url"]
    await msg.reply_video(highfive)


@app.on_message(filters.command("handhold"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/handhold"
    re=requests.get(url).json()    
    handhold=re["url"]
    await msg.reply_video(handhold)

@app.on_message(filters.command("nom"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/nom"
    re=requests.get(url).json()    
    nom=re["url"]
    await msg.reply_video(nom)

@app.on_message(filters.command("bite"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/bite"
    re=requests.get(url).json()    
    bite=re["url"]
    await msg.reply_video(bite)

@app.on_message(filters.command("glomp"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/glomp"
    re=requests.get(url).json()    
    glomp=re["url"]
    await msg.reply_video(glomp)

@app.on_message(filters.command("slap"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/slap"
    re=requests.get(url).json()    
    slap=re["url"]
    await msg.reply_video(slap)


@app.on_message(filters.command("kill"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/kill"
    re=requests.get(url).json()    
    kill=re["url"]
    await msg.reply_video(kill)


@app.on_message(filters.command("kick"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/kick"
    re=requests.get(url).json()    
    kick=re["url"]
    await msg.reply_video(kick)

@app.on_message(filters.command("happy"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/happy"
    re=requests.get(url).json()    
    happy=re["url"]
    await msg.reply_video(happy)

@app.on_message(filters.command("wink"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/wink"
    re=requests.get(url).json()    
    wink=re["url"]
    await msg.reply_video(wink)

@app.on_message(filters.command("poke"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/poke"
    re=requests.get(url).json()    
    poke=re["url"]
    await msg.reply_video(poke)

@app.on_message(filters.command("dance"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/dance"
    re=requests.get(url).json()    
    dance=re["url"]
    await msg.reply_video(dance)

@app.on_message(filters.command("cringe"))
async def waifu(_,msg):
    url="https://api.waifu.pics/sfw/cringe"
    re=requests.get(url).json()    
    cringe=re["url"]
    await msg.reply_video(cringe)


__help__="""
**⸢sᴏᴍᴇ ᴏғ ᴛʜᴇ ʙᴇsᴛ SFW ᴄᴏᴍᴍᴀɴᴅs ᴄʜᴇᴄᴋ ᴛʜᴇᴍ ᴏᴜᴛ⸥**

「𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦」 :
═───────◇───────═╗
๏ /neko                                    
๏ /waifu        
๏ /shinobu   
๏ /megumin 
๏ /bully          
๏ /cuddle      
๏ /cry             
๏ /hug            
๏ /awoo
๏ /kiss
๏ /lick
๏ /pat
๏ /smug
๏ /bonk
๏ /yeet
๏ /blush 
๏ /smile 
๏ /wave 
๏ /highfive 
๏ /handhold 
๏ /nom 
๏ /bite 
๏ /glomp 
๏ /slap 
๏ /kill 
๏ /kick 
๏ /happy 
๏ /wink 
๏ /poke 
๏ /dance                                 
๏ /cringe                                 
═───────◇───────═╝
"""
__mod_name__ = "𝚂ғᴡ"

