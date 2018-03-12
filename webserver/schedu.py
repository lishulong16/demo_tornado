# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/12 下午6:45
"""

from tornado import ioloop, gen
from time import time


def Count():
    print('1 second has gone')


if __name__ == '__main__':
    # ioloop.PeriodicCallback(Count, 1000).start()

    # ioloop.IOLoop.current().start()

    lop = ioloop.IOLoop.current()
    lop.call_at(time() + 5, Count)

    lop.start()

