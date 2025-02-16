# from twilio.rest import Client

# def send_whatsapp_message(to, body):
#     # Twilio configuration
#     account_sid = 'your_account_sid'
#     auth_token = 'your_auth_token'
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#         to=f"whatsapp:{to}",
#         from_="whatsapp:+14155238886",
#         body=body
#     )
#     return message.sid


import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_whatsapp_message(to, body):
    # Twilio credentials from environment variables
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp_number = "whatsapp:+14155238886"  # Twilio Sandbox Number

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=f"whatsapp:{to}",
        from_=from_whatsapp_number,
        body=body
    )
    return message.sid

# Example Usage
if __name__ == "__main__":
    response = send_whatsapp_message("+919876543210", "Hello from HR Agent!")
    print(f"WhatsApp Message Sent! SID: {response}")
