# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/12 下午5:27
"""

from __future__ import print_function
import platform

# 机器基本信息
print(platform.uname())
print(platform.uname().system)
print(platform.uname().node)
print(platform.uname().release)
print(platform.uname().version)
print(platform.uname().machine)
print(platform.uname().processor)

# cpu 核数
import multiprocessing

print(multiprocessing.cpu_count())

# cpu 信息
with open('/proc/cpuinfo') as f:
    for line in f:
        # Ignore the blank line separating the information between
        # details about two processing units
        if line.strip():
            if line.rstrip('\n').startswith('model name'):
                model_name = line.rstrip('\n').split(':')[1]
                print(model_name)
