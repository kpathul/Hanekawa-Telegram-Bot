from src import dispatcher

from telegram import Update, ChatPermissions, TelegramError
from telegram.ext import CommandHandler, CallbackContext as Context

# messages for errors common in most actions
REQUIRES_ADMIN = "You need to be an admin to {} members"
ALTER_CREATOR = "You're trying to {} the group owner\nThis incident will be reported"
FORMAT_ERROR = ("To {} a person, you need to send this command as a reply to any message by that person\n"
                "This is the only way I can identify members right now")
NOT_GROUP_MEMBER = "The member you're trying to {} is no longer part of this group"

# statuses that correspond to admin privileges
ADMINS = ['administrator', 'creator']

# objects for corresponding permissions
MUTED_STATE = ChatPermissions(can_send_messages=False,
                              can_send_media_messages=False,
                              can_send_polls=False,
                              can_send_other_messages=False,
                              can_add_web_page_previews=False,
                              can_change_info=False,
                              can_invite_users=False,
                              can_pin_messages=False)
UNMUTED_STATE = ChatPermissions(can_send_messages=True,
                                can_send_media_messages=True,
                                can_send_polls=True,
                                can_send_other_messages=True,
                                can_add_web_page_previews=True,
                                can_change_info=False,
                                can_invite_users=False,
                                can_pin_messages=False)


def get_args(update):
    chat = update.effective_chat
    req_user = chat.get_member(update.effective_user.id)

    member = None

    if update.message.reply_to_message:
        from_user = update.message.reply_to_message.from_user
        if from_user:
            member = chat.get_member(from_user.id)

    if member:
        return [req_user, member]

    else:
        raise ValueError('incorrect_format')


def promote(update: Update, context: Context):
    try:
        args = get_args(update)
        requesting_member = args[0]
        member = args[1]
        status = member.status
        user = member.user

        if requesting_member.status not in ADMINS:
            update.message.reply_text(REQUIRES_ADMIN.format('promote'))
        elif status == 'administrator':
            update.message.reply_text("Looks like {} is already an admin".format(user.name))
        elif status == 'creator':
            update.message.reply_text(ALTER_CREATOR.format('promote'))
        elif status in ['kicked', 'banned', 'left']:
            update.message.reply_text(NOT_GROUP_MEMBER.format('promote'))
        else:
            context.bot.promote_chat_member(chat_id=update.effective_chat.id,
                                            user_id=user.id,
                                            can_delete_messages=True,
                                            can_invite_users=True,
                                            can_restrict_members=True,
                                            can_pin_messages=True,
                                            can_promote_members=True)
            update.message.reply_text("{} has been promoted!".format(user.name))

    except ValueError:
        update.message.reply_text(FORMAT_ERROR.format('promote'))


def demote(update: Update, context: Context):
    try:
        args = get_args(update)
        requesting_member = args[0]
        member = args[1]
        status = member.status
        user = member.user

        if requesting_member.status != 'creator':
            update.message.reply_text("Only the group owner can control admins")
        elif status in ['member', 'restricted']:
            update.message.reply_text("Looks like {} is not an admin".format(user.name))
        elif status == 'creator':
            update.message.reply_text(ALTER_CREATOR.format('demote'))
        elif status in ['kicked', 'banned', 'left']:
            update.message.reply_text(NOT_GROUP_MEMBER.format('demote'))

        else:
            context.bot.promote_chat_member(chat_id=update.effective_chat.id,
                                            user_id=user.id,
                                            can_delete_messages=True,
                                            can_invite_users=True,
                                            can_restrict_members=True,
                                            can_pin_messages=True,
                                            can_promote_members=True)
            update.message.reply_text("{} has been demoted".format(user.name))

    except ValueError:
        update.message.reply_text(FORMAT_ERROR.format('demote'))


def mute(update: Update, context: Context):
    try:
        args = get_args(update)
        requesting_member = args[0]
        member = args[1]
        status = member.status
        user = member.user

        if requesting_member.status not in ADMINS:
            update.message.reply_text(REQUIRES_ADMIN.format('mute'))
        elif status == 'administrator' and requesting_member.status != 'creator':
            update.message.reply_text("Only group owner can mute admins")
        elif status == 'creator':
            update.message.reply_text(ALTER_CREATOR.format('mute'))
        elif status in ['kicked', 'banned', 'left']:
            update.message.reply_text(NOT_GROUP_MEMBER.format('mute'))
        else:
            permissions = MUTED_STATE
            context.bot.restrict_chat_member(update.effective_chat.id, user.id, permissions)
            update.message.reply_text("{} has been muted".format(user.name))

    except ValueError:
        update.message.reply_text(FORMAT_ERROR.format('mute'))


