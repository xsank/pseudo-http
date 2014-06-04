__author__ = 'Xsank'
import socket
import thread
import time
import threading

from pseduohttp.structure.tcpdata import TcpData
from pseduohttp.constant.settings import IS_BLOCKING


class TcpClient(object):
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

    def init_controller(self,handlers):
        self.handlers=handlers

    def send_if_connected(self,header,body):
        if self.connected:
            data=TcpData(header,body)
            try:
                self.socket.send(TcpData.serialize(data))
            except Exception:
                self.connected=False
                self.socket.close()

    def loop(self):
        if self.connected:
            thread.start_new_thread(self.process_response,())

    def process_response(self):
        while True:
            try:
                data=TcpData.deserialize(self.socket.recv(1024))
                self.handlers[data.header].process(data.body)
                print 'tcpclient:%s handler recieve data %s' % data.header,data.body
            except Exception:
                time.sleep(1)

    def reconnect(self):
        if not self.connected:
            self._init_socket()

    def destroy(self):
        self.socket.close()
