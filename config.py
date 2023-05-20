import os
from dotenv import load_dotenv

load_dotenv("botfather.env")

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')
