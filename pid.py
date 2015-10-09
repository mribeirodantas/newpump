__author__ = 'pabloholanda'
import settings
import sinal


def calc_erro(sp, pv):
    return (sp - pv)


def controle_p(Kp, erro):
    return Kp*erro


def controle_i(Ki, h, i, erro):
    return i + (Ki * h * erro)


def controle_d(Kd, h, erro, erro_passado):
    return (Kd*(erro-erro_passado))/h


def setar_pid(data):

    settings.controle['tipo'] = data['controlador']['tipo']
    settings.controle['tanque'] = data['tanque']

    if settings.controle['tipo'] == 'simples':

        if data['controlador']['controle_1']['tipo'] == 'P':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['tipo'] = 1

        elif data['controlador']['controle_1']['tipo'] == 'PI':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['Ki'] = data['controlador']['controle_1']['Ki']
            settings.controle['controle_1']['tipo'] = 2

        elif data['controlador']['controle_1']['tipo'] == 'PD':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['Kd'] = data['controlador']['controle_1']['Kd']
            settings.controle['controle_1']['tipo'] = 3

        elif data['controlador']['controle_1']['tipo'] == 'PID':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['Ki'] = data['controlador']['controle_1']['Ki']
            settings.controle['controle_1']['Kd'] = data['controlador']['controle_1']['Kd']
            settings.controle['controle_1']['tipo'] = 4

        elif data['controlador']['controle_1']['tipo'] == 'PI-D':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['Ki'] = data['controlador']['controle_1']['Ki']
            settings.controle['controle_1']['Kd'] = data['controlador']['controle_1']['Kd']
            settings.controle['controle_1']['tipo'] = 5

    elif settings.controle['tipo'] == 'cascata':

        if data['controlador']['controle_1']['tipo'] == 'P':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['tipo'] = 1

        elif data['controlador']['controle_1']['tipo'] == 'PI':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['Ki'] = data['controlador']['controle_1']['Ki']
            settings.controle['controle_1']['tipo'] = 2

        elif data['controlador']['controle_1']['tipo'] == 'PD':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['Kd'] = data['controlador']['controle_1']['Kd']
            settings.controle['controle_1']['tipo'] = 3

        elif data['controlador']['controle_1']['tipo'] == 'PID':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['Ki'] = data['controlador']['controle_1']['Ki']
            settings.controle['controle_1']['Kd'] = data['controlador']['controle_1']['Kd']
            settings.controle['controle_1']['tipo'] = 4

        elif data['controlador']['controle_1']['tipo'] == 'PI-D':

            settings.controle['controle_1']['Kp'] = data['controlador']['controle_1']['Kp']
            settings.controle['controle_1']['Ki'] = data['controlador']['controle_1']['Ki']
            settings.controle['controle_1']['Kd'] = data['controlador']['controle_1']['Kd']
            settings.controle['controle_1']['tipo'] = 5

        # Configurar segundo controlador

        if data['controlador']['controle_2']['tipo'] == 'P':

            settings.controle['controle_2']['Kp'] = data['controlador']['controle_2']['Kp']
            settings.controle['controle_2']['tipo'] = 1

        elif data['controlador']['controle_2']['tipo'] == 'PI':

            settings.controle['controle_2']['Kp'] = data['controlador']['controle_2']['Kp']
            settings.controle['controle_2']['Ki'] = data['controlador']['controle_2']['Ki']
            settings.controle['controle_2']['tipo'] = 2

        elif data['controlador']['controle_2']['tipo'] == 'PD':

            settings.controle['controle_2']['Kp'] = data['controlador']['controle_2']['Kp']
            settings.controle['controle_2']['Kd'] = data['controlador']['controle_2']['Kd']
            settings.controle['controle_2']['tipo'] = 3

        elif data['controlador']['controle_2']['tipo'] == 'PID':

            settings.controle['controle_2']['Kp'] = data['controlador']['controle_2']['Kp']
            settings.controle['controle_2']['Ki'] = data['controlador']['controle_2']['Ki']
            settings.controle['controle_2']['Kd'] = data['controlador']['controle_2']['Kd']
            settings.controle['controle_2']['tipo'] = 4

        elif data['controlador']['controle_2']['tipo'] == 'PI-D':

            settings.controle['controle_2']['Kp'] = data['controlador']['controle_2']['Kp']
            settings.controle['controle_2']['Ki'] = data['controlador']['controle_2']['Ki']
            settings.controle['controle_2']['Kd'] = data['controlador']['controle_2']['Kd']
            settings.controle['controle_2']['tipo'] = 5


def atuar_pid(tempo):
    if settings.controle['tipo'] == 'simples':
        if settings.controle['tanque'] == 0:
            if settings.controle['controle_1']['tipo'] == 1:
                sinal_pid = sinal.gerar_sinal(tempo)
                erro = calc_erro(sinal, settings.tanque['pvtq_1'])
                P = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.tanque['mvtq_1'] = P
        else:
            return 0
