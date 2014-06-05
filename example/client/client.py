__author__ = 'Xsank'

from example.api import HELLO
from example.api import GOODBYE
from hello import HelloHandler
from goodbye import GoodbyeHandler

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
