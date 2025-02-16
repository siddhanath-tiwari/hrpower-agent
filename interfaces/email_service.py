

# import sendgrid
# from sendgrid.helpers.mail import Mail

# SENDGRID_API_KEY = "your_sendgrid_api_key"

# def send_email(to, subject, body):
#     sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
#     email = Mail(
#         from_email="your_verified_sendgrid_email@example.com",
#         to_emails=to,
#         subject=subject,
#         plain_text_content=body
#     )

#     response = sg.send(email)
#     return response.status_code  # 202 means email sent successfully



import sendgrid
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")

def send_email(to, subject, body):
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    email = Mail(
        from_email=FROM_EMAIL,
        to_emails=to,
        subject=subject,
        plain_text_content=body
    )

    response = sg.send(email)
    return response.status_code  # 202 means email sent successfully


""" key twillo 
RE55NHK8PULETTSMYGARHJ6P"""