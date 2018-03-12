# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/12 下午4:47
"""

from tornado.ioloop import IOLoop
from tornado import gen, web


class Example_Handler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        delay = self.get_argument('delay', 5)

        yield gen.sleep(int(delay))

        self.write({'status': 1, 'msg': 'success'})

        self.finish()


application = web.Application([
    (r'/example', Example_Handler)
], autoreload=True).listen(9990)


IOLoop.current().start()
