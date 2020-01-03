from src import dispatcher

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext as Context

NEW_FEATURES = (
                "I'm now hosted on a remote server! This means I'll be active all the time!\n"
                "I now promote, demote, mute and kick members and pin messages.\n"
                "Also try /xkcd for new year surprise!\n\n "
                "Note: To be more inclusive, unfortunately my anime theme is getting slowly removed and will be "
                "completely down by next update (ノ﹏ヽ)")
NEXT_FEATURES = (
    "My creator is always giving me new powers nyaa!\nI'll be getting a database soon.\n"
    "Look forward to it! (=^･ω･^=)")


def whats_new(update: Update, context: Context):
    update.message.reply_markdown(NEW_FEATURES)


def whats_next(update: Update, context: Context):
    update.message.reply_markdown(NEXT_FEATURES)


wnext_handler = CommandHandler('whatsnext', whats_next)
dispatcher.add_handler(wnext_handler)

wnew_handler = CommandHandler('whatsnew', whats_new)
dispatcher.add_handler(wnew_handler)
