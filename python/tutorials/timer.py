""" Timer example.
"""

import sys
import time
import threading

def hello(event, count):
    print('hello %d' % (count))
    event.set()

def main():

    count = 0
    while count < 10:
        e = threading.Event()
        t = threading.Timer(1.0, hello, args=(e, count))
        t.start()
        e.wait()
        count += 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

