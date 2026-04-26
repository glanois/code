""" Example UDP receiver.

    Test with:
       socat - UDP-SENDTO:127.0.0.1:51001
"""

import sys
import argparse

import lib.network

def main(args):
    u = lib.network.UdpReceiver()
    u.bind(args.address[0], int(args.port[0]))
    data, address = u.recvfrom(1024)
    print(data.decode('ascii').rstrip())
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'address',
        help='Address of the UDP endpoint to receive from.',
        nargs=1)

    parser.add_argument(
        'port',
        help='Port of the UDP endpoint to receive from.',
        nargs=1)

    args = parser.parse_args()
    sys.exit(main(args))

