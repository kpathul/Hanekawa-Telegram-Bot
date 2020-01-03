from src import updater

from src.modules import help, reminder, start, updates, welcome, chat_actions, xkcd


def main():
    updater.start_polling()
    # updater.idle()


if __name__ == '__main__':
    main()
