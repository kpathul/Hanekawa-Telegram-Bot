from src import dispatcher

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext as Context

NEW_FEATURES = "I now welcome new users joinining the group!"
NEXT_FEATURES = (
    "My creator is always giving me new powers nyaa!\nNext my creator intends to implement invite, mute, "
    "promote, demote, kick, ban commands which can be used in groups.\nAlso, he's frantically trying to "
    "get hold of a remote server to host me so Meow can serve everyone 24\\7, no breaks!\nLook forward to "
    "it! (=^･ω･^=)")


def whats_new(update: Update, context: Context):
    update.message.reply_markdown(NEW_FEATURES)


def whats_next(update: Update, context: Context):
    update.message.reply_markdown(NEXT_FEATURES)


wnext_handler = CommandHandler('whatsnext', whats_next)
dispatcher.add_handler(wnext_handler)

wnew_handler = CommandHandler('whatsnew', whats_new)
dispatcher.add_handler(wnew_handler)
