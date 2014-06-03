__author__ = 'Xsank'
import socket
import threading

from structure.tcpdata import TcpData
from constant.settings import IS_BLOCKING


class TcpClient(threading.Thread):
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        self.connected=False
        self._init_socket()

    def _init_socket(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((self.ip,self.port))
        self.socket.setblocking(IS_BLOCKING)
        self.connected=True

    def send_if_connected(self,header,body):
        if self.connected:
            data=TcpData(header,body)
            try:
                self.socket.send(TcpData.serialize(data))
            except Exception:
                self.connected=False
                self.socket.close()

    def reconnect(self):
        if not self.connected:
            self._init_socket()

    def destroy(self):
        self.socket.close()
