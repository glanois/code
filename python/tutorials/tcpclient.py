""" Example TCP client.
"""

import logging
import sys
import argparse
import time
import threading

import lib.network

def timer_callback(event):
    event.set()
        
def main(options):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    t = lib.network.TcpClient()
    t.connect(options.address[0], int(options.port[0]))
    logging.info('main() connected to %s:%d' % (options.address[0], int(options.port[0])))

    while True:
        t.sendall('ping'.encode('utf-8'))
        logging.info('main() - sent: ping')

        response = ''
        while response != 'pong':
            fragment = t.recv(16)
            if len(fragment) > 0:
                fragment = fragment.decode('ascii').rstrip()
                response += fragment
        logging.info('main() - got:  pong')

        e = threading.Event()
        timer = threading.Timer(1.0, timer_callback, (e,))
        timer.start()
        e.wait()

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'address',
        help='Address of the server.',
        nargs=1)

    parser.add_argument(
        'port',
        help='Port number of the server.',
        nargs=1)

    options = parser.parse_args()
    sys.exit(main(options))

