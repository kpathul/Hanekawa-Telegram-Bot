from src import dispatcher

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext as Context

units = {}
units.update(dict.fromkeys(['s', 'sec', 'secs', 'second', 'seconds'], 'seconds'))
units.update(dict.fromkeys(['m', 'min', 'mins', 'minute', 'minutes'], 'minutes'))
units.update(dict.fromkeys(['h', 'hr', 'hrs', 'hour', 'hours'], 'hours'))
units.update(dict.fromkeys(['d', 'day', 'days'], 'days'))
units.update(dict.fromkeys(['w', 'wk', 'week', 'weeks'], 'weeks'))
units.update(dict.fromkeys(['mo', 'mos', 'month', 'months'], 'months'))
units.update(dict.fromkeys(['y', 'yr', 'yrs', 'year', 'years'], 'years'))

multiplier = {
    'seconds': 1,
    'minutes': 60, 'hours': 3600,
    'days': 86400
}

max_size = 1000


def set_reminder(update: Update, context: Context):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    user = update.effective_user.username

    if len(context.job_queue.jobs()) > max_size:
        update.message.reply_text(
            "I'm overloaded with reminders now nyaa (╥_╥). Let my creator know in the support group this happened")
    try:
        # args[0] should contain the time for the timer in seconds
        result = __parse_timer_context(context.args)
        due = result[0]
        reply = result[1]
        if due == -1:
            update.message.reply_text(reply)
            return

        context.job_queue.run_once(alarm, due, context={'chat_id': chat_id, 'user': user})

        update.message.reply_text(reply)

    except (IndexError, ValueError):
        update.message.reply_text('That was a wrong usage nyaa!\nSee /help for more details')


def __parse_timer_context(args):
    time_val = int(args[0])
    unit = 'seconds'

    if (time_val < 0):
        return [-1, "I can't go back in time nya (╥_╥)\nAsk that old vampire hag KissShot if you want to do that"]
    if len(args) > 1:
        unit = units[args[1]] if args[1] in units else args[1]

    if unit in ['months', 'years', 'decades', 'centuries', 'millennia'] or (unit == 'days' and time_val > 30):
        return [-1,
                "I don't know if I'll live that long nya (╥_╥)\nA shorter time(upto 30 days) is all I can handle at moment"]
    else:
        if unit not in multiplier:
            raise ValueError("Unexpected arguments")

    return [time_val * multiplier[unit],
            "Wakathawa nyaa(=^-ω-^=). Meow will remind you in %d %s" % (time_val, unit)]


def alarm(context):
    """Send the alarm message."""
    job = context.job
    context.bot.send_message(job.context['chat_id'], text='@%s Nyaaan! Your reminder is here!' % (job.context['user']))


remind_handler = CommandHandler("remindme", set_reminder,
                                pass_args=True,
                                pass_job_queue=True,
                                pass_chat_data=True)
dispatcher.add_handler(remind_handler)
