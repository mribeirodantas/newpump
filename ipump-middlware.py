# -*- coding: utf-8 -*-

import sys
import threading
import time

i = 0  # Recurso compartilhado pelas threads

lock = threading.Lock()


class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # Uma flag para notificar a thread de que ela deve parar e dar exit.
        self.kill_received = False

    def run(self):
        with lock:  # Adquire o lock e quando terminar libera.
            while not self.kill_received:
                self.do_something()

    def do_something(self):
        global i
        i += 1
        print i
        time.sleep(1)


def main(args):
    threads = []
    for i in range(10):
        t = Worker()
        threads.append(t)
        t.start()

    while len(threads) > 0:
        try:
            # O join basicamente une as threasd para que elas não bloqueiem
            # umas as outras. Filtra-se as threasd que já foram unidas ou
            # retornam None
            threads = [t.join(1) for t in threads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print "Ctrl-c received! Sending kill to threads..."
            for t in threads:
                t.kill_received = True

if __name__ == '__main__':
    main(sys.argv)
