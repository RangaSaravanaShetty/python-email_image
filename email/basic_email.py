import smtplib

"""
    The smtplib module defines an SMTP client session 
    object that can be used to send mail to any 
    Internet machine with an SMTP or ESMTP listener daemon.
"""

from_email = 'From@gmail.com'
password = 'password'

smtp = smtplib.SMTP('smtp.gmail.com',587)

smtp.ehlo()
smtp.starttls()
smtp.ehlo()

smtp.login(from_email,password)

message = "Subject: First test mail from Webinar session \n\n This is the content of the email body"

# message = '''Subject: First test mail with multi line string. \n\n
#  
#     This is the content of the email body.
# 
#     You can write any connect in this part.
#
# '''

smtp.sendmail(from_email,'info@skilldisk.com', message)
smtp.quit()
