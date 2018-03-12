# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/12 下午5:59
"""

from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado.httpclient import AsyncHTTPClient

url = 'http://www.baidu.com'


class GetPageHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        client = AsyncHTTPClient()
        response = yield client.fetch(url, method='GET')
        self.write(response.body.decode('utf-8'))
        self.finish()


if __name__ == '__main__':
    application = web.Application([
        (r"/getpage", GetPageHandler),
    ], autoreload=True)
    application.listen(8765)
    IOLoop.current().start()
