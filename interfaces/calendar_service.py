from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
# Google Calendar API configuration
SCOPES = ['https://www.googleapis.com/auth/calendar']

SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, "C:/Users/HP/Desktop/finnle HR project/config/credentials.json")


credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

def schedule_event(event):
    calendar_id = 'primary'
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    return event['htmlLink']

# Example usage
if __name__ == "__main__":
    event = {
        "summary": "Test Event",
        "description": "This is a test event",
        "start": {"dateTime": "2025-02-20T10:00:00Z", "timeZone": "UTC"},
        "end": {"dateTime": "2025-02-20T11:00:00Z", "timeZone": "UTC"}
    }
    event_link = schedule_event(event)
    print(f"Event created: {event_link}")