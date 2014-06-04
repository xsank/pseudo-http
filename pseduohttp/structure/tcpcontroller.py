__author__ = 'Xsank'

from multiprocessing.pool import Pool

from pseduohttp.constant.settings import MAX_PROCESS_POOL_SIZE


class TcpController(object):
    def __init__(self,handlers):
        self.handlers=handlers
        self.workers=Pool(MAX_PROCESS_POOL_SIZE)

    def process(self,header,body):
        self.workers.apply_async(self.handlers[header].process,(body,))

    def destroy(self):
        self.handlers=None
        self.workers.close()