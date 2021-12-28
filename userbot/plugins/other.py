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
osfle = [  "〔 لا خلقۿ ولا اخلاق لحاله عايش ☹️. 〕","〔 سڪر محلي محطوط على ڪريما 🤤🍰. 〕","〔 ؏ـسل × ؏ـسل 🍯. 〕","〔 أنسان مرتب وڪشاخ بس مشكلتۿ يجذب هواي 😂. 〕","〔 ملڪ جمال ألعالم 🥺💘. 〕","〔 أنسان زباله ومكضيها نوم 🙂. 〕","〔 يعني بشرفك هوه هذا يستاهل اوصفه؟ 〕","〔 أنسان ڪيمر 😞💘. 〕","〔 جنۿ جڪليته يربيـﮧ 🍬. 〕","〔 شمأ اوصف بي قليل 🥵💞. 〕","〔 وجۿا جنة كاهي من ألصبحـﮧ ☹️♥️. 〕","〔 هذا واحد يهودي دير بالك منه 🙂💘. 〕","〔 هذا انسان يحب مقتدئ ابتعد عنه 😂💞. 〕","〔 بس تزحف ع الولد وهيه زرڪة 😂. 〕","〔 جنۿ مرڪة شجر شبيك يول 😂😔. 〕","〔 هذا حبيبي ، أحبة ڪولش 🙊💘 〕","〔 جمالهـﮧ خبلني 😞💞. 〕","〔 چنۿ ڪريمة ؏ـلى ڪيك 😞💘. 〕","〔 انسان مينطاق 🙂💔. 〕","〔 فد أنسان مرتب وريحتة تخبل 🥺💞 〕","〔 شڪد حلو هذا ومؤدب 😭💞💘💕. 〕","〔 وفف مو بشر ضيم لضيعه من ايدڪك نصيحة 🥺💞. 〕","〔 نتا مخلوق من ڪتله مال عارية 🙂😂. 〕","〔 لضيعۿ من أيدك خوش أنسانن وحباب رتبط بي احسلڪك 🥺. 〕","〔 با؏ هذا الصاڪك يربي شنو مخلوق منعسل 🥺🧿. 〕","〔 شني عمي مو بشر ڪيك ورب 🥺💞. 〕","〔 عوفه ضلعي هذا انسان زباله 🙂😂. 〕","〔 انسان ساقط لتحجي وياه انطي بلوڪك بدون تفاهم 🙂🤦‍♀️. 〕","〔 باع منو شون بشر هوه وجۿا يطرد النعمة 🙂. 〕","〔 عيع فد أنسان وصخ 😂♥️. 〕","〔 يول هذا طاڪك قطة احسلك 😂💞. 〕","〔 لازم واحد يضمه بقوطيه ويقفل عليه لان هالبشر ڪيك 🤤💘. 〕","〔 هذا الله غاضب عليه 🌚💔. 〕","〔 شنو شنو ؟ تسرسح يله 😒💘. 〕","〔 وردة مال الله ، فدوا اروحله 🤤💞. 〕"," أنسان مؤدب من البيت للجامع ، ومن الجامع للبيت 😞💞. 〕","〔 انسان بومة وبس نايم مدري شلون اهله ساكتيله 🌚💞. 〕","〔 أنت شايف وجها من يكعد الصبح ؟ عمي خلينا ساكتين 🙂😂. 〕","〔 الله وكيلك هذا اهله كلشي ممستافدين من عنده 🥲💞. 〕","〔 لكشنو من جمالل هذا يربييييي 😭💞. 〕","〔 يومة فديته جنه زربه 😭😂💞. 〕",]

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
    await edit_or_reply(mention, f"هذا  [{iqth}](tg://user?id={user.id}) {iqt} ")
