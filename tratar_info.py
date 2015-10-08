__author__ = 'pabloholanda'
import settings


def enviar_parametros():
    return settings.tanque


def setar_tipo_controle(data):
    try:
        if data['malha_aberta']:
            print "malha aberta"
        else:
            print "malha fechada"
    except:
        pass
