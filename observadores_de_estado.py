import settings
import numpy
import cmath


def setar_polos(data):
    settings.observador['polos']['real1'] = data['polos']['real_1']
    settings.observador['polos']['real2'] = data['polos']['real_2']
    settings.observador['polos']['img1'] = data['polos']['img_1']
    settings.observador['polos']['img2'] = data['polos']['img_2']


def setar_ganhos(data):
    settings.observador['ganhos']['ganho1'] = data['ganhos']['ganho_1']
    settings.observador['ganhos']['ganho2'] = data['ganhos']['ganho_2']


def qc_a():
    A = [0.000344, 0][0.000656, 0.999344]


def calc_polinomio_complexo_conjugado():
    j = cmath.sqrt(-1)
    polinomio = numpy.poly((settings.observador['polos']['real1'] + settings.observador['polos']['img1']*j,
                            settings.observador['polos']['real1'] - settings.observador['polos']['img1']*j))

    return polinomio