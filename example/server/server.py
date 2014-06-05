__author__ = 'Xsank'

from example.api import HELLO
from example.api import GOODBYE
from hello import HelloHandler
from goodbye import GoodbyeHandler

from pseduohttp.core.server import TcpServer


SERVER_HANDLERS={
    HELLO:HelloHandler,
    GOODBYE:GoodbyeHandler
}

if __name__=="__main__":
    tcpserver=TcpServer()
    tcpserver.init_controller(SERVER_HANDLERS)
    tcpserver.start()
