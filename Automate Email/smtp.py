from email.message import EmailMessage
import smtplib
import ssl
import cred

receiver = cred.receiver
sender = cred.sender
password = cred.password

subject = cred.subject
body = cred.body

mail = EmailMessage()
mail["From"] = sender
mail["To"] = receiver
mail["Subject"] = subject
mail.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, mail.as_string())
