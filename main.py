# from telegram.ext import Updater
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram.ext import MessageHandler, filters, CallbackContext
from handlers.start_handler import start
from handlers.error_handler import error
from handlers.response_handler import handle_message
from handlers.joke_handler import joke
import logging

from config import TELEGRAM_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

print("Starting bot...")


def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    application.add_handler(CommandHandler("joke", joke))
    application.add_error_handler(error)

    application.run_polling()

if __name__ == '__main__':
    main()
