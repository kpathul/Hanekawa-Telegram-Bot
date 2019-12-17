from src import dispatcher

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext as Context

START_MESSAGE = (
    "Kyonichwa nyaaan!  V(=^･ω･^=)v\n\nI'm Neko Hanekawa. I'm the cat girl who'll take good care of your groups "
    "in exchange for headpats. (=^-ω-^=)\n\nTo see what all I can do as of now use /help.\nI'm still growing. "
    "Help me grow faster by joining the support group [here](https://t.me/NekoHanekawaGroup)\n\nMy owner is "
    "@DiscipleOfDisaster\n\nSore ja\nヽ(=^･ω･^=)丿")


def start(update: Update, context: Context):
    update.message.reply_markdown(START_MESSAGE)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
