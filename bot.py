import os

import telebot
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


def send_with_bot(message):

    bot = telebot.TeleBot(settings.BOT_TOKEN, parse_mode=None)

    for id in settings.ADMIN_TELEGRAM_IDS:
        bot.send_message(id, message)

    print(f'OTP Code: "{message}"')
