# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/12 下午6:53
"""

from tornado.testing import gen_test, AsyncTestCase
from tornado.httpclient import AsyncHTTPClient

import unittest


class MyAsyncTest(AsyncTestCase):
    @gen_test
    def test_01(self):
        client = AsyncHTTPClient(self.io_loop)

        path = 'https://gist.github.com/lishulong16'

        res = yield [client.fetch(path, method='GET') for _ in range(10)]

        for r in res:
            print(r.body)


if __name__ == '__main__':
    unittest.main()
