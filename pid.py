__author__ = 'pabloholanda'
import settings
import sinal
import travas

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


def controlador_externo(tempo):
    if settings.controle['controle_1']['tipo'] == 1:

        settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
        erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
        settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
        settings.tanque['mvtq_2'] = settings.controle['controle_1']['P']
        return settings.tanque['mvtq_2']

    elif settings.controle['controle_1']['tipo'] == 2:

        settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
        erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
        settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
        settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                          settings.controle['controle_1']['I'], erro)
        settings.tanque['mvtq_2'] = settings.controle['controle_1']['P'] + settings.controle['controle_1']['I']
        return settings.tanque['mvtq_2']

    elif settings.controle['controle_1']['tipo'] == 3:

        settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
        erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
        settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
        settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                          settings.tanque['erro_passado'])
        settings.tanque['erro_passado'] = erro
        settings.tanque['mvtq_2'] = settings.controle['controle_1']['P'] + settings.controle['controle_1']['D']
        return settings.tanque['mvtq_2']

    elif settings.controle['controle_1']['tipo'] == 4:

        settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
        erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
        settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
        settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                          settings.controle['controle_1']['I'], erro)
        settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                          settings.tanque['erro_passado'])
        settings.tanque['erro_passado'] = erro
        settings.tanque['mvtq_2'] = settings.controle['controle_1']['P'] +\
                                    settings.controle['controle_1']['I'] + settings.controle['controle_1']['D']
        return settings.tanque['mvtq_2']

    elif settings.controle['controle_1']['tipo'] == 5:

        settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
        erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
        settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
        settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                          settings.controle['controle_1']['I'], erro)
        settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                          settings.tanque['erro_passado'])
        settings.tanque['erro_passado'] = erro
        settings.tanque['mvtq_2'] = settings.controle['controle_1']['P'] +\
                                    settings.controle['controle_1']['I'] - settings.controle['controle_1']['D']
        return settings.tanque['mvtq_2']


def controlador_interno(sp):
    if settings.controle['controle_2']['tipo'] == 1:

        settings.tanque['sptq_1'] = sp
        erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
        settings.controle['controle_2']['P'] = controle_p(settings.controle['controle_2']['Kp'], erro)
        settings.tanque['mvtq_1'] = settings.controle['controle_2']['P']
        settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
        return settings.tanque['mvtq_1']

    elif settings.controle['controle_2']['tipo'] == 2:

        settings.tanque['sptq_1'] = sp
        erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
        settings.controle['controle_2']['P'] = controle_p(settings.controle['controle_2']['Kp'], erro)
        settings.controle['controle_2']['I'] = controle_i(settings.controle['controle_2']['Ki'], 0.1,
                                                          settings.controle['controle_2']['I'], erro)
        settings.tanque['mvtq_1'] = settings.controle['controle_2']['P'] + settings.controle['controle_2']['I']
        settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
        return settings.tanque['mvtq_1']

    elif settings.controle['controle_2']['tipo'] == 3:

        settings.tanque['sptq_1'] = sp
        erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
        settings.controle['controle_2']['P'] = controle_p(settings.controle['controle_2']['Kp'], erro)
        settings.controle['controle_2']['D'] = controle_d(settings.controle['controle_2']['Kd'], 0.1, erro,
                                                          settings.tanque['erro_passado'])
        settings.tanque['erro_passado'] = erro
        settings.tanque['mvtq_1'] = settings.controle['controle_2']['P'] + settings.controle['controle_2']['D']
        settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
        return settings.tanque['mvtq_1']

    elif settings.controle['controle_2']['tipo'] == 4:

        settings.tanque['sptq_1'] = sp
        erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
        settings.controle['controle_2']['P'] = controle_p(settings.controle['controle_2']['Kp'], erro)
        settings.controle['controle_2']['I'] = controle_i(settings.controle['controle_2']['Ki'], 0.1,
                                                          settings.controle['controle_2']['I'], erro)
        settings.controle['controle_2']['D'] = controle_d(settings.controle['controle_2']['Kd'], 0.1, erro,
                                                          settings.tanque['erro_passado'])
        settings.tanque['erro_passado'] = erro
        settings.tanque['mvtq_1'] = settings.controle['controle_2']['P'] +\
                                    settings.controle['controle_2']['I'] + settings.controle['controle_2']['D']
        settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
        return settings.tanque['mvtq_1']

    elif settings.controle['controle_2']['tipo'] == 5:

        settings.tanque['sptq_1'] = sp
        erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
        settings.controle['controle_2']['P'] = controle_p(settings.controle['controle_2']['Kp'], erro)
        settings.controle['controle_2']['I'] = controle_i(settings.controle['controle_2']['Ki'], 0.1,
                                                          settings.controle['controle_2']['I'], erro)
        settings.controle['controle_2']['D'] = controle_d(settings.controle['controle_2']['Kd'], 0.1, erro,
                                                          settings.tanque['erro_passado'])
        settings.tanque['erro_passado'] = erro
        settings.tanque['mvtq_1'] = settings.controle['controle_2']['P'] +\
                                    settings.controle['controle_2']['I'] - settings.controle['controle_2']['D']
        settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
        return settings.tanque['mvtq_1']


