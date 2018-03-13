# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/13 下午2:35
"""
import traceback
import logging

from tornado import ioloop, gen, iostream
from tornado.tcpserver import TCPServer


class My_Server(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        try:
            while True:
                msg = yield stream.read_bytes(200, partial=True)
                print('msg:{}, from address:{}'.format(msg, address))
                yield stream.write(msg[::-1])
                yield gen.sleep(0.005)
                if msg.decode('utf-8') == 'over':
                    stream.close()
                    pass
        except iostream.StreamClosedError as e:
            # logging.error('error', e, traceback.format_exc())
            pass


if __name__ == '__main__':
    server = My_Server()
    server.listen(1111)
    server.start()
    ioloop.IOLoop.current().start()
