import json
import requests
import html
import random
import time

from SiestaRobot import dispatcher
from SiestaRobot.modules.disable import DisableAbleCommandHandler
from SiestaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async, CallbackQueryHandler
from telegram import ParseMode, Update, InlineKeyboardMarkup, InlineKeyboardButton, replymarkup, ChatPermissions
from telegram.error import BadRequest

def anime_quote():
    url = "https://animechan.vercel.app/api/random"
    # since text attribute returns dictionary like string
    response = requests.get(url)
    try:
        dic = json.loads(response.text)
    except Exception:
        pass
    quote = dic["quote"]
    character = dic["character"]
    anime = dic["anime"]
    return quote, character, anime
def quotes(update: Update, context: CallbackContext):
    message = update.effective_message
    quote, character, anime = anime_quote()
    msg = f"<i>❝{quote}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Change🔁",
            callback_data="change_quote")]])
    message.reply_text(
        msg,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )
def change_quote(update: Update, context: CallbackContext):
    query = update.callback_query
    chat = update.effective_chat
    message = update.effective_message
    quote, character, anime = anime_quote()
    msg = f"<i>❝{quote}❞</i>\n\n<b>{character} from {anime}</b>"
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="Change🔁",
            callback_data="quote_change")]])
    message.edit_text(msg, reply_markup=keyboard,
                      parse_mode=ParseMode.HTML)
    
