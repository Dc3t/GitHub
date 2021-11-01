import asyncio
from datetime import datetime

from telethon.tl import functions, types

from userbot import iqthon

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.utils import _format
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "utils"

LOGS = logging.getLogger(__name__)


class AFK:
    def __init__(self):
        self.USERAFK_ON = {}
        self.sql_time = None
        self.last_sql_message = {}
        self.sql_star = {}
        self.sql_end = {}
        self.reason = None
        self.msg_link = False
        self.sql_type = None
        self.media_afk = None
        self.sql_on = False


AFK_ = AFK()


@iqthon.iq_cmd(outgoing=True, edited=False)
async def set_not_sql(event):
    if AFK_.sql_on is False:
        return
    back_alive = datetime.now()
    AFK_.sql_end = back_alive.replace(microsecond=0)
    if AFK_.sql_star != {}:
        total_sql_time = AFK_.afk_end - AFK_.sql_star
        time = int(total_sql_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        elif h > 0:
            endtime += f"{h}h {m}m {s}s"
        else:
            endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message = event.message.message
    if (("sql" not in current_message) or ("#afk" not in current_message)) and (
        "on" in AFK_.USERAFK_ON
    ):
        shite = await event.client.send_message(
            event.chat_id,
            "`Back alive! No Longer afk.\nWas afk for " + endtime + "`",
        )
        AFK_.USERAFK_ON = {}
        AFK_.sql_time = None
        await asyncio.sleep(5)
        await shite.delete()
        AFK_.sql_on = False
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#AFKFALSE \n`Set AFK mode to False\n"
                + "Back alive! No Longer afk.\nWas afk for "
                + endtime
                + "`",
            )


@iqthon.iq_cmd(
    incoming=True, func=lambda e: bool(e.mentioned or e.is_private), edited=False
)
async def on_sql(event):  # sourcery no-metrics
    if AFK_.sql_on is False:
        return
    back_alivee = datetime.now()
    AFK_.sql_end = back_alivee.replace(microsecond=0)
    if AFK_.sql_star != {}:
        total_sql_time = AFK_.sql_end - AFK_.sql_star
        time = int(total_sql_time.seconds)
        d = time // (24 * 3600)
        time %= 24 * 3600
        h = time // 3600
        time %= 3600
        m = time // 60
        time %= 60
        s = time
        endtime = ""
        if d > 0:
            endtime += f"{d}d {h}h {m}m {s}s"
        elif h > 0:
            endtime += f"{h}h {m}m {s}s"
        else:
            endtime += f"{m}m {s}s" if m > 0 else f"{s}s"
    current_message_text = event.message.message.lower()
    if "sql" in current_message_text or "#afk" in current_message_text:
        return False
    if not await event.get_sender():
        return
    if AFK_.USERAFK_ON and not (await event.get_sender()).bot:
        msg = None
        if AFK_.sql_type == "media":
            if AFK_.reason:
                message_to_reply = (
                    f"**⌔︙ عذرا انا الان في وضعيه عدم الاتصال  👁‍🗨** .\n\n**⌔︙ وضع عدم الاتصال منذ 🕐 :** `{endtime}`"
                )
            else:
                message_to_reply = f"**⌔︙ عذرا انا الان في وضعيه عدم الاتصال  👁‍🗨** .\n\n**⌔︙ وضع عدم الاتصال منذ 🕐 :** `{endtime}`"
            if event.chat_id:
                msg = await event.reply(message_to_reply, file=AFK_.media_sql.media)
        elif AFK_.sql_type == "text":
            if AFK_.msg_link and AFK_.reason:
                message_to_reply = (
                    f"**⌔︙ عذرا انا الان في وضعيه عدم الاتصال  👁‍🗨** .\n\n**⌔︙ وضع عدم الاتصال منذ 🕐 :** `{endtime}`"
                )
            elif AFK_.reason:
                message_to_reply = (
                    f"**⌔︙ عذرا انا الان في وضعيه عدم الاتصال  👁‍🗨** .\n\n**⌔︙ وضع عدم الاتصال منذ 🕐 :** `{endtime}` "
                )
            else:
                message_to_reply = f"**⌔︙ عذرا انا الان في وضعيه عدم الاتصال  👁‍🗨** .\n\n**⌔︙ وضع عدم الاتصال منذ 🕐 :** `{endtime}`"
            if event.chat_id:
                msg = await event.reply(message_to_reply)
        if event.chat_id in AFK_.last_afk_message:
            await AFK_.last_sql_message[event.chat_id].delete()
        AFK_.last_sql_message[event.chat_id] = msg
        if event.is_private:
            return
        hmm = await event.get_chat()
        if Config.PM_LOGGER_GROUP_ID == -100:
            return
        full = None
        try:
            full = await event.client.get_entity(event.message.from_id)
        except Exception as e:
            LOGS.info(str(e))
        messaget = media_type(event)
        resalt = f"<b>⌔︙ المجموعات 🚻 : </b><code>{hmm.title}</code>"
        if full is not None:
            resalt += f"\n<b>⌔︙ مـن  ➡️ : </b> 👤{_format.htmlmentionuser(full.first_name , full.id)}"
        if messaget is not None:
            resalt += f"\n<b>⌔︙ الـرسالـة 📧 : </b><code>{messaget}</code>"
        else:
            resalt += f"\n<b>⌔︙ الـرسالـة 📧 : </b>{event.message.message}"
        resalt += f"\n<b>⌔︙ رابـط الـرسالـة 🔗  : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>"
        if not event.is_private:
            await event.client.send_message(
                Config.PM_LOGGER_GROUP_ID,
                resalt,
                parse_mode="html",
                link_preview=False,
            )