def atuar_pid(tempo):
    if settings.controle['tipo'] == 'simples':
        if settings.controle['tanque'] == 0:
            if settings.controle['controle_1']['tipo'] == 1:

                settings.tanque['sptq_1'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.tanque['mvtq_1'] = settings.controle['controle_1']['P']
                settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
                return settings.tanque['mvtq_1']

            elif settings.controle['controle_1']['tipo'] == 2:

                settings.tanque['sptq_1'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                                  settings.controle['controle_1']['I'], erro)
                settings.tanque['mvtq_1'] = settings.controle['controle_1']['P'] + settings.controle['controle_1']['I']
                settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
                return settings.tanque['mvtq_1']

            elif settings.controle['controle_1']['tipo'] == 3:

                settings.tanque['sptq_1'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                                  settings.tanque['erro_passado'])
                settings.tanque['erro_passado'] = erro
                settings.tanque['mvtq_1'] = settings.controle['controle_1']['P'] + settings.controle['controle_1']['D']
                settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
                return settings.tanque['mvtq_1']

            elif settings.controle['controle_1']['tipo'] == 4:

                settings.tanque['sptq_1'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                                  settings.controle['controle_1']['I'], erro)
                settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                                  settings.tanque['erro_passado'])
                settings.tanque['erro_passado'] = erro
                settings.tanque['mvtq_1'] = settings.controle['controle_1']['P'] +\
                                            settings.controle['controle_1']['I'] + settings.controle['controle_1']['D']
                settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
                return settings.tanque['mvtq_1']

            elif settings.controle['controle_1']['tipo'] == 5:

                settings.tanque['sptq_1'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_1'], settings.tanque['pvtq_1'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                                  settings.controle['controle_1']['I'], erro)
                settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                                  settings.tanque['erro_passado'])
                settings.tanque['erro_passado'] = erro
                settings.tanque['mvtq_1'] = settings.controle['controle_1']['P'] +\
                                            settings.controle['controle_1']['I'] - settings.controle['controle_1']['D']
                settings.tanque['mvtq_1'] = travas.sequencia_travas(settings.tanque['mvtq_1'])
                return settings.tanque['mvtq_1']
        else:
            if settings.controle['controle_1']['tipo'] == 1:

                settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.tanque['mvtq_2'] = settings.controle['controle_1']['P']
                settings.tanque['mvtq_2'] = travas.sequencia_travas(settings.tanque['mvtq_2'])
                return settings.tanque['mvtq_2']

            elif settings.controle['controle_1']['tipo'] == 2:

                settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                                  settings.controle['controle_1']['I'], erro)
                settings.tanque['mvtq_2'] = settings.controle['controle_1']['P'] + settings.controle['controle_1']['I']
                settings.tanque['mvtq_2'] = travas.sequencia_travas(settings.tanque['mvtq_2'])
                return settings.tanque['mvtq_2']

            elif settings.controle['controle_1']['tipo'] == 3:

                settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                                  settings.tanque['erro_passado'])
                settings.tanque['erro_passado'] = erro
                settings.tanque['mvtq_2'] = settings.controle['controle_1']['P'] + settings.controle['controle_1']['D']
                settings.tanque['mvtq_2'] = travas.sequencia_travas(settings.tanque['mvtq_2'])
                return settings.tanque['mvtq_2']

            elif settings.controle['controle_1']['tipo'] == 4:

                settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                                  settings.controle['controle_1']['I'], erro)
                settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                                  settings.tanque['erro_passado'])
                settings.tanque['erro_passado'] = erro
                settings.tanque['mvtq_2'] = settings.controle['controle_1']['P'] +\
                                            settings.controle['controle_1']['I'] + settings.controle['controle_1']['D']
                settings.tanque['mvtq_2'] = travas.sequencia_travas(settings.tanque['mvtq_2'])
                return settings.tanque['mvtq_2']

            elif settings.controle['controle_1']['tipo'] == 5:

                settings.tanque['sptq_2'] = sinal.gerar_sinal(tempo)
                erro = calc_erro(settings.tanque['sptq_2'], settings.tanque['pvtq_2'])
                settings.controle['controle_1']['P'] = controle_p(settings.controle['controle_1']['Kp'], erro)
                settings.controle['controle_1']['I'] = controle_i(settings.controle['controle_1']['Ki'], 0.1,
                                                                  settings.controle['controle_1']['I'], erro)
                settings.controle['controle_1']['D'] = controle_d(settings.controle['controle_1']['Kd'], 0.1, erro,
                                                                  settings.tanque['erro_passado'])
                settings.tanque['erro_passado'] = erro
                settings.tanque['mvtq_2'] = settings.controle['controle_1']['P'] +\
                                            settings.controle['controle_1']['I'] - settings.controle['controle_1']['D']
                settings.tanque['mvtq_2'] = travas.sequencia_travas(settings.tanque['mvtq_2'])
                return settings.tanque['mvtq_2']

    elif settings.controle['tipo'] == 'cascata':
        return controlador_interno(controlador_externo(tempo))
