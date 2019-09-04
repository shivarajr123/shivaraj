from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import smtplib
email_user = config.EMAIL_ADDRESS1
email_send = config.EMAIL_ADDRESS2
subject = 'python'
import config

msg = MIMEMultipart()
msg['from'] = email_user
msg['from'] = email_send
msg ['subject'] = subject

body = ' hi this in python '
msg.attach(MIMEText(body , 'plain'))
filename = 'shivarajraju597@gmail.com'
attachment = open(filename,'rb')

part MIMEBase
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,config.PASSWORD)

server.sendmail(email_user,email_send,text)
server.quit()