from telegram import Update
from telegram.ext import MessageHandler, filters, CallbackContext
from services.openai_service import generate_response

async def handle_message(update: Update, context: CallbackContext) -> None:
    try:
        message = update.message.text
        response = generate_response(message)
        await update.message.reply_text(response)
    except Exception as e:
        print("An error occurred:", str(e))

response_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
