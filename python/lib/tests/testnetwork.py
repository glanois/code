""" testnetwork.py - Unit test for network. """

import unittest
import lib.network

class TestNetworkFunctions(unittest.TestCase):
    def test_udp_sender(self):
        s = lib.network.UdpSender()
        s.close()

    def test_udp_receiver(self):
        r = lib.network.UdpReceiver()
        r.close()

    def test_tcp_server(self):
        s = lib.network.TcpServer()
        s.close()

    def test_tcp_client(self):
        c = lib.network.TcpClient()
        c.close()
