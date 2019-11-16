""" Example UDP listener.

    Test with:
       socat - UDP-SENDTO:127.0.0.1:51001
"""

import sys
import argparse

import lib.network

def main(options):
    u = lib.network.UdpListener()
    u.bind(options.address[0], int(options.port[0]))
    data, address = u.get(1024)
    print(data.decode('ascii').rstrip())
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'address',
        help='Address of the UDP endpoint to listen to.',
        nargs=1)

    parser.add_argument(
        'port',
        help='Port of the UDP endpoint to listen to.',
        nargs=1)

    options = parser.parse_args()
    sys.exit(main(options))

