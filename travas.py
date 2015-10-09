__author__ = 'pabloholanda'
import settings


def trava(vp):
    if -4 <= vp <= 4:
        return vp
    elif vp > 4.00:
        return 4
    elif vp < -4:
        return -4.00


def trava_alto_nivel(vp):
    if settings.tanque['pvtq_1'] > 28 and vp > 3.15:
        return 3.15
    else:
        return vp


def trava_muito_nivel(vp):
    if (settings.tanque['pvtq_1'] > 29.00) and (vp > 0):
        return 0.0
    else:
        return vp


def trava_nivel_baixo(vp):
    if (settings.tanque['pvtq_1'] < 4.00) and (vp < 0):
        return 0
    else:
        return vp



def sequencia_travas(vp):
    vp = trava(vp)
    vp = trava_alto_nivel(vp)
    vp = trava_muito_nivel(vp)
    vp = trava_nivel_baixo(vp)
    return vp

