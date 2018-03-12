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

        times = yield self.delayTwice(int(delay))

        self.write({'status': 1, 'msg': 'success', 'times': times})

        self.finish()

    @gen.coroutine
    def delayTwice(self, seconds):
        yield gen.sleep(seconds)
        yield gen.sleep(seconds)
        raise gen.Return(2)


application = web.Application([
    (r'/example', Example_Handler)
], autoreload=True).listen(9990)

IOLoop.current().start()
