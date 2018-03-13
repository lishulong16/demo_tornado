# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/13 下午2:45
"""

from tornado import ioloop, gen, iostream

from tornado.tcpclient import TCPClient
import logging
import traceback

@gen.coroutine
def Trace_info():
    stream = yield TCPClient().connect('localhost', 1111)
    try:
        for msg in ('zxx', 'abc', 'jack', 'i am the king of the world', 'over'):
            yield stream.write(msg.encode(encoding='utf-8'))
            back = yield stream.read_bytes(20, partial=True)
            print(back.decode('utf-8'))
    except Exception as e:
        logging.error('error', traceback.format_exc(e))


if __name__ == '__main__':
    ioloop.IOLoop.current().run_sync(Trace_info)
