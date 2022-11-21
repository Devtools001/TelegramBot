from TeleBot import (
    pgram,
    LOG,
    updater,
    dispatcher
    )
from pyrogram import filters

@pgram.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_text("am started")

if __name__ == "__main__":
    LOG.info("started")
    pgram.run()

