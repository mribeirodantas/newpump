__author__ = 'pabloholanda'
import settings
import pid
import sinal


def setar_tensao(t):
    if settings.controle['malha_aberta']:
        return sinal.gerar_sinal(t)
    else:
        return 0
