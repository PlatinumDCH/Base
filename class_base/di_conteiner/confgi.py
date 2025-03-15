import punq

from class_base.di_conteiner.mail import MailProvider, UnioneProvider

container = punq.Container()
container.register(MailProvider, instance=UnioneProvider())