@iqthon.iq_cmd(
    pattern="وضع النائم(?:\s|$)([\s\S]*)",
    command=("وضع النائم", plugin_category),
    info={
        "header": "Enables afk for your account",
        "description": "When you are in afk if any one tags you then your bot will reply as he is offline.\
        AFK mean away from keyboard.",
        "options": "If you want AFK reason with hyperlink use [ ; ] after reason, then paste the media link.",
        "usage": [
            "{tr}afk <reason>",
            "{tr}afk <reason> ; <link>",
        ],
        "examples": "{tr}afk Let Me Sleep",
        "note": "Switches off AFK when you type back anything, anywhere. You can use #afk in message to continue in afk without breaking it",
    },
)
async def _(event):
    "To mark yourself as afk i.e. Away from keyboard"
    AFK_.USERAFK_ON = {}
    AFK_.sql_time = None
    AFK_.last_sql_message = {}
    AFK_.sql_end = {}
    AFK_.sql_type = "text"
    start_1 = datetime.now()
    AFK_.sql_on = True
    AFK_.sql_star = start_1.replace(microsecond=0)
    if not AFK_.USERAFK_ON:
        input_str = event.pattern_match.group(1)
        if ";" in input_str:
            msg, mlink = input_str.split(";", 1)
            AFK_.reason = f"[{msg.strip()}]({mlink.strip()})"
            AFK_.msg_link = True
        else:
            AFK_.reason = input_str
            AFK_.msg_link = False
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            AFK_.sql_time = datetime.now()
        AFK_.USERAFK_ON = f"on: {AFK_.reason}"
        if AFK_.reason:
            await edit_delete(
                event, f"⌔︙ عذرا انا الان في وضعيه عدم الاتصال يرجـى المراسلة لاحقـا بسـبب  {AFK_.reason} ✔️", 5
            )
        else:
            await edit_delete(event, f"**⌔︙ عذرا انا الان في وضعيه عدم الاتصال يرجـى المراسلة لاحقـا ✔️**", 5)
        if BOTLOG:
            if AFK_.reason:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"**⌔︙ وضع النائم 👁‍🗨 :** \n **تم تشغيل الوضع بسبب ✔️** {AFK_.reason}",
                )
            else:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"**⌔︙ وضع النائم 👁‍🗨 :** \n **تم تشغيل الوضع ✔️**",
                )


@iqthon.iq_cmd(
    pattern="mafk(?:\s|$)([\s\S]*)",
    command=("mafk", plugin_category),
    info={
        "header": "Enables afk for your account",
        "description": "When you are in afk if any one tags you then your bot will reply as he is offline.\
         AFK mean away from keyboard. Here it supports media unlike afk command",
        "options": "If you want AFK reason with hyperlink use [ ; ] after reason, then paste the media link.",
        "usage": [
            "{tr}mafk <reason> and reply to media",
        ],
        "examples": "{tr}mafk Let Me Sleep",
        "note": "Switches off AFK when you type back anything, anywhere. You can use #afk in message to continue in afk without breaking it",
    },
)
async def _(event):
    "To mark yourself as afk i.e. Away from keyboard (supports media)"
    reply = await event.get_reply_message()
    media_t = media_type(reply)
    if media_t == "Sticker" or not media_t:
        return await edit_or_reply(
            event, "`You haven't replied to any media to activate media afk`"
        )
    if not BOTLOG:
        return await edit_or_reply(
            event, "`To use media afk you need to set PRIVATE_GROUP_BOT_API_ID config`"
        )
    AFK_.USERAFK_ON = {}
    AFK_.sql_time = None
    AFK_.last_sql_message = {}
    AFK_.sql_end = {}
    AFK_.media_afk = None
    AFK_.sql_type = "media"
    start_1 = datetime.now()
    AFK_.sql_on = True
    AFK_.sql_star = start_1.replace(microsecond=0)
    if not AFK_.USERAFK_ON:
        input_str = event.pattern_match.group(1)
        AFK_.reason = input_str
        last_seen_status = await event.client(
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            AFK_.sql_time = datetime.now()
        AFK_.USERAFK_ON = f"on: {AFK_.reason}"
        if AFK_.reason:
            await edit_delete(
                event, f"`I shall be Going afk! because ~` {AFK_.reason}", 5
            )
        else:
            await edit_delete(event, f"`I shall be Going afk! `", 5)
        AFK_.media_sql = await reply.forward_to(BOTLOG_CHATID)
        if AFK_.reason:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#AFKTRUE \nSet AFK mode to True, and Reason is {AFK_.reason}",
            )
        else:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#AFKTRUE \nSet AFK mode to True, and Reason is Not Mentioned",
            )
