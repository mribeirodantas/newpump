# -*- coding: utf-8 -*-

import sys
import threading
import time

i = 0  # Recurso compartilhado pelas threads


class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
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
            # O join basicamente une as threasd para que elas não bloqueiem
            # umas as outras. Filtra-se as threasd que já foram unidas ou
            # retornam None
            threads = [t.join(1) for t in threads if t is not None and t.isAlive()]

if __name__ == '__main__':
    main(sys.argv)