def animequotes(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(QUOTES_IMG))
QUOTES_IMG = (
      "https://i.imgur.com/Iub4RYj.jpg", 
      "https://i.imgur.com/uvNMdIl.jpg", 
      "https://i.imgur.com/YOBOntg.jpg", 
      "https://i.imgur.com/fFpO2ZQ.jpg", 
      "https://i.imgur.com/f0xZceK.jpg", 
      "https://i.imgur.com/RlVcCip.jpg", 
      "https://i.imgur.com/CjpqLRF.jpg", 
      "https://i.imgur.com/8BHZDk6.jpg", 
      "https://i.imgur.com/8bHeMgy.jpg", 
      "https://i.imgur.com/5K3lMvr.jpg", 
      "https://i.imgur.com/NTzw4RN.jpg", 
      "https://i.imgur.com/wJxryAn.jpg", 
      "https://i.imgur.com/9L0DWzC.jpg", 
      "https://i.imgur.com/sBe8TTs.jpg", 
      "https://i.imgur.com/1Au8gdf.jpg", 
      "https://i.imgur.com/28hFQeU.jpg", 
      "https://i.imgur.com/Qvc03JY.jpg", 
      "https://i.imgur.com/gSX6Xlf.jpg", 
      "https://i.imgur.com/iP26Hwa.jpg", 
      "https://i.imgur.com/uSsJoX8.jpg", 
      "https://i.imgur.com/OvX3oHB.jpg", 
      "https://i.imgur.com/JMWuksm.jpg", 
      "https://i.imgur.com/lhM3fib.jpg", 
      "https://i.imgur.com/64IYKkw.jpg", 
      "https://i.imgur.com/nMbyA3J.jpg", 
      "https://i.imgur.com/7KFQhY3.jpg", 
      "https://i.imgur.com/mlKb7zt.jpg", 
      "https://i.imgur.com/JCQGJVw.jpg", 
      "https://i.imgur.com/hSFYDEz.jpg", 
      "https://i.imgur.com/PQRjAgl.jpg", 
      "https://i.imgur.com/ot9624U.jpg", 
      "https://i.imgur.com/iXmqN9y.jpg", 
      "https://i.imgur.com/RhNBeGr.jpg", 
      "https://i.imgur.com/tcMVNa8.jpg", 
      "https://i.imgur.com/LrVg810.jpg", 
      "https://i.imgur.com/TcWfQlz.jpg", 
      "https://i.imgur.com/muAUdvJ.jpg", 
      "https://i.imgur.com/AtC7ZRV.jpg", 
      "https://i.imgur.com/sCObQCQ.jpg", 
      "https://i.imgur.com/AJFDI1r.jpg", 
      "https://i.imgur.com/TCgmRrH.jpg", 
      "https://i.imgur.com/LMdmhJU.jpg", 
      "https://i.imgur.com/eyyax0N.jpg", 
      "https://i.imgur.com/YtYxV66.jpg", 
      "https://i.imgur.com/292w4ye.jpg", 
      "https://i.imgur.com/6Fm1vdw.jpg", 
      "https://i.imgur.com/2vnBOZd.jpg", 
      "https://i.imgur.com/j5hI9Eb.jpg", 
      "https://i.imgur.com/cAv7pJB.jpg", 
      "https://i.imgur.com/jvI7Vil.jpg", 
      "https://i.imgur.com/fANpjsg.jpg", 
      "https://i.imgur.com/5o1SJyo.jpg", 
      "https://i.imgur.com/dSVxmh8.jpg", 
      "https://i.imgur.com/02dXlAD.jpg", 
      "https://i.imgur.com/htvIoGY.jpg", 
      "https://i.imgur.com/hy6BXOj.jpg", 
      "https://i.imgur.com/OuwzNYu.jpg", 
      "https://i.imgur.com/L8vwvc2.jpg", 
      "https://i.imgur.com/3VMVF9y.jpg", 
      "https://i.imgur.com/yzjq2n2.jpg", 
      "https://i.imgur.com/0qK7TAN.jpg", 
      "https://i.imgur.com/zvcxSOX.jpg", 
      "https://i.imgur.com/FO7bApW.jpg", 
      "https://i.imgur.com/KK06gwg.jpg", 
      "https://i.imgur.com/6lG4tsO.jpg",
      "https://i.imgur.com/D6Gv66Q.jpg",
      "https://i.imgur.com/Nh6Sw54.jpg",
      "https://i.imgur.com/5hDvwKk.jpg",
      "https://i.imgur.com/ygtzH8d.jpg",
      "https://i.imgur.com/1SH7Bat.jpg",
      "https://i.imgur.com/IZjXBqy.jpg",
      "https://i.imgur.com/KcX1lEz.jpg",
      "https://i.imgur.com/EOVd1wk.jpg",
      "https://i.imgur.com/eNmTqYK.jpg",
      "https://i.imgur.com/6sZeQ3N.jpg",
      "https://i.imgur.com/86F0bqf.jpg",
      "https://i.imgur.com/OL8gGX0.jpg",
      "https://i.imgur.com/VGjYXHX.jpg",
      "https://i.imgur.com/tujl3rU.jpg",
      "https://i.imgur.com/wnBNcyz.jpg",
      "https://i.imgur.com/lQK56UX.jpg",
      "https://i.imgur.com/zRYTJkl.jpg",
      "https://i.imgur.com/7tgPw30.jpg",
      "https://i.imgur.com/WuYLzme.jpg",
      "https://i.imgur.com/caXj5DD.jpg",
      "https://i.imgur.com/9tIoFy5.jpg",
      "https://i.imgur.com/TkndZgn.png",
      "https://i.imgur.com/0iEf6es.jpg",
      "https://i.imgur.com/LIzfbyi.png",
      "https://i.imgur.com/OER5Zr9.jpg",
      "https://i.imgur.com/NWxuHwV.jpg",
      "https://i.imgur.com/LN4sCCI.jpg",
      "https://i.imgur.com/uBE1wnj.jpg",
      "https://i.imgur.com/F8nF3Ii.jpg",
      "https://i.imgur.com/6ePhNPO.jpg",
      "https://i.imgur.com/tsQLjFL.jpg",
      "https://i.imgur.com/VT1Fep3.jpg",
      "https://i.imgur.com/UzYzQXX.jpg",
      "https://i.imgur.com/S81p8Vh.jpg",
      "https://i.imgur.com/ZdMIpyn.jpg",
      "https://i.imgur.com/r7MmFZI.jpg",
      "https://i.postimg.cc/LsGJsMd6/Itachie.jpg"
      
      )    

__help__ = """
  ──「 ANIMEQUOTES 」──

• `/quote`*:* for quotes
• `/animequotes`*:* for anime quotes"""
__mod_name__ = "「animequotes」"


ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes, run_async=True)
QUOTES_HANDLER = DisableAbleCommandHandler("quote", quotes, run_async=True)

CHANGE_QUOTE = CallbackQueryHandler(
    change_quote, pattern=r"change_.*")
QUOTE_CHANGE = CallbackQueryHandler(
    change_quote, pattern=r"quote_.*")
dispatcher.add_handler(CHANGE_QUOTE)
dispatcher.add_handler(QUOTE_CHANGE)
dispatcher.add_handler(ANIMEQUOTES_HANDLER)
dispatcher.add_handler(QUOTES_HANDLER)

__command_list__ = [

    "animequotes",
    "quote"

]

__handlers__ = [

    ANIMEQUOTES_HANDLER,
    QUOTES_HANDLER

]
