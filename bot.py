import os
from dotenv import load_dotenv
import telebot

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.startswith("#"):
        bot.reply_to(message, "پیام با هشتگ دریافت شد.")
    else:
        bot.reply_to(message, "لطفاً پیام خود را با هشتگ ارسال کنید.")

bot.polling()
