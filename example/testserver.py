__author__ = 'Xsank'

from api import HELLO
from api import GOODBYE
from shello import HelloHandler
from sgoodbye import GoodbyeHandler

from pseduohttp.core.server import TcpServer


SERVER_HANDLERS={
    HELLO:HelloHandler,
    GOODBYE:GoodbyeHandler
}

if __name__=="__main__":
    tcpserver=TcpServer()
    tcpserver.init_controller(SERVER_HANDLERS)
    tcpserver.start()
