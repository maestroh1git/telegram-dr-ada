from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Hello! I am your medical bot. How can I assist you today?')


def start(update: Update, context: CallbackContext) -> None:
    first_name = update.effective_user.first_name
    joke = "Why don't scientists trust atoms? Because they make up everything!"
    update.message.reply_text(
        f"Hey there, {first_name}! I'm DocBot, your personal medical assistant. "
        f"I'm here to help you with your medical questions. But first, how about a joke? \n\n{joke}\n\n"
        f"Alright, now how can I assist you today?")


start_handler = CommandHandler('start', start)
