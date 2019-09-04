from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
email_user = config.EMAIL_ADDRESS1
email_send = config.EMAIL_ADDRESS2
subject = 'python'
import config

def send_mail(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS1,config.PASSWORD)
        message = "subject:{}\n\n{}".format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS1,config.EMAIL_ADDRESS2,message)
        server.quit()
        print("mail has sent successfully")
    except:
        print("Email failed to send")

subject = 'Test subject'

msg = "Hi this is Shivaraj from davanagere"

send_mail(subject,msg)