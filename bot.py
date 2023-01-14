import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

token = '5972375728:AAHGXbdkAqdmIGGbOul6Ds4BrJQMqOISRRY'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def good_am(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Good am!")
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('images/meme1.jpg', 'rb'))


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('good_am', good_am)
    application.add_handler(start_handler)

    application.run_polling()