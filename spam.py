# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -
• `{i}spam <no of msgs> <your msg>`
    spams chat, the current limit for this is from 1 to 99.

• `{i}bigspam <no of msgs> <your msg>`
    Spams chat, the current limit is above 100.

• `{i}picspam <no of spam> <reply to media>`
    Spam media.

• `{i}delayspam <delay time> <count> <msg>`
    Spam chat.

"""

import asyncio
import os

from . import *


@ultroid_cmd(pattern="tspam")
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()


@ultroid_cmd(pattern="spam")
async def spammer(e):
    message = e.text
    if len(message) <= 5:
        return await eod(e, "`Use in Proper Format`")
    counter = int(message[6:8])
    spam_message = str(e.text[8:])
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    await e.delete()


@ultroid_cmd(pattern="bigspam")
async def bigspam(e):
    message = e.text
    try:
        counter = int(message[9:13])
    except (ValueError, IndexError):
        return await eod(e,
            "Invalid Input Given, or Value is below 101"
        )
    spam_message = str(e.text[13:])
    for _ in range(1, counter):
        await e.respond(spam_message)
    await e.delete()


@ultroid_cmd(pattern="picspam")
async def tiny_pic_spam(e):
    reply = await e.get_reply_message()
    text = e.text.split()
    counter = int(text[1])
    media = await e.client.download_media(reply)
    for _ in range(1, counter):
        await e.client.send_file(e.chat_id, media)
    os.remove(media)
    await e.delete()


@ultroid_cmd(pattern="delayspam ?(.*)")
async def delayspammer(e):
    try:
        args = e.text.split(" ", 3)
        delay = float(args[1])
        count = int(args[2])
        msg = str(args[3])
    except BaseException:
        return await e.edit(f"**Usage :** {HNDLR}delayspam <delay time> <count> <msg>")
    await e.delete()
    try:
        for _ in range(count):
            await e.respond(msg)
            await asyncio.sleep(delay)
    except Exception as u:
        await e.respond(f"**Error :** `{u}`")
