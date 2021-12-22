from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.types import ChatBannedRights
from userbot import iqthon
from userbot.utils import admin_cmd, sudo_cmd, eor
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply


@iqthon.iq_cmd(pattern="nmtime ?(.*)")
async def set_time(e):
    if not e.pattern_match.group(1):
        return await edit_or_reply(e, get_string("nightm_1"))
    try:
        ok = e.text.split(maxsplit=1)[1].split()
        if len(ok) != 4:
            return await edit_or_reply(e, get_string("nightm_1"))
        tm = [int(x) for x in ok]
        udB.set("NIGHT_TIME", str(tm))
        await edit_or_reply(e, get_string("nightm_2"))
    except BaseException:
        await edit_or_reply(e, get_string("nightm_1"))


@iqthon.iq_cmd(pattern="addnm ?(.*)")
async def add_grp(e):
    pat = e.pattern_match.group(1)
    if pat:
        try:
            add_night((await ultroid_bot.get_entity(pat)).id)
            return await edit_or_reply(e, f"Done, Added {pat} To Night Mode.")
        except BaseException:
            return await edit_or_reply(e, get_string("nightm_5"), time=5)
    add_night(e.chat_id)
    await edit_or_reply(e, get_string("nightm_3"))


@iqthon.iq_cmd(pattern="remnm ?(.*)")
async def rem_grp(e):
    pat = e.pattern_match.group(1)
    if pat:
        try:
            rem_night((await ultroid_bot.get_entity(pat)).id)
            return await edit_or_reply(e, f"Done, Removed {pat} To Night Mode.")
        except BaseException:
            return await edit_or_reply(e, get_string("nightm_5"), time=5)
    rem_night(e.chat_id)
    await edit_or_reply(e, get_string("nightm_4"))


@iqthon.iq_cmd(pattern="listnm$")
async def rem_grp(e):
    chats = night_grps()
    name = "NightMode Groups Are-:\n\n"
    for x in chats:
        try:
            ok = await ultroid_bot.get_entity(x)
            name += "@" + ok.username if ok.username else ok.title
        except BaseException:
            name += str(x)
    await edit_or_reply(e, name)


async def open_grp():
    chats = night_grps()
    for chat in chats:
        try:
            await ultroid_bot(
                EditChatDefaultBannedRightsRequest(
                    chat,
                    banned_rights=ChatBannedRights(
                        until_date=None,
                        send_messages=False,
                        send_media=False,
                        send_stickers=False,
                        send_gifs=False,
                        send_games=False,
                        send_inline=False,
                        send_polls=False,
                    ),
                )
            )
            await ultroid_bot.send_message(chat, "**NightMode Off**\n\nGroup Opened 🥳.")
        except Exception as er:
            LOGS.info(er)


async def close_grp():
    chats = night_grps()
    h1, m1, h2, m2 = 0, 0, 7, 0
    if udB.get("NIGHT_TIME"):
        h1, m1, h2, m2 = eval(udB["NIGHT_TIME"])
    for chat in chats:
        try:
            await ultroid_bot(
                EditChatDefaultBannedRightsRequest(
                    chat,
                    banned_rights=ChatBannedRights(
                        until_date=None,
                        send_messages=True,
                    ),
                )
            )
            await ultroid_bot.send_message(
                chat, f"**NightMode : Group Closed**\n\nGroup Will Open At `{h2}:{m2}`"
            )
        except Exception as er:
            LOGS.info(er)


if night_grps():
    try:
        h1, m1, h2, m2 = 0, 0, 7, 0
        if udB.get("NIGHT_TIME"):
            h1, m1, h2, m2 = eval(udB["NIGHT_TIME"])
        sch = AsyncIOScheduler()
        sch.add_job(close_grp, trigger="cron", hour=h1, minute=m1)
        sch.add_job(open_grp, trigger="cron", hour=h2, minute=m2)
        sch.start()
    except Exception as er:
        LOGS.info(er)
