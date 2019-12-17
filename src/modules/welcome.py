from src import dispatcher

from telegram import Update
from telegram.ext import CallbackContext as Context, run_async, MessageHandler, Filters


@run_async
def welcome(update: Update, context: Context):
    new_members = update.effective_message.new_chat_members
    for new_mem in new_members:
        if new_mem.id == context.bot.id:
            update.effective_message.reply_text(
                "Thankyou for adding me to %s!\nUse /help to see how I can help you" % update.effective_chat.title)
            continue
        update.effective_message.reply_text(
            "Yokoso %s!\nWelcome to %s" % (new_mem.first_name, update.effective_chat.title))


welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome)
dispatcher.add_handler(welcome_handler)
