__author__ = 'Xsank'

#tcp server settings
SERVER_IP="127.0.0.1"
SERVER_PORT=8080

MAX_LISTEN_NUM=10
IS_BLOCKING=0
MAX_RECV=1024
EPOLL_TIMEOUT_SECONDS=1


#tcp handler worker settings
MAX_PROCESS_POOL_SIZE=8