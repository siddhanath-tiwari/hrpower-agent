import unittest
from unittest.mock import patch
from interfaces.email_service import send_email
from interfaces.sms_service import send_sms
from interfaces.whatsapp_service import send_whatsapp_message
from interfaces.calendar_service import schedule_event

class TestInterfaces(unittest.TestCase):
    @patch("interfaces.email_service.send_email")
    def test_send_email(self, mock_send_email):
        mock_send_email.return_value = "mocked-message-id"
        message_sid = send_email("test@example.com", "Test Subject", "Test Body")
        self.assertEqual(message_sid, "mocked-message-id")

    @patch("interfaces.sms_service.send_sms")
    def test_send_sms(self, mock_send_sms):
        mock_send_sms.return_value = "mocked-sms-id"
        message_sid = send_sms("1234567890", "Test SMS Body")
        self.assertEqual(message_sid, "mocked-sms-id")

    @patch("interfaces.whatsapp_service.send_whatsapp_message")
    def test_send_whatsapp_message(self, mock_send_whatsapp):
        mock_send_whatsapp.return_value = "mocked-whatsapp-id"
        message_sid = send_whatsapp_message("9876543210", "Test WhatsApp Message Body")
        self.assertEqual(message_sid, "mocked-whatsapp-id")

    @patch("interfaces.calendar_service.schedule_event")
    def test_schedule_event(self, mock_schedule_event):
        mock_schedule_event.return_value = "https://www.google.com/calendar/event?eid=mocked"
        event = {
            "summary": "Test Event",
            "description": "This is a test event",
            "start": {"dateTime": "2025-02-20T10:00:00Z", "timeZone": "UTC"},
            "end": {"dateTime": "2025-02-20T11:00:00Z", "timeZone": "UTC"}
        }
        event_link = schedule_event(event)
        self.assertIn("https://www.google.com/calendar/event", event_link)

if __name__ == '__main__':
    unittest.main()
