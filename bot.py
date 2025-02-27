import time
import logging
from telegram import Bot

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Replace with your Telegram Bot Token and Chat ID
BOT_TOKEN = "7503104760:AAHOpFMB8uG_aA48YM75-DodB2WcuHb8nZU"
CHAT_ID = "1331345346"

# Initialize the Bot
bot = Bot(token=BOT_TOKEN)

def send_message():
    """Send a message to the Telegram chat in an infinite loop."""
    while True:
        try:
            bot.send_message(chat_id=CHAT_ID, text="Hello, I am still running")
            logging.info("Message sent successfully!")
        except Exception as e:
            logging.error(f"Error sending message: {e}")
        
        # Wait for 60 seconds before sending the next message
        time.sleep(60)

if name == "main":
    send_message()
