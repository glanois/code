""" Example UDP sender.

    Test with:
       socat - UDP-RECV:127.0.0.1:51002
"""

import sys
import argparse

import lib.network

def main(args):
    u = lib.network.UdpSender()
    u.sendto(args.address[0], int(args.port[0]), args.message[0])
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'address',
        help='Address of the UDP endpoint to send to.',
        nargs=1)

    parser.add_argument(
        'port',
        help='Port of the UDP endpoint to send to.',
        nargs=1)

    parser.add_argument(
        'message',
        help='Message to send (use double quotes to contain whitespace).',
        nargs=1)

    args = parser.parse_args()
    sys.exit(main(args))

