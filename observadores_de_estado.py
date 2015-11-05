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


    settings.observador['polinomio'] = polinomio


def calc_polinomio_real():
    polinomio = numpy.poly((settings.observador['polos']['real1'],
                            settings.observador['polos']['real2']))

    settings.observador['polinomio'] = polinomio

def calc_polinomio_real_complexo():
    j = cmath.sqrt(-1)
    polinomio = numpy.poly((settings.observador['polos']['real1'] + settings.observador['polos']['img_1']*j,
                            settings.observador['polos']['real2']))

    settings.observador['polinomio'] = polinomio


def calc_polinomio_complexos():
    j = cmath.sqrt(-1)
    polinomio = numpy.poly((settings.observador['polos']['real1'] + settings.observador['polos']['img_1']*j,
                            settings.observador['polos']['real2'] + settings.observador['polos']['img_2']*j))

    settings.observador['polinomio'] = polinomio


def calc_ql():
    ql = 0
    g = numpy.array([[0.999344, 0], [0.000656, 0.999344]])

    for i, valor in enumerate(list(reversed(settings.observador['polinomio']))):
        if i == 0:
            ql += valor
        else:
            ql = ql + valor*numpy.linalg.matrix_power(g, i)

    settings.observador['ql'] = ql

    return ql


def calc_wo():
    wo_inv = numpy.array([-1523.39, 1524.39], [1524.39, -1524.39])
    settings.observador['wo'] = numpy.dot(wo_inv, numpy.array([[0], [1]]))

    return wo_inv


def calc_l():
    settings.observador['l'] = numpy.dot(calc_ql(), calc_wo())


def calc_x():
    g = numpy.array([[0.999344, 0], [0.000656, 0.999344]])
    part_1 = numpy.dot(g, settings.observador['x'])

