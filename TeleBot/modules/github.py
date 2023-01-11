import requests 
from TeleBot import pgram,SUPPORT_CHAT
from pyrogram import filters,enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 


@pgram.on_message(filters.command(["git","github"]))
async def _github(_, message):
    if len(message.command) < 2:
        return await message.reply_text("🙃 ʜᴇʏ ɢɪᴠᴇ ᴀ GɪᴛHᴜʙ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏᴏ.")

    username = message.text.split(None,1)[1]
    URL = f'https://api.github.com/users/{username}'
    result = requests.get(URL).json()
    try:
        m = await message.reply_text("`Searching.....`")
        url = result['html_url']
        name = result['name']
        company = result['company']
        bio = result['bio']
        created_at = result['created_at']
        avatar_url = result['avatar_url']
        blog = result['blog']
        location = result['location']
        repositories = result['public_repos']
        followers = result['followers']
        following = result['following']
        caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profile Link:** [Here]({url})
**Company:** `{company}`
**Created On:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Location:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
        await m.delete()
        await message.reply_photo(avatar_url, caption=caption,reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Profile",
                            url=url,
                        ),
                    ],
                ],
            ), parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        print(str(e))
        await message.reply_text(f"ERROR!! Contact @{SUPPORT_CHAT}")
        pass
