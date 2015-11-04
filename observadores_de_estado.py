import settings


def setar_polos(data):
    settings.observador['polos']['real1'] = data['polos']['real_1']
    settings.observador['polos']['real2'] = data['polos']['real_2']
    settings.observador['polos']['img1'] = data['polos']['img_1']
    settings.observador['polos']['img2'] = data['polos']['img_1']


def setar_ganhos(data):
    settings.observador['ganhos']['ganho1'] = data['ganhos']['ganho_1']
    settings.observador['ganhos']['ganho2'] = data['ganhos']['ganho_2']
