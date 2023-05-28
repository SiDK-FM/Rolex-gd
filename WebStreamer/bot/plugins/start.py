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

@StreamBot.on_message(filters.command(["start", "Rolexhelp"])) 
async def start(_, m: Message):
    message = f"ʜᴇʟʟᴏ {m.from_user.mention(style='md')},\n\n"
    message += "sᴇɴᴅ ᴍᴇ ᴀ ғɪʟᴇ ᴏʀ ʏᴏᴜ ᴄᴀɴ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴜsᴇ.\n"
    message += "<b>ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ :- @SkymoviesHDX</b>\n"
    await m.reply(message)
    

