""" Example TCP client.
"""

import logging
import sys
import argparse
import time
import threading

import lib.network

def ping(event, tcp_client):
    tcp_client.sendall('ping'.encode('utf-8'))
    event.set()

        
def main(options):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    t = lib.network.TcpClient()
    t.connect(options.address[0], int(options.port[0]))

    while True:
        e = threading.Event()
        timer = threading.Timer(1.0, ping, (e, t))
        timer.start()
        e.wait()

        response = ''
        while response != 'pong':
            fragment = t.recv(16)
            if len(fragment) > 0:
                fragment = fragment.decode('ascii').rstrip()
                response += fragment
          
            if len(response) > 0:
                logging.info(response)

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

