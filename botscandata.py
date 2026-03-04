import telebot

TOKEN = '8393798970:AAHO6UhsD7xx7WDsV7CiNgKSuz4xfL6dEDo'
ADMIN_ID = 7216238572

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! If you need help, type /help.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "This bot is here to help you. Just send a message and the admin will be notified.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)

bot.polling()