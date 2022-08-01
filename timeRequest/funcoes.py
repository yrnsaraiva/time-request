import requests
import datetime
from prompt_toolkit.validation import Validator, ValidationError
import os


def limpa_tela():
    return os.system('cls')


def hora(timezone):
    url = 'https://worldtimeapi.org/api/timezone/' + timezone

    resposta = requests.get(url)
    hora_actual = datetime.datetime.fromisoformat(resposta.json()['datetime'])

    return hora_actual


def timezone_lst():
    url = 'https://worldtimeapi.org/api/timezone/'
    resposta = requests.get(url)

    return resposta.json()


class TimezoneValidator(Validator):
    def validate(self, document):
        texto = document.text

        if texto not in timezone_lst():
            raise ValidationError(message='Timezone '+texto+' invalid!')
