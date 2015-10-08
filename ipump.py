# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import threading
import sys
from time import sleep
import driver
from jsonsocket import Server
import settings, tratar_info

lock = threading.Lock()

class MyThread(threading.Thread):
    def __init__(self, op):
        if op == 0:
            threading.Thread.__init__(self, target=self.ler_altura)
        elif op == 1:
            threading.Thread.__init__(self, target=self.escrever_tensao)
        elif op == 2:
            threading.Thread.__init__(self, target=self.calc_valores)
        else:
            threading.Thread.__init__(self, target=self.conn_supervisorio)
        # Uma flag para notificar a thread de que ela deve parar e dar exit.
        self.kill_received = False

    def ler_altura(self):
        while not self.kill_received:
            lock.acquire()
            tanque = 0
            leitura_tanque = conn.readAD(tanque) * 6.25
            # print 'Tanque 1: %s' % (leitura_tanque)
            lock.release()
            sleep(1)

    def escrever_tensao(self):
        global tensao
        while not self.kill_received:
            lock.acquire()
            canal = 0
            conn.writeDA(canal, tensao)
            # print 'Escrevendo %s em %s' % (tensao, canal)
            lock.release()
            sleep(1)

    def calc_valores(self):
        while not self.kill_received:
            lock.acquire()
            # print 'Calculando...'
            lock.release()
            sleep(1)

    def conn_supervisorio(self):
        # global i, tensao
        while not self.kill_received:
            server.accept()
            data_in = server.recv()
            try:
                 # Ler Variáveis
                 if data_in['comando'] == 0:
                     server.send(tratar_info.enviar_parametros())
                 # Controlar
                 elif data_in['comando'] == 1:
                     tratar_info.setar_tipo_controle(data_in)
            except:
                pass
            # server.send({'sptq_1': 12, "sptq_2": 12, 'pvtq_1': 12,
            #              "pvtq_2": 12, "mvtq_1": 12, "mvtq_2": 12,
            #              "tp": 0, "tr": 0, "ts": 0, "mp": 0, "ess": 0, })
        #     lock.acquire()
        #     if i < 3:
        #         i += 1
        #     if i == 3:
        #         i = 0
        #         tensao += 1
        #     lock.release()
        #     sleep(1)
        # server.send({'response': '2'})


def main():
    global threads
    t = MyThread(0)
    threads.append(t)
    t = MyThread(1)
    threads.append(t)
    t = MyThread(2)
    threads.append(t)
    t = MyThread(3)
    threads.append(t)
    for thread in threads:
        thread.daemon = True
    for thread in threads:
        thread.start()
    while len(threads) > 0:
        # O join basicamente une as threasd para que elas não bloqueiem
        # umas as outras. Filtra-se as threasd que já foram unidas ou
        # retornam None
        threads = [t.join(3) for t in threads if t is not None and t.isAlive()]

if __name__ == '__main__':
    settings.init()

    host = '127.0.0.1'
    port = 8001
    server = Server(host, port)
    threads = []

    i = tensao = 0
    conn = driver.Quanser("localhost", 20081)
    if conn == -1:
        print 'Não foi possível estabelecer uma comunicação.\nRetornou -1'
    else:
        print 'Conectado à planta.'
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print "Ctrl-c recebido! Enviando SIGINT para todas as threads..."
        for t in threads:
            t.kill_received = True
            server.close()
            conn.closeServer()
            sys.exit(0)
