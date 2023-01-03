
from TeleBot import pgram as pbot
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from pyrogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio


Buttons = [ 
    [
        InlineKeyboardButton(text="Raiden Pic", callback_data="izumi_wife"),
        InlineKeyboardButton(text="Ganyu Pic", callback_data="ayato_wife"),
        InlineKeyboardButton(text="Shenhe Pic", callback_data="hachi_wife"),
        InlineKeyboardButton(text="Eula Pic", callback_data="Eulassy_wife"),
        InlineKeyboardButton(text="Zhongli Pic", callback_data="axel_husband"),
        InlineKeyboardButton(text=" BACK ", callback_data="revert")
    ]
]

@pbot.on_message(filters.command("profile"))
async def duh(_,m : Message):
    await m.reply_photo(
        photo="https://graph.org//file/391b178775977960b97bc.jpg",
        caption="text",
        reply_markup=InlineKeyboardMarkup(Buttons)
    )

@pbot.on_callback_query()
async def callbacks(_, CallbackQuery):
    if CallbackQuery.data == "izumi_wife":
        await CallbackQuery.edit_message_media(message.chat.id, message.id
            InputMediaPhoto("https://graph.org//file/e5b52252d26e00a76ec18.jpg")
        )
        await CallbackQuery.edit_message_caption(
            "Raiden Shogun Is ......for izumi",
            reply_markup=InlineKeyboardMarkup(Buttons)
        )
    elif CallbackQuery.data == "ayato_wife":
        await CallbackQuery.edit_message_media(
            media="https://graph.org//file/56aaee33fe6bb7b596680.jpg"
        )
        await CallbackQuery.edit_message_caption(
            caption="Ayato's wife is ganyu [ respectfull ship ] ",
            reply_markup=InlineKeyboardMarkup(Buttons)
        )
    elif CallbackQuery.data == "hachi_wife":
        await CallbackQuery.edit_message_media(
            media="https://graph.org//file/ff708ff6ce6ddb24e0efa.jpg"
        )
        await CallbackQuery.edit_message_caption(
            caption="a lovebite having shenhe as a wife ",
            reply_markup=InlineKeyboardMarkup(Buttons)
        )
    elif CallbackQuery.data == "Eulassy_wife":
        await CallbackQuery.edit_message_media(
            "https://graph.org//file/8fc599e834e4563a5314c.jpg"
        )
        await CallbackQuery.edit_message_caption(
            caption="corny doge wife = eula",
            reply_markup=InlineKeyboardMarkup(Buttons)
        )
    elif CallbackQuery.data == "axel_husband":
        await CallbackQuery.edit_message_media(
            "https://graph.org//file/1351234f830d51f7a7197.jpg"
        )
        await CallbackQuery.edit_message_caption(
            caption="dude zhongli is ok #no homo, but axel is gay....."
        )
    elif CallbackQuery.data == "revert":
        await CallbackQuery.edit_message_media(
            "https://graph.org//file/391b178775977960b97bc.jpg"
        )
        await CallbackQuery.edit_message_caption(
            caption="text"
        )
    else:
        return
