import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration, ref for smtp hakim [vivobook] C:\data\test\python\email
SMTP_SERVER = "mail.example.co.id"  # Replace with your SMTP server
SMTP_PORT = 587                   # Replace with your SMTP port
USERNAME = "hakim@example.co.id"  # Your email
PASSWORD = "password"           # Your email password
TO_EMAIL = "hafiz@example.co.id"   # Recipient's email

JSON_FILE = "data.json"  # Path to your JSON file

def check_json_condition():
    try:
        with open(JSON_FILE, 'r') as file:
            data = json.load(file)
        # Example condition: Check if `status` key is `true`
        return data.get('status') is True
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return False

def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = TO_EMAIL
        msg['Subject'] = "SUBJECT"
        body = "The condition in the JSON file is met. This is an automated alert."
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(USERNAME, PASSWORD)
            server.sendmail(USERNAME, TO_EMAIL, msg.as_string())
        print(f"Email sent to {TO_EMAIL}")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    if check_json_condition():
        send_email()
    else:
        print("Condition not met; no email sent.")
