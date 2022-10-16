import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 هلا عمري {message.from_user.mention()} !
   بوت اشغلك اغاني بكروبك الخايس احبك لضوج هههههععععع 

    ✯ راح تلكه طريقة الاستخدام في زر الاوامر

    ✯ واذا واجهة مشكلة لا تتواصل مع مطور البوت
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☬ اضفني الى مجموعتك ☬", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 مطور البوت 👨‍💻", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "🥇 كروب الدعم 🥇", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "👷‍♂ الاوامر 👷‍♂", url=f"https://telegra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-04-06"
                    ),
                    InlineKeyboardButton(
                        "🌐 قناة البوت الرسمية 🌐", url="https://t.me/KKKT6"
                    )]
            ]
       ),
    )

