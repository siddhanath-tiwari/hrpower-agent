from interfaces.email_service import send_email

def applicant_initiation(applicant_name, email):
    subject = "Application Received"
    body = f"Dear {applicant_name},\n\nThank you for applying. We have received your application and will get back to you soon.\n\nBest regards,\nHR Team"
    send_email(email, subject, body)
    return f"Email sent to {applicant_name} at {email}."