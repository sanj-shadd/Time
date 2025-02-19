import requests
import schedule
import time
from datetime import datetime
from wa_automate_socket_client import WhatsAppClient

# WhatsApp Bot Config
whatsapp = WhatsAppClient("ws://localhost:3000")  # Connect to Baileys server
receiver_number = "+254759596566"  # Format: "+1234567890"

# Function to fetch trade signals
def get_trade_signal():
    api_url = "https://example.com/trading-signals"  # Replace with actual signal API
    response = requests.get(api_url)
    
    if response.status_code == 200:
        signal = response.json()
        message = f"📈 Trade Alert!\nAsset: {signal['asset']}\nAction: {signal['action']}\nPrice: {signal['price']}"
        
        # Send message via WhatsApp
        whatsapp.send_message(receiver_number, message)
        print(f"[{datetime.now()}] Signal sent: {message}")
    else:
        print("Failed to fetch trade signal.")

# Schedule signal fetching every 15 minutes
schedule.every(15).minutes.do(get_trade_signal)

# Run the bot
while True:
    schedule.run_pending()
    time.sleep(1)
