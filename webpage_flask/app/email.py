from flask_mail import Message
from app import mail, mail_settings


def send_email(user):
    msg = Message(f"Form received from {user.name}", sender=mail_settings['MAIL_USERNAME'],
                  recipients=['moh.nov16@gmail.com'])
    msg.body = 'text body'
    msg.html = f"{user.message}"
    mail.send(msg)
