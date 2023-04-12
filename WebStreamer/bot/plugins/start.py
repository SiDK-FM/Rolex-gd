# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer.utils import get_hash, get_name
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    message = f"Hello {m.from_user.mention(style='md')},\n\n"
    message += "Send me a file or You can just add me any Telegram Channel and Use.\n"
    message += "<b>Example:-</b>\n"
    message += "<i>https://file2link.vigabots.rf.gd/1001901987607/1</i>\n\n"
    message += "<i>https://file2link.vigabots.rf.gd/Your_Channel_ID/Message_ID</i>\n\n"
    message += "<b>Join My Updates Channel :- @Link_Leech</b>\n"
    message += "<b>Join My Support Group :- @Viga_Bots_Discussion</b>"
    await m.reply(message)
