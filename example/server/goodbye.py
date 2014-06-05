__author__ = 'Xsank'


from pseduohttp.structure.tcphandler import TcpHandler


class GoodbyeHandler(TcpHandler):
    def process(self,body):
        print 'goodbye from client:%s' % body