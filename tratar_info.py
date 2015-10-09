__author__ = 'pabloholanda'
import settings
import sinal
import pid


def enviar_parametros():
    return settings.tanque


def setar_tipo_controle(data):
    try:
        if data['malha_aberta']:
            settings.controle['malha_aberta'] = True
            if data['tanque'] == 0:
                settings.controle['tanque'] = 0
                settings.tanque['mvtq_2'] = 0.00
            else:
                settings.controle['tanque'] = 1
                settings.tanque['mvtq_1'] = 0.00

            sinal.setar_sinal(data)
            print settings.sinal

        else:
            sinal.setar_sinal(data)
            pid.setar_pid(data)
            settings.controle['malha_aberta'] = False
            print settings.sinal
            print settings.controle
    except:
        pass
