import asyncio
from telegram import Bot
from datetime import datetime
import schedule
import time

# Telegram Bot Token and Chat ID
BOT_TOKEN = "7634325376:AAHFqGzi6w5PnLqSd-pF_SCC1eXfuy-cjiA"
CHAT_ID = "8027632810"

bot = Bot(token=BOT_TOKEN)

async def send_time():
    """Sends the current time to the Telegram chat asynchronously."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Current Time: {now}"
    
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

def job():
    asyncio.run(send_time())  # Ensures async execution

# Schedule the job every 10 minutes
schedule.every(10).minutes.do(job)

# Run the scheduler
if __name__ == "__main__":
    print("Bot is running...")
    asyncio.run(send_time())  # Send first message immediately
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
