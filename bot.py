import os
import telebot

BOT_TOKEN = '5972375728:AAHGXbdkAqdmIGGbOul6Ds4BrJQMqOISRRY'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(command=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
