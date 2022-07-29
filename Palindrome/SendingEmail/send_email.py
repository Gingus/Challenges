# Input(reciever email address, Subjust line, message body)
# send email with python, using smtplib
# SSL = Secure Sockets Layer
# TLS = Transport Layer Security

import smtplib, ssl
smtp_server = 'smtp.outlook.com'
port = 465

sender = 'my_email_account@outlook.com'
password = input("Enter your password here: ")
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print("It worked!")
# reciever_email = 'pminard@criticalsoftware.com'
# server.quit()
