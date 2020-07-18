import smtplib

from_email = 'From@gmail.com'
password = 'password'

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()

    smtp.login(from_email, password)

    message = "Subject: First test mail from Webinar session \n\n This is the content of the email body"

    # message = '''Subject: First test mail with multi line string. \n\n
    #  
    #     This is the content of the email body.
    # 
    #     You can write any connect in this part.
    #
    # '''

    smtp.sendmail(from_email,'info@skilldisk.com', message)

