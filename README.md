# Hanekawa Telegram Bot

A group-management telegram bot in python. Written with the help of the `python-telegram-bot` api. Inspired by HarukaAyaBot.

# Installation

This project was written in `python3.7`. Setting up a virtual environment with this python version is recommended before proceeding.

Install required python dependencies by running:

```
pip install -r requirements.txt\
```

Set up the `config.py` in the `src` folder by adding the `API_TOKEN` of your bot.
Other fields are optional.


# Running the bot

`cd` into the project directory and run
```
python3.7 -m src
```

The bot will now be alive. Test it out by sending it `/start` in telegram.

`NOTE`: If you have set up a virtual environment with `python3.7`, it is sufficient to just run
```
python -m src
```
