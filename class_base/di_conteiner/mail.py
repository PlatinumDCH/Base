from abc import ABC, abstractmethod


class MailProvider(ABC):
    @abstractmethod
    def send(self, to: str, subject: str, message: str):
        pass


class MailgunProvider(MailProvider):
    def send(self, to: str, subject: str, message: str):
        print(f'Sended email to {to} throught Mailgun')

class UnioneProvider(MailProvider):
    def send(self, to: str, subject: str, message: str):
        print(f'Sended email to {to} throught UnioneProvider')


class Mail:
    def __init__(self, provider: MailProvider):
        self._provider = provider
        print('User provider {}'.format(provider.__class__.__name__))
    
    def send(self, to: str, subject: str, message: str):
        self._provider.send(to, subject, message)
