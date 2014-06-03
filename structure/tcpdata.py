__author__ = 'Xsank'
import cPickle


class TcpData(object):
    def __init__(self,header,body):
        self.header=header
        self.body=body

    @staticmethod
    def serialize(obj):
        return cPickle.dumps(obj)

    @staticmethod
    def deserialize(s):
        return cPickle.loads(s)
