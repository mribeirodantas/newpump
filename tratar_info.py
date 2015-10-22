__author__ = 'pabloholanda'
import settings
import sinal
import pid


def enviar_parametros():
    return {
        'pvtq_1': settings.tanque['pvtq_1'],
        'pvtq_2': settings.tanque['pvtq_2'],
        'mvtq_1': settings.tanque['mvtq_1'],
        'mvtq_2': settings.tanque['mvtq_2'],
        'sptq_1': settings.tanque['sptq_1'],
        'sptq_2': settings.tanque['sptq_2'],
        'erro_passado': settings.tanque['erro_passado'],
        'tp': settings.tanque['tp'],
        'tr': settings.tanque['tr'],
        'ts': settings.tanque['ts'],
        'mp': settings.tanque['mp'],
        'ess': settings.tanque['ess'],
        'P_master': settings.controle['controle_1']['P'],
        'I_master': settings.controle['controle_1']['I'],
        'D_master': settings.controle['controle_1']['D'],
        'P_slave': settings.controle['controle_2']['P'],
        'I_slave': settings.controle['controle_2']['I'],
        'D_slave': settings.controle['controle_2']['D']
    }


def setar_tipo_controle(data):
    try:
        settings.tanque['tempo'] = 0.0
        settings.tanque['flag_ts'] = True
        settings.tanque['flag_mp'] = True
        settings.tanque['pv_passado'] = -40
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
    except:
        pass
