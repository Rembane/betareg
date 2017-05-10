#!/usr/bin/env python3

"""Runs the program on the board.
"""

import queue, subprocess, sys
from threading import Thread

# http://stackoverflow.com/questions/375427/non-blocking-read-on-a-subprocess-pipe-in-python

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

def main():
    p = subprocess.Popen(['rshell', 'repl', '~', 'import main'], stdout=subprocess.PIPE, bufsize=1)
    q = queue.Queue()
    t = Thread(target=enqueue_output, args=(p.stdout, q), daemon=True)
    t.start()
    while True:
        try:
            line = q.get(timeout=0.5)
        except queue.Empty:
            pass
        else:
            print('Got data', line)

if __name__ == '__main__':
    main()
