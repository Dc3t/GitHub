# ملف تعبان عليه والفكره هم بستر عرضك لاتاخذه ابو الغيره
import time
import json
import math
import os
import random
import re
from telethon import Button, events, types
from userbot import iqthon
from SQL.extras import *
from ..Config import Config 
# ها راح تاخذه مو ولك ليش 
from telethon.events import CallbackQuery, InlineQuery
from telethon.errors import QueryIdInvalidError
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, mention, BOTLOG, BOTLOG_CHATID, HEROKU_APP 
# عرفتك كواد والله  
IQTHONPC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/9fa2824990eb9d80adcea.jpg"
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None # ذمه برقبتك اذا تاخذ سطر واحد او تاخذ الفكره تعبي لاتخمطه ولاتاخذ افكاري بس الفاشل يسويها الى يوم القيامه
        query = iqthon.text
        await bot.get_me() # بشرفك عوفه  
        if query.startswith("تنصيب") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.url("1- شرح التنصيب", "https://youtu.be/44tYK_yV02Q"), Button.url("2- استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("3- ستخراج تيرمكس", "https://replit.com/@telethon-Arab/generatestringsession#start.sh"), Button.url("4- بوت فاذر", "http://t.me/BotFather"),],[Button.url("5- رابط التنصيب", "https://dashboard.heroku.com/new?template=https://github.com/telethon-Arab/telethohelp"),],[Button.url("المطـور 👨🏼‍💻", "https://t.me/LLL5L"),]]
            if IQTHONPC and IQTHONPC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(IQTHONPC, text=help1, buttons=buttons, link_preview=False)
            elif IQTHONPC:
                result = builder.document(IQTHONPC,title="iqthon",text=help1,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="iqthon",text=help1,buttons=buttons,link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="تنصيب"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return # ذمه برقبتك اذا تاخذ سطر واحد او تاخذ الفكره تعبي لاتخمطه ولاتاخذ افكاري بس الفاشل يسويها الى يوم القيامه
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "تنصيب")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete() # متكلي شعندك عوفه بابه
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("^/orders$") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر السورس", data="order1"),],[Button.inline("𝟑 اوامر الحساب", data="order12"), Button.inline("𝟐 اوامر الحساب", data="order3"), Button.inline("𝟏 اوامر الحساب", data="order2"),],[Button.inline("𝟑 اوامر الكروب", data="order11"), Button.inline("𝟐 اوامر الكروب", data="order5"), Button.inline("𝟏 اوامر الكروب", data="order4"),],[Button.inline("𝟐 اوامر الالعاب", data="order7"), Button.inline("𝟏 اوامر الالعاب", data="order6"),],[Button.inline("𝟐 اوامر الصيغ", data="order9"), Button.inline("𝟏 اوامر الصيغ", data="order8"),],[Button.inline("اوامر الاغاني", data="order10"), Button.inline("اوامر الوقتي", data="order13"),],[Button.inline("اوامر التسليه", data="order14"),],[Button.inline("𝟐 الفارات", data="order16"), Button.inline("𝟏 الفارات", data="order15"),]]
            if IQTHONPC and IQTHONPC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(IQTHONPC, text=help2, buttons=buttons, link_preview=False)
            elif IQTHONPC:
                result = builder.document(IQTHONPC,title="iqthon",text=help2,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="iqthon",text=help2,buttons=buttons,link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="^/orders$"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return 
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "^/orders$")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("(امور|اوامر|الاوامر|الأوامر)") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.inline("اوامر السورس", data="order1"),],[Button.inline("𝟑 اوامر الحساب", data="order12"), Button.inline("𝟐 اوامر الحساب", data="order3"), Button.inline("𝟏 اوامر الحساب", data="order2"),],[Button.inline("𝟑 اوامر الكروب", data="order11"), Button.inline("𝟐 اوامر الكروب", data="order5"), Button.inline("𝟏 اوامر الكروب", data="order4"),],[Button.inline("𝟐 اوامر الالعاب", data="order7"), Button.inline("𝟏 اوامر الالعاب", data="order6"),],[Button.inline("𝟐 اوامر الصيغ", data="order9"), Button.inline("𝟏 اوامر الصيغ", data="order8"),],[Button.inline("اوامر الاغاني", data="order10"), Button.inline("اوامر الوقتي", data="order13"),],[Button.inline("اوامر التسليه", data="order14"),],[Button.inline("𝟐 الفارات", data="order16"), Button.inline("𝟏 الفارات", data="order15"),]]
            if IQTHONPC and IQTHONPC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(IQTHONPC, text=help2, buttons=buttons, link_preview=False)
            elif IQTHONPC:
                result = builder.document(IQTHONPC,title="iqthon",text=help2,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="iqthon",text=help2,buttons=buttons,link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="(امور|اوامر|الاوامر|الأوامر)"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return # ذمه برقبتك اذا تاخذ سطر واحد او تاخذ الفكره تعبي لاتخمطه ولاتاخذ افكاري بس الفاشل يسويها الى يوم القيامه
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "(امور|اوامر|الاوامر|الأوامر)")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order1")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر السورس   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴ ⦙ `.السورس` \n**✐  : يضهر لك معلومات السورس ومدة تنصيبك❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑵ ⦙ `.رابط التنصيب` \n**✐  : سوف يعطيك رابط التنصيب ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮  \n⑶ ⦙ `.حساب كيثاب + اسم الحساب` \n**✐  : ينطيك معلومات الحساب وسورساته بموقع جيت هوب ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑷ ⦙ `.حذف جميع الملفات` \n**✐  : يحذف جميع ملفات تنصيبك ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸ ⦙ `.المده` \n**✐  : يضهر لك مدة تشغيل بوت تليثون لديك ❝** \n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.فارات تنصيبي` \n**✐  : يجلب لك جميع الفارات التي لديك وجميع معلومات تنصيبك في هيروكو ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.تحميل ملف + الرد ع الملف`\n**✐ : يحمل ملفات تليثون ❝**\n\n⑻ ⦙  `.مسح ملف + الرد ع الملف` \n**✐ :  يمسح الملف الي حملته  ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑼ ⦙  `.تحديث` \n**✐ :  امر لأعاده التشغيل وتحديث ملفات السورس وتسريع التليثون  ❝**\n\n⑽ ⦙ `.اطفاء مؤقت + عدد الثواني`\n**✐ : يقوم بأطفاء التليثون بعدد الثواني الي ضفتها  عندما تخلص الثواني سيتم اعاده تشغيل التليثون ❝**\n⤪⟿⟿⟿⟿⤮\n\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order2")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الحساب 1   ⦒  :** \n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙ `.معرفه + الرد ع الشخص` \n**✐ : سيجلب لك معرف الشخص ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑵  ⦙ `.سجل الاسماء + الرد ع الشخص` \n**✐ : يجلب لك اسماء الشخص القديمه ❝** \n ⑶  ⦙ `.انشاء بريد` \n**✐ : ينشئ لك بريد وهمي مع رابط رسائل التي تأتي الى البريد ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑷  ⦙ `.ايدي + الرد ع الشخص` \n**✐ : سيعطيك معلومات الشخص ❝** \n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `. الايدي الرد ع الشخص` \n**✐ : سوف يعطيك ايدي المجموعه او ايدي حسابك ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.معلومات تخزين المجموعه` \n**✐ : يجلب لك جميع معلومات الوسائط والمساحه وعدد ملصقات وعدد تخزين ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑺ ⦙ `.تخزين الخاص تشغيل`\n**✐ : يجلب لك جميع الرسائل التي تأتي اليك في الخاص ❝**\n⑻ ⦙ . تخزين الخاص ايقاف \n✐ : يوقف ارسال جميع الرسائل التي تأتي اليك في الخاص ❝\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n⑼ ⦙ .تخزين الكروبات تشغيل\n✐ : يرسل لك جميع الرسائل التي يتم رد عليها في رسالتك في الكروبات ❝\n⑽ ⦙ .تخزين الكروبات ايقاف\n✐ : يوقف لك جميع ارسال الرسائل التي يتم رد عليها ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order3")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الحساب 2   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙  `.صورته + الرد ع الشخص`\n**✐ : يجلب صوره الشخص الذي تم رد عليه ❝**\n \n⑵  ⦙ `.رابطه + الرد ع الشخص`\n**✐ :  يجلب لك رابط الشخص الذي تم رد عليه  ❝**\n\n⑶  ⦙ `.اسمه + الرد ع الشخص`\n**✐ : يجلب لك اسم الشخص الذي تم رد عليه ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑷  ⦙  `.نسخ + الرد ع الرساله`\n**✐ : يرسل الرساله التي تم رد عليها ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.كورونا + اسم المدينه`\n**✐ : يجلب لك مرض كورونا وعدد الموتى والمصابين**❝\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.الاذان +اسم المدينه`\n**✐ : يجلب لك معلومات الاذان في هذهّ المدينه بجميع الاوقات ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.رابط تطبيق + اسم التطبيق`\n**✐ : يرسل لك رابط التطبيق مع معلوماته ❝**\n\n⑻ ⦙ `.تاريخ الرساله + الرد ع الرساله`\n**✐ : يجلب لك تاريخ الرساله بالتفصيل ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑼ ⦙ `.بنك`\n**✐ : يقيس سرعه استجابه لدى تنصيبك ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑽ ⦙ `.سرعه الانترنيت`\n**✐ : يجلب لك سرعه الانترنيت لديك ❝**\n\n⑾ ⦙ `.الوقت`\n**✐ : يضهر لك الوقت والتاريخ واليوم ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑿ ⦙  `.وقتي`\n**✐ : يضهر لك الوقت والتاريخ بشكل جديد ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order4")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  اوامر الكروب 1     ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙ `.كتم + الرد ع الشخص`\n**✐ : يكتم الشخص من الخاص او الكروبات فقط اذا كانت عندك صلاحيه حذف رسائل ❝**\n \n⑵  ⦙ `. الغاء كتم + الرد ع الشخص`\n**✐ :  يجلب لك جميع معرفات المشرفين في الكروب  ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑶  ⦙ `.البوتات`\n**✐ : يجلب لك جميع معرفات البوتات في الكروب ❝**\n \n⑷  ⦙ `.الأعضاء`\n**✐ : اضهار قائمة الاعضاء للكروب اذا هواي سيرسل ملف كامل لمعلوماتهم  ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.معلومات`\n**✐ : سيرسل لك جميع معلومات الكروب بالتفصيل ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.مسح المحظورين`\n**✐ : يمسح جميع المحظورين في الكروب ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.المحذوفين`\n**✐ : يجلب لك جميع الحسابات المحذوفه ❝**\n\n⑻ ⦙ `.المحذوفين تنظيف`\n**✐ : يمسح جميع الحسابات المحذوفه في الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑼ ⦙ `.احصائيات الاعضاء`\n**✐ : يمسح جميع المحظورين في الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑽ ⦙ `.انتحال + الرد ع الشخص`\n**✐ : يقوم بأنتحال الشخص ويضع صورته ونبذته واسمه في حسابك عدا المعرف ❝**\n\n⑾ ⦙ `.الغاء الانتحال + الرد ع الشخص`\n**✐ : يقوم بألغاء الانتحال وسيرجع معلومات المذكوره بالسورس ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order5")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الكروب 2   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑴  ⦙  `.ترحيب + الرساله` \n**✐ : يضيف ترحيب في الكروب اي شخص ينضم راح يرحب بي  ❝**\n⑵  ⦙   `.مسح الترحيبات` \n**✐ :  ييقوم بمسح الترحيب من الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n  ⦙  `.ترحيباتي` \n**✐ :  يضهر لك جميع الترحيبات التي وضعتها في الكروب ❝**\n⑷  ⦙ `.رساله الترحيب السابقه تشغيل`  \n**✐ :  عندما يحدث تكرار سيحذف رساله الترحيب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙  `.رساله الترحيب السابقه ايقاف`\n**✐ :  عندما يحدث تكرار لا يحذف رساله الترحيب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙  `.اضف رد + الكلمه` \n**✐ :  مثلاً تدز رساله هلو تسوي عليها رد بهلوات ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.مسح رد + الكلمه` \n**✐ :  سيحذف الكلمه الي انت ضفتها ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n⑻ ⦙  `.جميع الردود` \n **✐ :  يجلب لك جميع الردود الذي قمت بأضافتها  ❝**\n⑼ ⦙  `.مسح جميع الردود` \n**✐ :  يمسح جميع الردود الي انت ضفتها ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑽ ⦙  `.صنع مجموعه + اسم المجموعه`\n**✐ : يقوم بعمل مجموعه خارقه ❝**\n \n⑾ ⦙  `.صنع قناه +  اسم القناة`\n**✐ : يقوم بعمل قناه خاصه  ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑿ ⦙ `.عدد رسائلي`\n**✐ : سيظهر لك عدد رسائلك في الكروب ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order6")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الالعاب والكلمات 1   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n**⑴  ⦙  نسب وهميه :**\n`.نسبه الحب + الرد ع الشخص`\n`. نسبه الانحراف + الرد ع الشخص `\n`.نسبه الكراهيه + الرد ع الشخص`\n`.نسبه المثليه +الرد ع الشخص`\n`. نسبه النجاح + الرد ع الشخص`\n`.نسبه الانوثه + الرد ع الشخص `\n`.نسبه الغباء + الرد ع الشخص`\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n**⑵  ⦙  رفع وهمي :**\n`.رفع زباله + الرد ع الشخص `\n`.رفع منشئ + الرد ع الشخص `\n`.رفع مدير + الرد ع الشخص`\n`.رفع مطور + الرد ع الشخص` \n`.رفع مثلي + الرد ع الشخص` \n`.رفع كواد + الرد ع الشخص` \n`.رفع مرتبط + الرد ع الشخص` \n`.رفع مطي + الرد ع الشخص` \n`.رفع كحبه + الرد ع الشخص` \n`.رفع زوجتي + الرد ع الشخص` \n`.رفع صاك + الرد ع الشخص` \n`.رفع صاكه + الرد ع الشخص`\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑶  ⦙ `.كت`\n**✐ : لعبه اسأله كت تويت عشوائيه ❝**\n⑷  ⦙ `.اكس او` \n**✐ :  لعبه اكس او دز الامر و اللعب ويا صديقك ❝**\n⑸  ⦙  `.همسه + الكلام + معرف الشخص` \n**✐ : يرسل همسه سريه الى معرف الشخص فقط هو يكدر يشوفها  ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order7")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الالعاب والكلمات 2   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n**⑻ ⦙ `.رسم شعار + الاسم` \n**✐ : يرسم شعار للأسم  ❝**\n⑼ ⦙ `.نص ثري دي + الكلمه`\n**✐ : يقوم بكتابه الكلمه بشكل ثلاثي الابعاد~  ❝**\n⑽ ⦙ `.كلام متحرك + الكلام`\n**✐ : يقوم بكتابه الكلام حرف حرف  ❝**\n⑾  ⦙  `.ملصق متحرك + الكلام`\n**✐ : يقوم بكتابه الكلام بملصق متحرك  ❝**\n⑿ ⦙  `.بورن + معرف الشخص + الكلام + الرد ع اي صوره`\n**✐ :  قم بتجربه الامر لتعرفه +18  ❝**\n⒀ ⦙ `.رسم قلوب + الاسم`\n**✐ : يكتب الاسم ع شكل قلوب  ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order8")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  1 اوامر تحويل الصيغ  ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑴  ⦙  `.تحويل بصمه + الرد ع الصوت mp3`\n**✐ : يحول صوت mp3 الى بصمه ❝**\n⑵  ⦙  `.تحويل صوت + الرد ع الصوت` \n**✐ :  يحول البصمه الى صوت   mp3**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑶  ⦙  `.تحويل ملصق + الرد ع الصوره` \n**✐ :  يحول الصوره الى ملصق ❝**\n⑷  ⦙ `. تحويل صوره + الرد ع الملصق` \n**✐ :  يحول الملصق الى صوره ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙  `.تحويل متحركه + الرد ع الفيديو` \n**✐ :  يقوم بتحويل الفيديو الى متحركه ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙  `.بي دي اف + الرد ع الملف او الصوره`\n**✐ :  يحول الملف او الصوره الى بي دي اف ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.ملصقي + الرد ع الرساله` \n**✐ : يحول رساله الى ملصق ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑻ ⦙  `. تليجراف ميديا + الرد ع الفيديو او صوره`\n **✐ :  يقوم بتحويل الفيديو او الصوره الى رابط تليجراف للأستخدام  ❝**\n⑼ ⦙  `.تحويل رساله + الرد ع الملف` \n**✐ :  يقوم بجلب جميع الكتابه الذي داخل الملف ويقوم بأرسالها اليك ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑽ ⦙ `.تحويل فديو دائري + الرد ع الفيديو`\n**✐ : يحول الفيديو الى فيديو دائري مرئي ❝**\n⑾  ⦙ `.تحويل ملصق دائري + الرد ع الملصق` \n**✐ :  يحول الملصق الى ملصق دائري** \n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order9")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  2 اوامر تحويل الصيغ   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑿ ⦙  `.ترجمه en + الرد ع الرساله` \n**✐ :  يقوم بترجمه الرساله الى اللغه الانكليزيه**\n⒀ ⦙ `.ترجمه ar + الرد ع الشخص` \n**✐ :  يقوم بترجمه الرساله الى اللغه العربيه ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order10")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر التنزيلات والبحث الاغاني ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙ `.بحث صوت + اسم الاغنيه`\n**✐ : سيحمل لك الاغنية صوت ايضا يمكنك وضع رابط الاغنيه بدل الاسم ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑵  ⦙ `.بحث فيديو + اسم الاغنيه` \n**✐ : سيحمل لك الاغنية  فيديو ايضا يمكنك وضع رابط الاغنيه بدل الاسم ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n ⑶  ⦙ `.معلومات الاغنيه` \n**✐ : الرد ع الاغنيه سيجلب لك معلوماتها واسم الفنان ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n \n⑷  ⦙ `.كوكل بحث + موضوع البحث`\n**✐ : يجلب لك معلومات الموضوع من كوكل ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.تخزين الصوت + الرد ع البصمه`\n**✐ : تخزين الصوت من اجل استخدامه لوضع صوت في الفيديو ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.اضف الصوت + الرد ع الصوره او متحركه او فيديو`\n**✐ : يتم اضافه الصوت الى الفيديو او المتحركه او الصوره ❝**\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.اسم الاغنيه + الرد ع الاغنيه`\n**✐ : ييجلب لك اسم الاغنيه مدة البصمه 10 الى 5 ثواني ❝**\n⑻ ⦙ `تيك توك + الرد ع رابط الفيديو.`\n**✐ : يحمل فيديو تيك توك بدون العلامه المائيه** ❝\n ⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inlineiqthon(iqthon):
        builder = iqthon.builder
        result = None
        query = iqthon.text
        await bot.get_me()
        if query.startswith("السورس") and iqthon.query.user_id == bot.uid:
            buttons = [[Button.url("Source", "https://t.me/IQTHON"), Button.url("Dev", "https://t.me/LLL5L")]]
            if IQTHONPC and IQTHONPC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(IQTHONPC, text=Sour, buttons=buttons, link_preview=False)
            elif IQTHONPC:
                result = builder.document(IQTHONPC,title="iqthon",text=Sour,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="iqthon",text=Sour,buttons=buttons,link_preview=False)
            await iqthon.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="السورس"))
async def repoiqthon(iqthon):
    if iqthon.fwd_from:
        return # ذمه برقبتك اذا تاخذ سطر واحد او تاخذ الفكره تعبي لاتخمطه ولاتاخذ افكاري بس الفاشل يسويها الى يوم القيامه
    TG_BOT = Config.TG_BOT_USERNAME
    if iqthon.reply_to_msg_id:
        await iqthon.get_reply_message()
    response = await bot.inline_query(TG_BOT, "السورس")
    await response[0].click(iqthon.chat_id)
    await iqthon.delete()
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order11")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الكروب 3   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙  `.تفعيل حمايه المجموعه`\n**✐ : يقوم غلق جميع صلاحيات المجموعه يبقي فقط ارسال  الرسائل❝**\n \n⑵  ⦙ `تعطيل حمايه المجموعه`\n**✐ :  يقوم بتشغيل جميع صلاحيات المجموعة ماعدا تغير المعلومات و التثبيت و اضافه اعضاء تبقى مسدوده❝**\n\n⑶  ⦙ `.صلاحيات المجموعه`\n**✐ : يقوم بعرض صلاحيات المجموعه المغلقه والمفتوحه❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑷  ⦙  `.رفع مشرف + الرد على شخص`\n**✐ : يرفع الشخص مشرف يعطي صلاحيه حذف رسائل والتثبيت فقط❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.منع + كلمة`\n**✐ : منع كلمه من الارسال في الكروب**❝\n⑹ ⦙ `.الغاء منع + كلمه`\n**✐ : يقوم بالغاء منع الكلمه ❝** \n⑺ ⦙ `.قائمه المنع`\n**✐ : يقوم بجلب جميع الكلمات الممنوعه في الكروب ❝**\n\n⑻ ⦙ ` .تاك + ( الاعداد المحدده وثابتة فقط) ⤵️`\n  ( 10 - 50 - 100 - 200  )\n**✐ : يجلب لك الاعضاء بالروابط بالعدد المحدد ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑼ ⦙ `.معرفات + ( الاعداد المحدده وثابتة فقط) ⤵️`\n  ( 10 - 50 - 100 - 200  )\n**✐ :جلب لك معرفات الاعضاء بالعدد المحدد ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders "
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order12")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الحساب 3   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴  ⦙  `.احصائيات حسابي`\n**✐ : يقوم بجلب عدد القنوات والاشخاص والمجموعات و التاكات لحسابك ❝**\n \n⑵  ⦙ `.قائمه جميع القنوات`\n**✐ :  يقوم بجلب جميع القنوات التي في حسابك مع روابط الخاصه بهن  ❝**\n\n⑶  ⦙ `.قائمه قنوات اديرها`\n**✐ : يقوم بجلب جميع القنوات التي مشرف بها مع روابطهن ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n⑷  ⦙  `.قائمه قنوات امتلكها`\n**✐ : يقوم بجلب جميع القنوات التي تمتلكها مع روابطهن ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑸  ⦙ `.قائمه جميع المجموعات `\n**✐ : يقوم بجلب جميع المجموعات في حسابك مع روابطهن**❝\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑹ ⦙ `.قائمه مجموعات اديرها`\n**✐ : يقوم بجلب جميع المجموعات التي مرفوع بها مشرف مع روابطهن ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑺ ⦙ `.قائمه مجموعات امتلكها`\n**✐ : يقوم بجلب جميع المجموعات التي تمتلكها مع روابطهن ❝**\n\n⑻ ⦙ `.وضع بايو + الرد على البايو`\n**✐ : يضع الكلمه التي تم رد عليها في البايو الخاص بك ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑼ ⦙ `.وضع اسم + الرد على الاسم`\n**✐ : يضع الاسم الذي تم رد عليه في اسمك ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑽ ⦙ `.وضع صوره + الرد على صوره`\n**✐ : يضع الصوره التي تم رد عليها في حسابك ❝**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order13")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑   اوامر الوقتي   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n ⑴ ⦙ `.اسم وقتي`\n**✐ : يضع الوقت المزخرف في اسمك تلقائيا ❝**\n\n ⑵ ⦙  `.نبذه وقتيه`\n**✐ : يضع الوقت المزخرف في نبذه الخاصه بك تلقائيا ❝**\n\n⑶⦙ `.صوره وقتيه`\n**✐ : يضع لك الوقت لمزخرف في صورتك تغير تلقائي ❝**\n\n\n⑷⦙ `.ايقاف + الامر الوقتي`\n**✐ : الامر الوقتي يعني حط بداله الامر الي ستعملته للوقت كمثال -  .ايقاف اسم وقتي او .ايقاف نبذه وقتيه او .ايقاف صوره وقتي ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order14")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑    الاوامر المتحركه للتسلية   ⦒  :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n\n `.غبي`\n`.تفجير`\n`.قتل`\n`.طوبه`\n`.مربعات`\n`.حلويات`\n`.نار`\n`.هلكوبتر`\n`.اشكال مربع`\n`.دائره`\n`.قلب `\n`.مزاج`\n`.قرد`\n`.ايد`\n`.العد التنازلي`\n`.الوان قلوب`\n`.عين`\n`.ثعبان`\n`.رجل`\n`.رموز شيطانيه`\n`.قطار`\n`.موسيقى`\n`.رسم`\n`.فراشه`\n`.مكعبات`\n`.مطر`\n`.تحركات`\n`.ايموجيات`\n`.طائره`\n`.شرطي`\n`.النضام الشمسي`\n`.افكر`\n`.اضحك`\n`.ضايج`\n`.ساعه متحركه`\n`.بوسه`\n`.قلوب`\n`.رياضه`\n`.الارض`\n`.قمر`\n`.اقمار`\n`.قمور`\n`.زرفه`\n`.بيبي`\n`.تفاعلات`\n`.اخذ قلبي`\n`.اشوفج السطح`\n`.احبك`\n`.اركض`\n`.روميو`\n`.البنك`\n`.تهكير + الرد على شخص`\n`.طياره`\n`.مصاصه`\n`.مصه`\n`.جكه`\n`.اركضلي`\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order15")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  1 اوامـر الـفـارات  ⦒ :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑴ ⦙ `.اضف فار + اسم افار + القيمه`\n**✐ :  يضيف اليك الفار الخاص بسورس ❝**\n⑵ ⦙ `.حذف فار + اسم الفار`\n**✐ :  يحذف الفار الذي اضفته ❝**\n⑶  ⦙ `.جلب فار + اسم الفار`\n**✐ :  يرسل اليك معلومات الفار وقيمه الفار ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**☣️  ⦑  1  الــفــارات  ⦒  :**\n\n**⑴ ⦙  لأضـافة فار كليشة حماية  الخاص للأضـافـة  ارسـل  :**\n`.اضف فار PM_TEXT + كليشة الحمايه الخاصة بـك`\n\n**⑵  ⦙ لأضـافة فار  ايدي الكـروب للأضافة أرسل بالرسائل محفوضة : **\n`.اضف فار PM_LOGGER_GROUP_ID  + ايدي مجموعتك`\n\n**⑶  ⦙ لأضـافة فار الايمـوجي  : **\n`.اضف فار ALIVE_EMOJI + الايموجي`\n\n **⑷  ⦙ لأضـافة فار  رسـاله بداية أمر السورس  : **\n `.اضف فار ALIVE_TEXT + النص`\n\n**⑸  ⦙  لأضـافة فار صورة رساله حماية  الخاص :**\n `.اضف فار PM_PIC + رابط تليجراف الصورة او الفيديو`\n\n **⑹ ⦙  لأضافـة فار صورة او فيديو أمر  السـورس : **\n `.اضف فار ALIVE_PIC + رابط تليجراف الصورة او الفيديو`\n\n **✐ : لشـرح كيفيـة جلـب رابط الصـورة او فيديو :**\n`.تليجراف ميديا + الرد على صورة او فيديو`\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text)
@iqthon.tgbot.on(CallbackQuery(data=re.compile(rb"order16")))
async def inlineiqthon(iqthon):
    text = "**🚹  ⦑  2 اوامـر الـفـارات  ⦒ :**\n\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮ \n⑴ ⦙ `.اضف فار + اسم افار + القيمه`\n**✐ :  يضيف اليك الفار الخاص بسورس ❝**\n⑵ ⦙ `.حذف فار + اسم الفار`\n**✐ :  يحذف الفار الذي اضفته ❝**\n⑶  ⦙ `.جلب فار + اسم الفار`\n**✐ :  يرسل اليك معلومات الفار وقيمه الفار ❝**\n⤪⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⟿⤮\n\n**☣️  ⦑  2  الــفــارات  ⦒  :**\n\n**⑴ ⦙  لتغير كليشة الفحص كاملة :**\n`.اضف فار ALIVE_TELETHONIQ + كليشه مع المتغيرات`\n\n**✐ : متغيرات كليشه الفحص  :**\n\n1 -  :  `{uptime}` :  مده التشغيل بوتك \n2 -  :  `{my_mention}`  : رابط حسابك  \n3 -  :  `{TM}`  : الوقت \n4 -  :  `{ping} ` : البنك \n5 -  : ` {telever} ` : نسخه تليثون \n6 -  :  `{tg_bot}` :  معرف بوتك \n\n**⎈ ⦙ لأضهار الأوامر مرة اخرى قم بضغط على ⬅️**  /orders"
    await iqthon.edit(text) # ذمه برقبتك اذا تاخذ سطر واحد او تاخذ الفكره تعبي لاتخمطه ولاتاخذ افكاري بس الفاشل يسويها الى يوم القيامه
