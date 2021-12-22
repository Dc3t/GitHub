from userbot import iqthon
from userbot.utils import admin_cmd, sudo_cmd, eor
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.bot_pms_sql import (
    add_user_to_db,
    get_user_id,
    get_user_logging,
    get_user_reply,
)

@iqthon.iq_cmd("dm", fullsudo=True)
async def dm(e):
    if len(e.text) > 3 and e.text[3] != " ":  # weird fix
        return
    if len(e.text.split()) <= 1:
        return await eor(e, get_string("dm_1"), time=5)
    chat = e.text.split()[1]
    try:
        chat_id = await get_user_id(chat)
    except Exception as ex:
        return await eor(e, f"`{ex}`", time=5)
    if e.reply_to:
        msg = await e.get_reply_message()
    elif len(e.text.split()) > 2:
        msg = e.text.split(maxsplit=2)[2]
    else:
        return await eor(e, get_string("dm_2"), time=5)
    try:
        await e.client.send_message(chat_id, msg)
        await eor(e, get_string("dm_3"), time=5)
    except Exception as m:
        await eor(e, get_string("dm_4").format(m, HNDLR), time=5)


@iqthon.iq_cmd(fwdreply ?(.*)", fullsudo=True)
async def _(e):
    message = e.pattern_match.group(1)
    if not e.reply_to_msg_id:
        return await eor(e, get_string("ex_1"), time=5)
    if not message:
        return await eor(e, get_string("dm_6"), time=5)
    msg = await e.get_reply_message()
    fwd = await msg.forward_to(msg.sender_id)
    await fwd.reply(message)
    await eor(e, get_string("dm_5"), time=5)


@iqthon.iq_cmd(pattern="save$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(
            e, "Reply to Any Message to save it to ur saved messages", time=5
        )
    if e.out:
        await e.client.send_message("me", x)
    else:
        await e.client.send_message(e.sender_id, x)
    await eor(e, "Message saved to Your Pm/Saved Messages.", time=5)


@iqthon.iq_cmd(pattern="fsave$")
async def saf(e):
    x = await e.get_reply_message()
    if not x:
        return await eod(
            e, "Reply to Any Message to save it to ur saved messages", time=5
        )
    if e.out:
        await x.forward_to("me")
    else:
        await x.forward_to(e.sender_id)
    await eor(e, "Message saved to Your Pm/Saved Messages.", time=5)
