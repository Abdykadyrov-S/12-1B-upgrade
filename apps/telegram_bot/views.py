from django.shortcuts import render

from django.conf import settings
from telebot import TeleBot, types
from .models import TelegramUser

# Create your views here.

TELEGRAM_TOKEN = "6774314746:AAEgwNioDtJimhkmm4tveqMPZSw2q7GEwBk"
ADMIN_ID = 1904375259

bot = TeleBot(TELEGRAM_TOKEN, threaded=False)

@bot.message_handler(commands=["start"])
def start(message:types.Message):
    TelegramUser.objects.get_or_create(username = message.from_user.username, id_user=message.from_user.id, first_name = message.from_user.first_name, last_name = message.from_user.last_name,)
    bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

def get_text(message):
    bot.send_message(ADMIN_ID, message)


def echo(message:types.Message):
    bot.send_message(message.chat.id, f"Я вас не понял {message.from_user.full_name}")
