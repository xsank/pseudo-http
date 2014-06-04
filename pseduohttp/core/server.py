__author__ = 'Xsank'
import socket
import select
import threading

from pseduohttp.structure.tcpdata import TcpData
from pseduohttp.structure.tcpcontroller import TcpController
from pseduohttp.constant.settings import MAX_LISTEN_NUM
from pseduohttp.constant.settings import IS_BLOCKING
from pseduohttp.constant.settings import MAX_RECV
from pseduohttp.constant.settings import EPOLL_TIMEOUT_SECONDS


class TcpServer(threading.Thread):
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port
        self._init_socket()
        self._init_epoll()

    def _init_socket(self):
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind((self.ip,self.port))
        self.socket.listen(MAX_LISTEN_NUM)
        self.socket.setblocking(IS_BLOCKING)
        self.socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)

    def _init_epoll(self):
        self.epoll=select.epoll()
        self.epoll.register(self.socket.fileno(),select.EPOLLIN)

    def init_controller(self,handlers):
        self.controller=TcpController(handlers)

    def run(self):
        try:
            requests={}
            responses={}
            connections={}
            while True:
                events=self.epoll.poll(EPOLL_TIMEOUT_SECONDS)
                for fileno,event in events:
                    if fileno == self.socket.fileno():
                        connection,address=self.socket.accept()
                        connection.setblocking(IS_BLOCKING)
                        self.epoll.register(connection,fileno(),select.EPOLLIN)
                        connections[connection.fileno()]=connection
                    elif event & select.EPOLLIN:
                        data=connections[fileno].recv(MAX_RECV)
                        tcpdata=TcpData.deserialize(data)
                        requests[fileno]=tcpdata
                        self.controller.process(tcpdata.header,tcpdata.body)
                        self.epoll.modify(fileno,select.EPOLLOUT)
                    elif event & select.EPOLLOUT:
                        print 'request %s process ok' % requests[fileno].header
                        responses[fileno]=requests[fileno].header
                        connections[fileno].send(responses[fileno])
                        self.epoll.modify(fileno,0)
                        connections[fileno].shutdown(socket.SHUT_RDWR)
                    elif event & select.EPOLLHUP:
                        self.epoll.unregister(fileno)
                        connections[fileno].close()
                        del connections[fileno]
        finally:
            self.destroy()

    def destroy(self):
        self.epoll.unregister(self.socket.fileno())
        self.epoll.close()
        self.socket.close()
