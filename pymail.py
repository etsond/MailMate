# Emal you are sending from
from email.message import EmailMessage
# from pyPassword import password
import ssl
import smtplib
import os

from dotenv import load_dotenv
load_dotenv()


send_email = os.getenv("send_email")
pass_word = os.getenv("password")

user = 'felehig814@minterp.com'

subject = 'testing to see if it works'

body = "If this works for you please let me know"

em = EmailMessage()
# sending from
em['From'] = send_email
em['To'] = user
em['subject'] = subject
# content of the email is the body
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    # loggin in with the email sender
    smtp.login(send_email, pass_word)
    # loggin in with the credentials & converting the email
    smtp.sendmail(send_email, user, em.as_string())
