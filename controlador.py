__author__ = 'pabloholanda'
import settings
import pid
import sinal


def setar_tensao(t):
    if settings.controle['malha_aberta']:
        if settings.controle['tanque'] == 0:

            settings.tanque['mvtq_1'] = sinal.gerar_sinal(t)
            return settings.tanque['mvtq_1']

        elif settings.controle['tanque'] == 1:

            settings.tanque['mvtq_2'] = sinal.gerar_sinal(t)
            return settings.tanque['mvtq_2']

    else:
        return 0
