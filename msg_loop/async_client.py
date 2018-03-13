# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/13 下午3:42
"""

import socket
from time import time

from tornado import ioloop

loop = ioloop.IOLoop.current()

sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(50)]

[socket.connect(('localhost', 1111)) for socket in sockets]

sockets_A = {socket.fileno(): socket for socket in sockets}

t0 = time()
n = 0


def onEnv(fd, evnet):
    if evnet == loop.WRITE:
        loop.update_handler(fd, loop.READ)
    elif evnet == loop.READ:
        socket = sockets_A[fd]
        socket.recv(99)
        global n
        n += 1
        if n >= 1000:
            print('time cost:{}'.format(time() - t0))
            socket.close()
            loop.remove_handler(fd)
            loop.stop()
            return
        loop.update_handler(fd, loop.WRITE)
        socket.send('test msg {}'.format(n).encode('utf-8'))


for fd, sock in sockets_A.items():
    loop.add_handler(fd, onEnv, loop.WRITE)
    sock.send('test msg ----1'.encode('utf-8'))
loop.start()
