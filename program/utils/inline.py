""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data=f'cls'),
    ],
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
     InlineKeyboardButton(text="▢", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'cbresume | {user_id}'),
      InlineKeyboardButton(text="‣‣I", callback_data=f'cbunmute | {user_id}'),
    ],
    [
      InlineKeyboardButton(text="• Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Team_Bot_Support"),
      InlineKeyboardButton(text="Uᴘᴅᴀᴛᴇs •", url=f"https://t.me/team_bot_update"),
    ],
    [
      InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data="set_close"),
    ],
  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🗑 Close", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="cbmenu"
      )
    ]
  ]
)
