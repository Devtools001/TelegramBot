import random 
import time
import os
import asyncio
import requests 
from TeleBot import pgram
from pyrogram import filters
from types import NoneType
from pyrogram import filters, Client
from pyrogram.errors import UserNotParticipant, WebpageCurlFailed, WebpageMediaEmpty
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message
)

from TeleBot import (
    ANILIST_CLIENT,
    ANILIST_REDIRECT_URL,
    ANILIST_SECRET,
    OWNER,
    TRIGGERS as trg,
    BOT_NAME,
    anibot
)
