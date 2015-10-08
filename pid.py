__author__ = 'pabloholanda'
import math


def calc_erro(sp, pv):
    return (sp - pv)


def controle_p(Kp, erro):
    return Kp*erro


def controle_i(Ki, h, i, erro):
    return i + (Ki * h * erro)


def controle_d(Kd, h, erro, erro_passado):
    return (Kd*(erro-erro_passado))/h
