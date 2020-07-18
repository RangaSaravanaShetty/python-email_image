import smtplib
from email.message import EmailMessage

from_email = 'From@gmail.com'
password = 'password'

mes = EmailMessage()
mes['Subject'] = "Im a Subject"
mes['From'] = from_email
mes['To'] = 'info@skilldisk.com'
mes.set_content(" Im the content of the email.")

with open('banner.png','rb') as f:
    attachment_data = f.read()

mes.add_attachment(attachment_data, maintype='image', subtype='png', filename='Webinar.png')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(from_email,password )

    smtp.send_message(mes)


