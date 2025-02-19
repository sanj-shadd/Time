import time
import schedule
import telegram
from datetime import datetime

# Telegram Bot Token (Replace with your actual token)
BOT_TOKEN = "7634325376:AAHFqGzi6w5PnLqSd-pF_SCC1eXfuy-cjiA"
CHAT_ID = "8027632810"

# Initialize the bot
bot = telegram.Bot(token=BOT_TOKEN)

def send_time():
    """Sends the current time to the Telegram chat."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Current Time: {now}"
    
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Schedule the job every 10 minutes
schedule.every(10).minutes.do(send_time)

# Run the scheduler
if __name__ == "__main__":
    print("Bot is running...")
    send_time()  # Send first message immediately
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
