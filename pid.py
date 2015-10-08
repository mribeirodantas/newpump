__author__ = 'pabloholanda'
import settings

def calc_erro(sp, pv):
    return (sp - pv)


def controle_p(Kp, erro):
    return Kp*erro


def controle_i(Ki, h, i, erro):
    return i + (Ki * h * erro)


def controle_d(Kd, h, erro, erro_passado):
    return (Kd*(erro-erro_passado))/h


def setar_pid(data):
    settings.tanque['tanque'] = data['tanque']

    if data['controle']['tipo'] == 'P':
        settings.controle['Kp'] = data['controle']['Kp']
        settings.controle['tipo'] = 1
    elif data['controle']['tipo'] == 'PI':
        settings.controle['Kp'] = data['controle']['Kp']
        settings.controle['Ki'] = data['controle']['Ki']
        settings.controle['tipo'] = 2
    elif data['controle']['tipo'] == 'PD':
        settings.controle['Kp'] = data['controle']['Kp']
        settings.controle['Kd'] = data['controle']['Kd']
        settings.controle['tipo'] = 3
    elif data['controle']['tipo'] == 'PID':
        settings.controle['Kp'] = data['controle']['Kp']
        settings.controle['Ki'] = data['controle']['Ki']
        settings.controle['Kd'] = data['controle']['Kd']
        settings.controle['tipo'] = 4
    elif data['controle']['tipo'] == 'PI-D':
        settings.controle['Kp'] = data['controle']['Kp']
        settings.controle['Ki'] = data['controle']['Ki']
        settings.controle['Kd'] = data['controle']['Kd']
        settings.controle['tipo'] = 5
