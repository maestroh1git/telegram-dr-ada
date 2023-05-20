from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# Replace 'your-telegram-bot-token' with your token
updater = Updater(token='your-telegram-bot-token', use_context=True)

dispatcher = updater.dispatcher

# Replace 'your-openai-api-key' with your OpenAI key
openai.api_key = 'your-openai-api-key'

def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I am your ChatGPT bot. Ask me anything.")

def respond(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    response = openai.Completion.create(engine="text-davinci-002", prompt=message, max_tokens=60)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text.strip())

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), respond)
dispatcher.add_handler(echo_handler)

updater.start_polling()
