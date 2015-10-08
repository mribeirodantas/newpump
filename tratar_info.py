__author__ = 'pabloholanda'
import settings
import sinal


def enviar_parametros():
    return settings.tanque


def setar_tipo_controle(data):
    try:
        if data['malha_aberta']:
            sinal.setar_sinal(data)
            print settings.sinal
        else:
            sinal.setar_sinal(data)
    except:
        pass
