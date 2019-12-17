from src import dispatcher

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext as Context

COMMAND_LIST = {
    'start': 'Command to check if I\'m alive',
    'help': '/help: Sends you a message on how to use me\n/help <command>: Sends you the usage of a particular command',
    'list': 'Lists all available commands',
    'remindme': 'Sets a remindmer\nUsage: /remindme <time> <unit>\nExample: */remindme 10 min* sets a reminder for 10 minutes after current time',
    'whatsnew': 'Lets you know about the latest feature added to me',
    'whatsnext': 'Lets you know what features my creator is working on adding next'
}

HELP_MESSAGE = (
    "Nyeko is here to help nyaa!\n\nTo see all commands I respond to, use /list\nTo get the usage of a "
    "particular command use /help <command>\nTo support my creator use /support (Available soon!)\n\nIf you "
    "have any other queries or want to request new features, head over to the [support group]("
    "https://t.me/NekoHanekawaGroup)")


def help(update: Update, context: Context):
    try:
        command = context.args[0]
        if command[0] == '/':
            command = command[1:]

        update.message.reply_markdown(COMMAND_LIST[command])

    except(ValueError, IndexError):
        update.message.reply_markdown(HELP_MESSAGE)


def list_all(update: Update, context: Context):
    commands = '/' + '\n/'.join(COMMAND_LIST.keys())
    update.message.reply_text("List of available commands are:\n%s" % (commands))


help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

list_handler = CommandHandler('list', list_all)
dispatcher.add_handler(list_handler)
