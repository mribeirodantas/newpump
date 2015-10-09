__author__ = 'pabloholanda'


def init():
    global tanque, sinal, controle
    tanque = {
        'pvtq_1': 0.00,
        'pvtq_2': 0.00,
        'mvtq_1': 0.00,
        'mvtq_2': 0.00,
        'sptq_1': 0.00,
        'sptq_2': 0.00,
        'erro_passado': 0.00,
        'tp': 0,
        'tr': 0,
        'ts': 0,
        'mp': 0,
        'ess': 0
    }

    sinal = {
        'tipo_sinal': 0,
        'deslocamento': 0,
        'periodo': 0,
        'amp_min': 0,
        'amp_max': 0.00,
        'offset': 0,
        'duracao': 0
    }

    controle = {
        'tipo': 'simples',
        'tanque': 0,
        'malha_aberta': True,
        'controle_1': {
            'tipo': 0,
            'Kp': 0.000,
            'Ki': 0.000,
            'Kd': 0.000,
            'P': 0.000,
            'I': 0.000,
            'D': 0.000
        },
        'controle_2': {
            'tipo': 0,
            'Kp': 0.000,
            'Ki': 0.000,
            'Kd': 0.000,
            'P': 0.000,
            'I': 0.000,
            'D': 0.000
        }
    }
