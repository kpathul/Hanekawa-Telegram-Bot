from src import dispatcher

from telegram import Update, ChatPermissions
from telegram.ext import CommandHandler, CallbackContext as Context


def promote(update: Update, context: Context):
    chat = update.effective_chat
    admins = chat.get_administrators()
    req_user = chat.get_member(update.effective_user.id)

    if req_user not in admins:
        update.message.reply_text("You need to be an admin or owner to promote nyaa!")
        return

    user = None
    # try:
    #     uname= context.args[1]
    #     if not uname.startswith('@'):
    #         raise ValueError("Unexpected arguments")
    #     user =

    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user

    if user:
        if chat.get_member(user.id) not in admins:
            context.bot.promote_chat_member(chat_id=chat.id,
                                            user_id=user.id,
                                            can_delete_messages=True,
                                            can_invite_users=True,
                                            can_restrict_members=True,
                                            can_pin_messages=True,
                                            can_promote_members=True)
            update.message.reply_text("Got it, {} has been promoted!".format(user.name))
        else:
            update.message.reply_text("Wahh! Looks like {} is already an admin".format(user.name))
    else:
        update.message.reply_text(
            "To promote a person, you need to send this command as a reply to any message by that person\n"
            "This is the only way I can identify users right now. Gomen (ノ﹏ヽ)")


def demote(update: Update, context: Context):
    chat = update.effective_chat
    admins = chat.get_administrators()
    req_user = chat.get_member(update.effective_user.id)

    if req_user not in admins:
        update.message.reply_text("You need to be an owner to demote nyaa!")
        return

    user = None

    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user

    if user:
        if chat.get_member(user.id) in admins:
            context.bot.promote_chat_member(chat_id=chat.id,
                                            user_id=user.id,
                                            can_delete_messages=False,
                                            can_invite_users=False,
                                            can_restrict_members=False,
                                            can_pin_messages=False,
                                            can_promote_members=False)
            update.message.reply_text("Got it, {} has been stripped of their powers!".format(user.name))
        else:
            update.message.reply_text("Wahh! Looks like {} is not an admin".format(user.name))
    else:
        update.message.reply_text(
            "To demote a person, you need to send this command as a reply to any message by that person\n"
            "This is the only way I can identify users right now. Gomen (ノ﹏ヽ)")


def kick(update: Update, context: Context):
    chat = update.effective_chat
    admins = chat.get_administrators()
    req_user = chat.get_member(update.effective_user.id)

    if req_user not in admins:
        update.message.reply_text("You need to be an admin to kick nyaa!")
        return

    user = None

    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user

    if user:
        if chat.get_member(user.id) not in admins:
            context.bot.kick_chat_member(chat.id, user.id)
            update.message.reply_text("Got it, {} has been kicked!".format(user.name))
        else:
            update.message.reply_text("Wahh! Looks like {} is an admin".format(user.name))
    else:
        update.message.reply_text(
            "To kick a person, you need to send this command as a reply to any message by that person\n"
            "This is the only way I can identify users right now. Gomen (ノ﹏ヽ)")


def mute(update: Update, context: Context):

    permissions= ChatPermissions(can_send_messages=False,
                                 can_send_media_messages=False,
                                 can_send_polls=False,
                                 can_send_other_messages=False,
                                 can_add_web_page_previews=False,
                                 can_change_info=False,
                                 can_invite_users=False,
                                 can_pin_messages=False)

    chat = update.effective_chat
    admins = chat.get_administrators()
    req_user = chat.get_member(update.effective_user.id)

    if req_user not in admins:
        update.message.reply_text("You need to be an admin to mute nyaa!")
        return

    user = None

    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user

    if user:
        if chat.get_member(user.id) not in admins:
            context.bot.restrict_chat_member(chat.id, user.id, permissions)
            update.message.reply_text("Got it, {} has been muted!".format(user.name))
        else:
            update.message.reply_text("Wahh! Looks like {} is an admin".format(user.name))
    else:
        update.message.reply_text(
            "To mute a person, you need to send this command as a reply to any message by that person\n"
            "This is the only way I can identify users right now. Gomen (ノ﹏ヽ)")


def unmute(update: Update, context: Context):

    permissions= ChatPermissions(can_send_messages=True,
                                 can_send_media_messages=True,
                                 can_send_polls=True,
                                 can_send_other_messages=True,
                                 can_add_web_page_previews=True,
                                 can_change_info=False,
                                 can_invite_users=False,
                                 can_pin_messages=False)

    chat = update.effective_chat
    admins = chat.get_administrators()
    req_user = chat.get_member(update.effective_user.id)

    if req_user not in admins:
        update.message.reply_text("You need to be an admin to unmute nyaa!")
        return

    user = None

    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user

    if user:
        if chat.get_member(user.id) not in admins:
            context.bot.restrict_chat_member(chat.id, user.id, permissions)
            update.message.reply_text("Got it, {} has been unmuted!".format(user.name))
        else:
            update.message.reply_text("Wahh! Looks like {} is an admin".format(user.name))
    else:
        update.message.reply_text(
            "To unmute a person, you need to send this command as a reply to any message by that person\n"
            "This is the only way I can identify users right now. Gomen (ノ﹏ヽ)")


promote_handler = CommandHandler('promote', promote)
dispatcher.add_handler(promote_handler)

demote_handler = CommandHandler('demote', demote)
dispatcher.add_handler(demote_handler)

mute_handler= CommandHandler('mute', mute)
dispatcher.add_handler(mute_handler)

unmute_handler= CommandHandler('unmute', unmute)
dispatcher.add_handler(unmute_handler)

kick_handler= CommandHandler('kick', kick)
dispatcher.add_handler(kick_handler)