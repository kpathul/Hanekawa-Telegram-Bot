from src import dispatcher

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext as Context

NEW_FEATURES = "New year update is here! I now promote, demote, mute and kick members. Also try /xkcd for new year surprise!"
NEXT_FEATURES = (
    "My creator is always giving me new powers nyaa!\nI'll be getting a database soon.\nAnd I'm close to being hosted"
    "on a remote server!\nLook forward to it! (=^･ω･^=)")


def whats_new(update: Update, context: Context):
    update.message.reply_markdown(NEW_FEATURES)


def whats_next(update: Update, context: Context):
    update.message.reply_markdown(NEXT_FEATURES)


wnext_handler = CommandHandler('whatsnext', whats_next)
dispatcher.add_handler(wnext_handler)

wnew_handler = CommandHandler('whatsnew', whats_new)
dispatcher.add_handler(wnew_handler)
