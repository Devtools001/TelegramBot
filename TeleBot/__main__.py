import asyncio
import os
import re
import time
from datetime import datetime
from typing import Optional
from sys import argv
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from pyrogram.errors import BadRequest 
from pyrogram.types import CallbackQuery
from pyrogram import filters,idle

from TeleBot.modules import ALL_MODULES

from TeleBot.modules.utilities.misc import paginate_modules
 
