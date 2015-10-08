__author__ = 'pabloholanda'
import settings


def setar_sinal(data):
        if data['sinal']['tipo'] == 'degrau':

            settings.sinal['tipo_sinal'] = 0
            settings.sinal['amp_max'] = data['sinal']['amp_max']
            settings.sinal['offset'] = data['sinal']['offset']

        elif data['sinal']['tipo'] == 'senoidal':
            settings.sinal['tipo_sinal'] = 1
            settings.sinal['amp_max'] = data['sinal']['amp_max']
            settings.sinal['periodo'] = data['sinal']['periodo_max']
            settings.sinal['offset'] = data['sinal']['offset']

        elif data['sinal']['tipo'] == 'quadrada':
            settings.sinal['tipo_sinal'] = 2
            settings.sinal['amp_max'] = data['sinal']['amp_max']
            settings.sinal['periodo'] = data['sinal']['periodo_max']
            settings.sinal['offset'] = data['sinal']['offset']

        elif data['sinal']['tipo'] == 'serra':
            settings.sinal['tipo_sinal'] = 3
            settings.sinal['amp_max'] = data['sinal']['amp_max']
            settings.sinal['duracao'] = data['sinal']['periodo_max']
            settings.sinal['offset'] = data['sinal']['offset']

        elif data['sinal']['tipo'] == 'aleatorio':
            settings.sinal['tipo_sinal'] = 4
            settings.sinal['amp_min'] = data['sinal']['amp_min']
            settings.sinal['amp_max'] = data['sinal']['amp_max']
