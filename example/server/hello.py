__author__ = 'Xsank'

from pseduohttp.structure.tcphandler import TcpHandler


class HelloHandler(TcpHandler):
    def process(self,body):
        print 'hello from client:%s' % body