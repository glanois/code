""" Example TCP server.

    Test with:
       telnet 127.0.0.1 51001
"""

import sys
import argparse

import lib.network

def main(options):
    t = lib.network.TcpServer()
    t.bind(options.address[0], int(options.port[0]))

    shutdown = False
    while not shutdown:
        t.accept()
        while True:
            data = t.recv(1024)
            if data:
                s = data.decode('ascii').rstrip()
                if s == 'shutdown':
                    t.close()
                    shutdown = True
                    break
                elif s == 'ping':
                    response = 'pong'
                    t.sendall(bytes(response.encode('utf-8')))
                else:
                    print(s)
            else:
                # No data received.
                break
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'address',
        help='Address of the network interface to host the socket.',
        nargs=1)

    parser.add_argument(
        'port',
        help='Port number of the socket.',
        nargs=1)

    options = parser.parse_args()
    sys.exit(main(options))

