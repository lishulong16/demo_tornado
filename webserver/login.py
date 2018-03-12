# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/12 下午6:28
"""

from tornado.ioloop import IOLoop
from tornado import gen, web


class LoginHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_secure_cookie('uname', 'Tom')
        self.write('login ok')
        self.finish()


class LogoutHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.clear_cookie('uname')
        self.write('log out')
        self.finish()


class WhoHandler(web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('uname') or 'unknown'

    @gen.coroutine
    def get(self):
        self.write('you are ' + str(self.get_current_user()))
        self.finish()


if __name__ == '__main__':
    app = web.Application([
        (r'/login', LoginHandler),
        (r'/logout', LogoutHandler),
        (r'/whoami', WhoHandler)
    ], autoreload=True,cookie_secret='acd')

    app.listen(2222)
    IOLoop.current().start()
