__author__ = 'pabloholanda'
import settings
import sinal
import pid


def enviar_parametros():
    return settings.tanque


def setar_tipo_controle(data):
    try:
        if data['malha_aberta']:
            sinal.setar_sinal(data)
            print settings.sinal
        else:
            sinal.setar_sinal(data)
            pid.setar_pid(data)
            print settings.sinal
            print settings.controle
    except:
        pass
