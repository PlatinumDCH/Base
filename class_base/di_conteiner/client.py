from class_base.di_conteiner.confgi import container
from class_base.di_conteiner.mail import Mail, MailProvider


def run():
    mail_provider = container.resolve(MailProvider)
    Mail(mail_provider).send(
        to='hello@example.ua',
        subject='Hello',
        message='How are you?!'
    )