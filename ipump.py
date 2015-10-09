# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import threading
import sys
from time import sleep
import driver
from jsonsocket import Server
import settings
import tratar_info
import controlador

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
            settings.tanque['pvtq_1'] = conn.readAD(0) * 6.25
            settings.tanque['pvtq_2'] = conn.readAD(1) * 6.25
            lock.release()
            sleep(0.06)

    def escrever_tensao(self):
        tempo = 0.1
        tensao = 0.00
        while not self.kill_received:
            lock.acquire()
            tensao = controlador.setar_tensao(tempo)
            conn.writeDA(0, tensao)
            tempo += 0.1
            lock.release()
            sleep(0.1)

    def calc_valores(self):
        while not self.kill_received:
            lock.acquire()
            # print 'Calculando...'
            lock.release()
            sleep(1)

    def conn_supervisorio(self):
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
