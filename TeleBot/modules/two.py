import io
from re import sub
import sys
import traceback
from TeleBot import pgram as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import RPCError
import subprocess

DEV_USERS = [5696053228,5459540851]

@app.on_message(filters.command("eval"))
async def eval(client, message):
    if message.from_user.id not in DEV_USERS:
        await message.reply_text("you r not dev of the bot")
    else:
        status_message = await message.reply_text("Processing ...")
        try:
            cmd = message.text.split(" ", maxsplit=1)[1]
        except IndexError:
            return await message.delete()
        reply_to_ = message
        if message.reply_to_message:
            reply_to_ = message.reply_to_message

        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None

        try:
            await aexec(cmd, client, message)
        except Exception:
            exc = traceback.format_exc()

        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"

        final_output = "<b>EVAL</b>: "
        final_output += f"<code>{cmd}</code>\n\n"
        final_output += "<b>OUTPUT</b>:\n"
        final_output += f"<code>{evaluation.strip()}</code> \n"

        if len(final_output) > 4096:
            with io.BytesIO(str.encode(final_output)) as out_file:
                out_file.name = "eval.text"
                await reply_to_.reply_document(document=out_file,
                                           caption=cmd,
                                           disable_notification=True)
        else:
            await reply_to_.reply_text(final_output)
        await status_message.delete()


async def aexec(code, client, message):
    exec("async def __aexec(client, message): " +
         "".join(f"\n {l_}" for l_ in code.split("\n")))
    return await locals()["__aexec"](client, message)
