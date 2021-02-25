""" Example socketserver.TCPServer

    Test with:
       telnet 127.0.0.1 51001
"""

import logging
import sys
import argparse
import socketserver
import time

class Handler(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('Handler')
        self.logger.debug('__init__()')
        super().__init__(request, client_address, server)
        
    def handle(self):
        logger = logging.getLogger('Handler::handle()')
        self.data = self.request.recv(16)
        if self.data:
            self.data = self.data.decode('ascii').rstrip()
            logger.debug('Got string %s' % (self.data))
            if self.data == 'ping':
                response = 'pong'
                self.request.sendall(bytes(response.encode('utf-8')))
                logger.debug('Sent reponse %s' % (response))
        

class PingPongServer(socketserver.TCPServer):
    def __init__(self, server_address, handler_class):
        super().__init__(server_address, handler_class)
        self.allow_reuse_address = True
        logger = logging.getLogger('PingPongServer')
        logger.debug('__init__()')


def main(options):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)s %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger('main()')
    logger.info('Starting up PingPongSever at %s:%d' % (options.address[0], int(options.port[0])))
    
    server_address = (options.address[0], int(options.port[0]))
    with PingPongServer(server_address, Handler) as server:
        server.serve_forever()
        logger.info('Returned from PingPongServer.serve_forever()')

    time.sleep(5)
        
if __name__ == '__main__':
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

