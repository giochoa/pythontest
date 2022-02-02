from cgitb import html
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Gio Choa'
email['to'] = 'beautyhealthgojp@gmail.com'
email['subject'] = 'test in python'

email.set_content(html.substitute({'name': 'jacky'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('giochoa0422@gmail.com', 'Faith3:16')
    smtp.send_message(email)
    print('message on the way')