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
