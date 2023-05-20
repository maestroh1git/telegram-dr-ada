from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import random

# A list of jokes for the bot to choose from
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't some animals play cards? Because they are afraid of cheetahs!",
    # Add as many jokes as you want here
]

def joke(update: Update, context: CallbackContext) -> None:
    joke = random.choice(jokes)
    update.message.reply_text(joke)

joke_handler = CommandHandler('joke', joke)
