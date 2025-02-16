# from interfaces.calendar_service import schedule_event

# def schedule_interview(candidate_name, interviewer_name, date_time):
#     event = {
#         "summary": f"Interview with {candidate_name}",
#         "description": f"Interview scheduled with {candidate_name} and {interviewer_name}.",
#         "start": {"dateTime": date_time, "timeZone": "UTC"},
#         "end": {"dateTime": date_time, "timeZone": "UTC"}
#     }
#     schedule_event(event)
#     return f"Interview scheduled for {candidate_name} with {interviewer_name} on {date_time}."

from datetime import datetime, timedelta
import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Google Calendar API Authentication
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "config\credentials.json"  # Update with your actual credentials file

def authenticate_calendar():
    """Authenticate and return Google Calendar API service."""
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build("calendar", "v3", credentials=credentials)

def schedule_interview(candidate_name, interviewer_name, date_time):
    """Schedules an interview on Google Calendar"""
    logging.debug(f"🔹 Scheduling Interview for {candidate_name} with {interviewer_name} on {date_time}")
    
    try:
        # Convert date_time string to datetime object
        start_time = datetime.fromisoformat(date_time[:-1])  # Removing 'Z'
        end_time = start_time + timedelta(hours=1)

        # Google Calendar Event Details
        event = {
            "summary": f"Interview: {candidate_name} & {interviewer_name}",
            "description": f"Scheduled interview with {candidate_name} and {interviewer_name}.",
            "start": {"dateTime": start_time.isoformat() + "Z", "timeZone": "UTC"},
            "end": {"dateTime": end_time.isoformat() + "Z", "timeZone": "UTC"}
        }

        # Authenticate and schedule event
        service = authenticate_calendar()
        event_result = service.events().insert(calendarId="primary", body=event).execute()
        
        event_link = event_result.get("htmlLink", "No Link Available")
        logging.debug(f"✅ Interview Scheduled: {event_link}")
        return f"Interview scheduled for {candidate_name} with {interviewer_name} on {date_time}. Link: {event_link}"

    except Exception as e:
        logging.error(f"❌ Scheduling Error: {e}")
        return f"Error scheduling interview: {e}"


print(schedule_interview("Rahul Sharma", "Ankit Mehta", "2025-02-16T10:00:00Z"))

