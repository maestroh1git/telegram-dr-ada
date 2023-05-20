import logging
from telegram import Update
from telegram.ext import CallbackContext

def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, context.error)
