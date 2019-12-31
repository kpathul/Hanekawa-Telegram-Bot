from src import dispatcher
from src.helper_functions import xkcd_meme

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext as Context

from random import randint


def xkcd(update: Update, context: Context):
    COMIC_NO = randint(1, 2248)
    try:
        meme = xkcd_meme.Meme(COMIC_NO).getImageUrl()
        if meme:
            update.message.reply_photo(meme)
        else:
            update.message.reply_text("xkcd server seems to be down")

    except ValueError:
        update.message.reply_text(ValueError)

meme_handler= CommandHandler("xkcd", xkcd)
dispatcher.add_handler(meme_handler)