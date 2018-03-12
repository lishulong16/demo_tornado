# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/12 下午3:58
"""

import tornado.ioloop
import tornado.web


class MainHandle(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")
        pass

    pass


def make_app():
    return tornado.web.Application([
        ('/', MainHandle)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()