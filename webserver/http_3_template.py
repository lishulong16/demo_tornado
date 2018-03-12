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
        self.render('template/index.html', he=delay)


application = web.Application([
    (r'/example', Example_Handler)
], autoreload=True, debug=True).listen(9990)

IOLoop.current().start()


# autoreload 在程序运行起来 每次编写代码并保存时，可以自定重新运行
# debug = true 会把程序运行出错信息 打印在屏幕上
# static_path 静态文件路径，如果与当前文件统一路径，可设为 os.path.dirname(__file__)
# 。。。。
