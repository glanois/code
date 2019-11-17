import socket

class UdpReceiver:
    """ Receive from UDP socket.
        Test with socat - forwards stdin to addr:port
            socat - UDP-SENDTO:127.0.0.1:51001
    """
    def __init__(self):
        self._input = None
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def bind(self, address, port):
        self._sock.bind( (address, port) )

    def recvfrom(self, size):
        data, address = self._sock.recvfrom(size)
        return data, address


class UdpSender:
    """ Send to UDP endpoint.
        Test with socat - 
            socat - UDP-RECV:127.0.0.1:51001
    """
    def __init__(self):
        self._input = None
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def sendto(self, address, port, data):
        self._sock.sendto(bytes(data.encode('utf-8')), ( address, port ))


class TcpServer:
    """ TCP/IP server.
        Example usage:

        t = TcpServer()
        t.bind('localhost', 51001)
        while True:
            t.accept()
            while True:
                data = t.recv(1024)
                if data:
                    # Do something with the data.
                    # eg, for plain ASCII text strings 
                    #      data.decode('ascii').rstrip()

                    # Send something back
                    t.sendall('blah blah blah')
                else:
                    # No data received.
                    break
        t.close()
    """
    def __init__(self):
        self._input = None
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Avoid "OSError: [Errno 98] Address already in use" when restarting.
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._connection = None

    def bind(self, address, port):
        self._sock.bind( (address, port) )
        self._sock.listen(1)
        
    def accept(self):
        self._connection, client_address = self._sock.accept()

    def recv(self, size):
        data = self._connection.recv(size)
        return data

    def sendall(self, data):
        self._connection.sendall(data)

    def close(self):
         self._connection.close()


class TcpClient:
    """ TCP/IP client.
        Example usage:

    """
    def __init__(self):
        self._input = None
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, address, port):
        self._sock.connect( (address, port) )
        
    def recv(self, size):
        data = self._sock.recv(size)
        return data

    def sendall(self, data):
        self._sock.sendall(data)

    def close(self):
         self._sock.close()

