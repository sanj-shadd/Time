import time
import schedule
from datetime import datetime
from twilio.rest import Client

# Twilio Credentials
ACCOUNT_SID = "ACd3d11924833b8deda6cd627af1152a47"
AUTH_TOKEN = "e5a3c0062b8c622f77a77e30f425e420"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio Sandbox Number
MY_WHATSAPP_NUMBER = "whatsapp:+254759596566"  # Your WhatsApp number

# Initialize Twilio Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_time():
    """Sends the current time via WhatsApp"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Current Time: {now}"
    
    try:
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=MY_WHATSAPP_NUMBER,
            body=message
        )
        print(f"Sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Schedule the job every 10 minutes
schedule.every(2).minutes.do(send_time)

if __name__ == "__main__":
    print("WhatsApp Bot is running...")
    send_time()  # Send first message immediately
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
