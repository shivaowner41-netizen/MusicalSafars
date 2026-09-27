import telebot
import requests

TOKEN = 8338329388:AAF8DWkuoG8u_6u0ylP96uj3 OwYuC9iS4is
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot.")

bot.polling()

