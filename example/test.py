__author__ = 'Xsank'


class A(object):
    @staticmethod
    def f():
        pass


class B(A):
    def f():
        print 'hello'