def unmute(update: Update, context: Context):
    try:
        args = get_args(update)
        requesting_member = args[0]
        member = args[1]
        status = member.status
        user = member.user

        if requesting_member.status not in ADMINS:
            update.message.reply_text(REQUIRES_ADMIN.format('unmute'))
        elif status in ['administrator', 'member']:
            update.message.reply_text("The member you're trying to unmute does not have any restrictions")
        elif status == 'creator':
            update.message.reply_text(ALTER_CREATOR.format('unmute'))
        elif status in ['kicked', 'banned', 'left']:
            update.message.reply_text(NOT_GROUP_MEMBER.format('unmute'))
        else:
            permissions = UNMUTED_STATE
            context.bot.restrict_chat_member(update.effective_chat.id, user.id, permissions)
            update.message.reply_text("{} has been unmuted!".format(user.name))

    except ValueError:
        update.message.reply_text(FORMAT_ERROR.format('unmute'))


def kick(update: Update, context: Context):
    try:
        args = get_args(update)
        requesting_member = args[0]
        member = args[1]
        status = member.status
        user = member.user

        if requesting_member.status not in ADMINS:
            update.message.reply_text(REQUIRES_ADMIN.format('kick'))
        elif status == 'administrator' and requesting_member.status != 'creator':
            update.message.reply_text("Only group owner can kick admins")
        elif status == 'creator':
            update.message.reply_text(ALTER_CREATOR.format('kick'))
        elif status in ['kicked', 'banned', 'left']:
            update.message.reply_text(NOT_GROUP_MEMBER.format('kick'))
        else:
            context.bot.kick_chat_member(update.effective_chat.id, user.id)
            update.message.reply_text("{} has been kicked".format(user.name))

    except ValueError:
        update.message.reply_text(FORMAT_ERROR.format('kick'))


def unban(update: Update, context: Context):
    try:
        args = get_args(update)
        requesting_member = args[0]
        member = args[1]
        status = member.status
        user = member.user

        if requesting_member.status not in ADMINS:
            update.message.reply_text(REQUIRES_ADMIN.format('unban'))
        elif status in ['administrator', 'member', 'restricted', 'left']:
            update.message.reply_text("The user is currently not banned")
        elif status == 'creator':
            update.message.reply_text(ALTER_CREATOR.format('unban'))
        else:
            context.bot.unban_chat_member(update.effective_chat.id, user.id)
            update.message.reply_text("{} has been unbanned".format(user.name))

    except ValueError:
        update.message.reply_text(FORMAT_ERROR.format('unban'))


def pin(update: Update, context: Context):
    requesting_member = update.effective_chat.get_member(update.effective_user.id)
    message = update.message.reply_to_message

    if requesting_member.status not in ADMINS:
        update.message.reply_text("Only admins can pin messages")
    elif message:
        context.bot.pin_chat_message(update.effective_chat.id, message.message_id)
        update.message.reply_text("Done. Message pinned")
    else:
        update.message.reply_text("Please send this command as reply to the message to be pinned")


def unpin(update: Update, context: Context):
    requesting_member = update.effective_chat.get_member(update.effective_user.id)

    if requesting_member.status not in ADMINS:
        update.message.reply_text("Only admins can unpin messages")
    else:
        try:
            context.bot.unpin_chat_message(update.effective_chat.id)
            update.message.reply_text("Done. Message unpinned")
        except TelegramError:
            update.message.reply_text("No message has been pinned")


promote_handler = CommandHandler('promote', promote)
dispatcher.add_handler(promote_handler)

demote_handler = CommandHandler('demote', demote)
dispatcher.add_handler(demote_handler)

mute_handler = CommandHandler('mute', mute)
dispatcher.add_handler(mute_handler)

unmute_handler = CommandHandler('unmute', unmute)
dispatcher.add_handler(unmute_handler)

kick_handler = CommandHandler(['kick', 'ban'], kick)
dispatcher.add_handler(kick_handler)

unban_handler = CommandHandler('unban', unban)
dispatcher.add_handler(unban_handler)

pin_handler = CommandHandler('pin', pin)
dispatcher.add_handler(pin_handler)

unpin_handler = CommandHandler('unpin', unpin)
dispatcher.add_handler(unpin_handler)
