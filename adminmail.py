import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def adminsendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('mallabhargavi157@gmail.com','orwpkttgyhlezfuv')
    msg=EmailMessage()
    msg['From']='mallabhargavi157@gmail.com'
    msg['Subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
