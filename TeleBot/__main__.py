from TeleBot import pgram
from pyrogram import filters

@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_text("am started")

if __name__ == "__main__":
    LOG.info("started")
    app.run()

