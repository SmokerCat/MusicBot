
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAImYGDMHTX4zOA9PWMPjokeT_woS2uzAAKqAgACgAxhVrW_bIls07PzHwQ")
        
    await message.reply_text(
        f"""**Dear {message.from_user.first_name}!

🌼 I am Aami Music Player. 🌼

🥳 I can play music in your Telegram Group's Voice Chat😉


⚜️You can make your own music bot just tap on deploy link 🔱


Developed by ⚡ @Cat_of_TelegramX ⚡


My commands - type  /help to get commands, which work in grp

Thanks for using .

Regrards [AAMI](https://t.me/Aami_song_bot)
**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍁 REPO 🍁", url="https://t.me/Cat_Telegram_Project_Club")
                  ],[
                    InlineKeyboardButton(
                        "🌼 Group", url="https://t.me/Cat_Telegram_Project_Club"
                    ),
                    InlineKeyboardButton(
                        "🌼 Channel", url="https://t.me/Cat_Telegram_Projects"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🦋 Add To Your Group 🦋", url="https://t.me/Aami_song_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⭐Aami MUSIC PLAYER IS ALWAYS ACTIVE!!⭐**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼 Channel", url="https://t.me/Cat_Telegram_Projects")
                ]
            ]
        )
   )
