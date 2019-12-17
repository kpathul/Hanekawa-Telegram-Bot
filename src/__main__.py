from src import updater

from src.modules import help, reminder, start, updates, welcome


def main():
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
