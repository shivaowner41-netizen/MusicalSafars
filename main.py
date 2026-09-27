import telebot

TOKEN="8338329388:AAGL1GFg_JmRTwjCO94toE5sVjnAraa4flw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your bot.")

bot.infinity_polling()
