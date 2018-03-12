# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/12 下午4:47
"""

from tornado.ioloop import IOLoop
from tornado import gen, web
import multiprocessing
from tornado.httpserver import HTTPServer


class Example_Handler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        delay = self.get_argument('delay', 5)

        yield gen.sleep(int(delay))

        self.write({'status': 1, 'msg': 'success'})

        self.finish()


if __name__ == '__main__':
    application = web.Application([
        (r'/example', Example_Handler)
    ], autoreload=False, debug=False)
    server = HTTPServer(application)
    server.bind(8888)
    # 开启多进程的时候要关闭自动load' 和debug 模式
    server.start(multiprocessing.cpu_count())
    IOLoop.current().start()


"""
➜  demo_tornado git:(master) ✗ lsof -i:8888 
COMMAND     PID      USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
python3.6 96114 lishulong    5u  IPv4 0x898bd8a93847ff85      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96114 lishulong    6u  IPv6 0x898bd8a921fbe5fd      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96115 lishulong    5u  IPv4 0x898bd8a93847ff85      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96115 lishulong    6u  IPv6 0x898bd8a921fbe5fd      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96116 lishulong    5u  IPv4 0x898bd8a93847ff85      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96116 lishulong    6u  IPv6 0x898bd8a921fbe5fd      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96117 lishulong    5u  IPv4 0x898bd8a93847ff85      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96117 lishulong    6u  IPv6 0x898bd8a921fbe5fd      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96118 lishulong    5u  IPv4 0x898bd8a93847ff85      0t0  TCP *:ddi-tcp-1 (LISTEN)
python3.6 96118 lishulong    6u  IPv6 0x898bd8a921fbe5fd      0t0  TCP *:ddi-tcp-1 (LISTEN)
➜  demo_tornado git:(master) ✗ 


"""