__author__ = 'Xsank'

from api import HELLO
from api import GOODBYE
from chello import HelloHandler
from cgoodbye import GoodbyeHandler

from pseduohttp.core.client import TcpClient

CLIENT_HANDLERS={
    HELLO:HelloHandler,
    GOODBYE:GoodbyeHandler
}


if __name__=="__main__":
    tcpclient=TcpClient()
    tcpclient.init_handlers(CLIENT_HANDLERS)
    tcpclient.loop()
    tcpclient.send_if_connected(HELLO,'testclient')
