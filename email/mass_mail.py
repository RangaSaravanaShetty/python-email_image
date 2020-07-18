import smtplib
from email.message import EmailMessage

from_email = 'skillstech2020@gmail.com'
password = 'mwciuuzrtxbmyxut'

email_list = ['info@skilldisk.com','arunkumarnaa@gmail.com']

for email_id in email_list:
    mes = EmailMessage()
    mes['Subject'] = "Im a Subject"
    mes['From'] = from_email
    mes['To'] = email_id
    mes.set_content(" Im the content of the email.")

    mes.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body  style="text-align: center;">
            <img src="http://skilldisk.com/static/image/sigma.png" alt="Skill-Disk-Logo" style="height: 50px;">
            <h1 style="color:#ffaa00;">Skill Disk</h1>
            <h4 style="color:#2a2a2a;"> Webinar on Automate boring stuff using pyton </h4>
            <br>
            <hr>
            <p>Lorem Ipsum is simply dummy text of the printing 
            and typesetting industry. Lorem Ipsum has been the 
            industry's standard dummy text ever since the 1500s, 
            when an unknown printer took a galley of type and 
            scrambled it to make a type specimen book. It has 
            survived not only five centuries, but also the leap 
            into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset
            sheets containing Lorem Ipsum passages, and more recently 
            with desktop publishing software like Aldus PageMaker 
            including versions of Lorem Ipsum</p>
        </body>
    </html>

    """,subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(from_email,password )

        smtp.send_message(mes)
