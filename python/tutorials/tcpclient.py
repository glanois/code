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
        format='%(asctime)s %(name)s %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger('main()')

    t = lib.network.TcpClient()
    t.connect(options.address[0], int(options.port[0]))
    logger.info('connected to %s:%d' % (options.address[0], int(options.port[0])))

    while True:
        t.sendall('ping'.encode('utf-8'))
        logger.info('sent: ping')

        response = t.recv(16)
        if len(response) == 0:
            # Connection closed.
            logger.info('recv() returned 0 bytes')
            break
        else:
            response = response.decode('ascii').rstrip()
            if response == 'pong':
                logger.info('got:  pong')

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

