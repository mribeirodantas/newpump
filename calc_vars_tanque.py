__author__ = 'pabloholanda'
import settings


def ts(tempo):
    if settings.tanque['flag_ts']:
        if not settings.controle['malha_aberta']:
            if settings.controle['tanque'] == 0 and settings.controle['tipo'] == 'simples':
                if (settings.tanque['sptq_1'] - 1) < settings.tanque['pvtq_1'] < (settings.tanque['sptq_1'] + 1):
                    settings.tanque['flag_ts'] = False
                    settings.tanque['ts'] = tempo
                    print settings.tanque['ts']
            elif settings.controle['tanque'] == 1 and settings.controle['tipo'] == 'simples':
                if (settings.tanque['sptq_2'] - 1) < settings.tanque['pvtq_2'] < (settings.tanque['sptq_2'] + 1):
                    settings.tanque['flag_ts'] = False
                    settings.tanque['ts'] = tempo
                    print settings.tanque['ts']

