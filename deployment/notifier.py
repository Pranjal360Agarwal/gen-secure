import smtplib
from email.mime.text import MIMEText

def send_email_notification(recipient, subject, body):
    sender_email = "example@gmail.com"
    password = "your-email-password"

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = recipient

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient, message.as_string())
        server.quit()
        print("Notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
