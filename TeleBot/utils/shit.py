

TELEGRAPH = InlineKeyboardMarkup( [
            [
            InlineKeyboardButton(text="Open Link", url=f"https://graph.org{downloaded_file[0]}"),
            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{downloaded_file[0]}")
            ],
            [
            InlineKeyboardButton(text="✗ Close ✗", callback_data="close")
            ],
          ]
        )
     
        
