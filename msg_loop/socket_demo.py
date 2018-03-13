# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/13 下午3:35
"""

import socket
from time import time

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost', 1111))

t0 = time()

for _ in range(1000):
    socket.send('test msg'.encode('utf-8'))
    socket.recv(99)

print('time cost:{}'.format(time() - t0))

socket.close()
