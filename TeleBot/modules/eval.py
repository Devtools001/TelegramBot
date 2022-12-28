import io
from re import sub
import sys
import traceback
from TeleBot import pgram as app
#from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import RPCError
import subprocess
from datetime import datetime
from pyrogram import filters, enums

DEV_USERS = [5459540851]

@app.on_message(filters.command(["shell", "sh"]))
@app.on_edited_message(
    filters.command(["shell", "sh"]))
async def shell(_, m):
    cmd = m.text.split(" ", 1)
    if len(cmd) == 1:
        return await m.reply("No command to execute was given.")
    shell = (await shell_exec(cmd[1]))[0]
    if len(shell) > 3000:
        with open("shell_output.txt", "w") as file:
            file.write(shell)
        with open("shell_output.txt", "rb") as doc:
            await m.reply_document(document=doc, file_name=doc.name)
            try:
                os.remove("shell_output.txt")
            except:
                pass
    elif len(shell) != 0:
        await m.reply(shell, parse_mode=enums.ParseMode.HTML)
    else:
        await m.reply("No Reply")


@app.on_message(filters.command(["ev", "run"]))
@app.on_edited_message(filters.command(["ev", "run"]))
async def evaluation_cmd_t(_, m):
    status_message = await m.reply("__Processing eval pyrogram...__")
    try:
        cmd = m.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await status_message.edit("__No evaluate message!__")

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, _, m)
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

    final_output = f"**EVAL**:\n`{cmd}`\n\n**OUTPUT**:\n`{evaluation.strip()}`\n"

    if len(final_output) > 4096:
        with open("MissKatyEval.txt", "w+", encoding="utf8") as out_file:
            out_file.write(final_output)
        await status_message.reply_document(
            document="MissKatyEval.txt",
            caption=f"<code>{cmd[: 4096 // 4 - 1]}</code>",
            disable_notification=True,
        )
        os.remove("MissKatyEval.txt")
        await status_message.delete()
    else:
        await status_message.edit(final_output, parse_mode=enums.ParseMode.MARKDOWN)


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "\n p = print"
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def shell_exec(code, treat=True):
    process = await asyncio.create_subprocess_shell(
        code, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT
    )

    stdout = (await process.communicate())[0]
    if treat:
        stdout = stdout.decode().strip()
    return stdout, process
