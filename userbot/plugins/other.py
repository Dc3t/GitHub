import asyncio
import random
import pyfiglet
import re
import requests
from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError
from cowpy import cow
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins, MessageEntityMentionName
from time import sleep
from datetime import datetime
from telethon import Button, events
from telethon.events import CallbackQuery
from telethon.utils import get_display_name
from collections import deque
from random import choice
from userbot import iqthon
from ..helpers import catmemes
from ..core.managers import edit_or_reply, edit_delete
from . import ALIVE_NAME
from ..helpers import fonts as emojify
from ..helpers.utils import reply_id, _catutils, parse_pre, yaml_format, install_pip, get_user_from_event, _format
from . import deEmojify
from ..helpers import get_user_from_event
plugin_category = "fun"
from userbot.utils import admin_cmd, sudo_cmd, eor
from ..sql_helper.bot_pms_sql import add_user_to_db,    get_user_id,    get_user_logging,    get_user_reply

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
osfle = [  "   ـ 〔 لا خلقۿ ولا اخلاق لحاله عايش ☹️. 〕",
"   ـ 〔 سڪر محلي محطوط على ڪريما 🤤🍰. 〕",
"   ـ 〔 ؏ـسل × ؏ـسل 🍯. 〕",
"   ـ 〔 أنسان مرتب وڪشاخ بس مشكلتۿ يجذب هواي 😂. 〕",
"   ـ 〔 ملڪ جمال ألعالم 🥺💘. 〕",
"   ـ 〔 أنسان زباله ومكضيها نوم 🙂. 〕",
"   ـ 〔 يعني بشرفك هوه هذا يستاهل اوصفه؟ 〕",
"   ـ 〔 أنسان ڪيمر 😞💘. 〕",
"   ـ 〔 جنۿ جڪليته يربيـﮧ 🍬. 〕",
"   ـ 〔 شمأ اوصف بي قليل 🥵💞. 〕",
"   ـ 〔 وجۿا جنة كاهي من ألصبحـﮧ ☹️♥️. 〕",
"   ـ 〔 هذا واحد يهودي دير بالك منه 🙂💘. 〕",
"   ـ 〔 هذا انسان يحب مقتدئ ابتعد عنه 😂💞. 〕",
"   ـ 〔 بس تزحف ع الولد وهيه زرڪة 😂. 〕",
"   ـ 〔 جنۿ مرڪة شجر شبيك يول 😂😔. 〕",
"   ـ 〔 هذا حبيبي ، أحبة ڪولش 🙊💘 〕",
"   ـ 〔 جمالهـﮧ خبلني 😞💞. 〕",
"   ـ 〔 چنۿ ڪريمة ؏ـلى ڪيك 😞💘. 〕",
"   ـ 〔 انسان مينطاق 🙂💔. 〕",
"   ـ 〔 فد أنسان مرتب وريحتة تخبل 🥺💞 〕",
"   ـ 〔 شڪد حلو هذا ومؤدب 😭💞💘💕. 〕",
"   ـ 〔 وفف مو بشر ضيم لضيعه من ايدڪك نصيحة 🥺💞. 〕",
"   ـ 〔 نتا مخلوق من ڪتله مال عارية 🙂😂. 〕",
"   ـ 〔 لضيعۿ من أيدك خوش أنسانن وحباب رتبط بي احسلڪك 🥺. 〕",
"   ـ 〔 با؏ هذا الصاڪك يربي شنو مخلوق منعسل 🥺🧿. 〕",
"   ـ 〔 شني عمي مو بشر ڪيك ورب 🥺💞. 〕",
"   ـ 〔 عوفه ضلعي هذا انسان زباله 🙂😂. 〕",
"   ـ 〔 انسان ساقط لتحجي وياه انطي بلوڪك بدون تفاهم 🙂🤦‍♀️. 〕",
"   ـ 〔 باع منو شون بشر هوه وجۿا يطرد النعمة 🙂. 〕",
"   ـ 〔 عيع فد أنسان وصخ 😂♥️. 〕",
"   ـ 〔 يول هذا طاڪك قطة احسلك 😂💞. 〕",
"   ـ 〔 لازم واحد يضمه بقوطيه ويقفل عليه لان هالبشر ڪيك 🤤💘. 〕",
"   ـ 〔 هذا الله غاضب عليه 🌚💔. 〕",
"   ـ 〔 شنو شنو ؟ تسرسح يله 😒💘. 〕",
"   ـ 〔 وردة مال الله ، فدوا اروحله 🤤💞. 〕",
"   ـ 〔 أنسان مؤدب من البيت للجامع ، ومن الجامع للبيت 😞💞. 〕",
"   ـ 〔 انسان بومة وبس نايم مدري شلون اهله ساكتيله 🌚💞. 〕",
"   ـ 〔 أنت شايف وجها من يكعد الصبح ؟ عمي خلينا ساكتين 🙂😂. 〕",
"   ـ 〔 الله وكيلك هذا اهله كلشي ممستافدين من عنده 🥲💞. 〕",
"   ـ 〔 لكشنو من جمالل هذا يربييييي 😭💞. 〕",
"   ـ 〔 يومة فديته جنه زربه 😭😂💞. 〕",]

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

@iqthon.on(admin_cmd(pattern="اوصفلي(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 1226408155:
        return await edit_or_reply(mention, f"**- تاج راسك  هذا مبرمج السورس  **")
    iqth = user.first_name.replace("\u2060", "") if user.first_name else user.username
    iqt = random.choice(osfle)
    await edit_or_reply(mention, f"هذا [{iqth}](tg://user?id={user.id})  {iqt} ")
