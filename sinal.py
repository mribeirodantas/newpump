# -*- coding: utf-8 -*-
from __future__ import division
import settings
import math


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

    elif data['sinal']['tipo'] == 'quadrado':
        settings.sinal['tipo_sinal'] = 2
        settings.sinal['amp_max'] = data['sinal']['amp_max']
        settings.sinal['periodo'] = data['sinal']['periodo_max']
        settings.sinal['offset'] = data['sinal']['offset']

    elif data['sinal']['tipo'] == 'serra':
        settings.sinal['tipo_sinal'] = 3
        settings.sinal['amp_max'] = data['sinal']['amp_max']
        settings.sinal['duracao'] = data['sinal']['periodo_max']
        settings.sinal['offset'] = data['sinal']['offset']

    elif data['sinal']['tipo'] == u'aleatório':
        settings.sinal['tipo_sinal'] = 4
        settings.sinal['amp_min'] = data['sinal']['amp_min']
        settings.sinal['amp_max'] = data['sinal']['amp_max']
        settings.sinal['offset'] = data['sinal']['offset']


def gerar_sinal(tempo):
    if settings.sinal['tipo_sinal'] == 0:
        return settings.sinal['offset'] + settings.sinal['amp_max']

    elif settings.sinal['tipo_sinal'] == 1:
        w = 1.0 / settings.sinal['periodo']
        return settings.sinal['offset'] + (settings.sinal['amp_max'] * math.sin(2.0 * math.pi * w * tempo))

    elif settings.sinal['tipo_sinal'] == 2:
        w = 1.0 / settings.sinal['periodo']
        s = settings.sinal['amp_max'] * math.sin(2.0 * math.pi * w * tempo)

        if s > 0:
            return settings.sinal['offset'] + settings.sinal['amp_max']
        elif s < 0:
            return settings.sinal['offset'] + (-1 * settings.sinal['amp_max'])

    elif settings.sinal['tipo_sinal'] == 3:
        return settings.sinal['offset'] + (2 * settings.sinal['amp_max'] *
                                           ((tempo / settings.sinal['duracao']) - math.floor(
                                               tempo / settings.sinal['duracao'])) -
                                           settings.sinal['amp_max'])

        # elif settings.sinal['tipo_sinal'] == 4:
        #     sinal = sinais.sinalAleatorio(amp_min, amp_max)
        #     return sinal
