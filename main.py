import telebot
import requests

TOKEN = '8338329388:AAHOjUuxY_r3eL4DRhokaa zElKc47-CH710'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot.")

bot.polling()


