# -*- coding: utf-8 -*-

import sys
import threading
import time
import driver

lock = threading.Lock()
threads = []


class Leitor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # Uma flag para notificar a thread de que ela deve parar e dar exit.
        self.kill_received = False

    def run(self):
        with lock:  # Adquire o lock e quando terminar libera.
            while not self.kill_received:
                self.ler_altura()

    def ler_altura(self):
        tanque1 = conn.readAD(0) * 6.25
        tanque2 = conn.readAD(1) * 6.25
        print 'Tanque 1/2: %s/%s' % (tanque1, tanque2)
        time.sleep(1)


def main(args):
    global threads
    # Uma thread para ler e uma para escrever
    for i in range(2):
        t = Leitor()
        threads.append(t)
        t.daemon = True
        t.start()

    while len(threads) > 0:
        # O join basicamente une as threasd para que elas não bloqueiem
        # umas as outras. Filtra-se as threasd que já foram unidas ou
        # retornam None
        threads = [t.join(1) for t in threads if t is not None and t.isAlive()]

if __name__ == '__main__':
    conn = driver.Quanser("localhost", 20081)
    if conn == -1:
        print 'Não foi possível estabelecer uma comunicação.\nRetornou -1'
    else:
        print 'Conectado à planta.'
    while True:
        try:
            main(sys.argv)
        except KeyboardInterrupt:
            print "Ctrl-c recebido! Enviando SIGINT para todas as threads..."
            for t in threads:
                t.kill_received = True
                sys.exit(0)
