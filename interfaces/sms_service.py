# from twilio.rest import Client

# def send_sms(to, body):
#     # Twilio configuration
#     account_sid = 'your_account_sid'
#     auth_token = 'your_auth_token'
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#         to=to,
#         from_="your_twilio_number",
#         body=body
#     )
#     return message.sid


from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

def send_sms(to, body):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        to=to,
        from_=TWILIO_PHONE_NUMBER,
        body=body
    )
    return message.sid
