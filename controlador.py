__author__ = 'pabloholanda'
import settings
import pid
import sinal
import travas


def setar_tensao(tempo):
    if settings.tanque['controle'] == 0:
        if settings.controle['malha_aberta']:
            if settings.controle['tanque'] == 0:

                settings.tanque['mvtq_1'] = sinal.gerar_sinal(tempo)
                settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
                return settings.tanque['mvtq_1']

            elif settings.controle['tanque'] == 1:

                settings.tanque['mvtq_2'] = sinal.gerar_sinal(tempo)
                settings.tanque['mvtq_2'] = travas.sequencia_travas(settings.tanque['mvtq_2'])
                return settings.tanque['mvtq_2']

        else:
            return pid.atuar_pid(tempo)
    elif settings.tanque['controle'] == 1:
        pass
