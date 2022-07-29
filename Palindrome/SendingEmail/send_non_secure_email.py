# OR the the unencripted, then encripted method
import smtplib, ssl
smtp_server = 'smtp.outlook.com'
port = 587

sender = 'my_email_account@outlook.com'
password = input("Enter your password here: ")
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    print("It worked!")
except Exception as e:
    print(e)
finally:
    server.quit()