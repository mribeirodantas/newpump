from __future__ import division
import settings


def ts(tempo):
    if settings.tanque['flag_ts']:
        if not settings.controle['malha_aberta']:
            if settings.controle['tanque'] == 0:
                if (settings.tanque['sptq_1'] - 1) < settings.tanque['pvtq_1'] < (settings.tanque['sptq_1'] + 1):
                    settings.tanque['flag_ts'] = False
                    settings.tanque['ts'] = tempo
            elif settings.controle['tanque'] == 1 and settings.controle['tipo'] == 'simples':
                if (settings.tanque['sptq_2'] - 1) < settings.tanque['pvtq_2'] < (settings.tanque['sptq_2'] + 1):
                    settings.tanque['flag_ts'] = False
                    settings.tanque['ts'] = tempo


# noinspection PyBroadException
def mp():
    try:
        if settings.tanque['flag_mp']:
            if not settings.controle['malha_aberta']:
                if settings.controle['tanque'] == 0:
                    if settings.tanque['pvtq_1'] >= settings.tanque['pv_passado'] and settings.tanque['pvtq_1'] > 0:
                        settings.tanque['pv_passado'] = settings.tanque['pvtq_1']
                        return 0
                    elif settings.tanque['pvtq_1'] < settings.tanque['pv_passado'] - settings.tanque['pv_passado']*0.02:
                        settings.tanque['flag_mp'] = False
                        settings.tanque['mp'] = ((settings.tanque['pv_passado'] - settings.tanque['sptq_1']) * 100)/ settings.tanque['sptq_1']
                        print settings.tanque['mp'], "%"
                        return 0
                elif settings.controle['tanque'] == 1:
                    if settings.tanque['pvtq_2'] >= settings.tanque['pv_passado']:
                        settings.tanque['pv_passado'] = settings.tanque['pvtq_2']
                        return 0
                    elif settings.tanque['pvtq_2'] < settings.tanque['pv_passado'] - settings.tanque['pv_passado']*0.02:
                        settings.tanque['flag_mp'] = False
                        settings.tanque['mp'] = (settings.tanque['pv_passado'] * 100)/settings.tanque['sptq_2']
                        return 0
    except:
        settings.tanque['flag_mp'] = True
