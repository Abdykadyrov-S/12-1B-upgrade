from django.core.management.base import BaseCommand
from apps.telegram_bot.views import bot

# from apps.telegram_bot

class Command(BaseCommand):
    help = "Bot"

    def handle(self, *args, **kwargs):
        print("Бот запустился")
        bot.polling(none_stop=True, interval=0)