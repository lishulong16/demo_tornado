# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/3/13 下午3:14
"""

import traceback
import logging


try:
    if 1==1:
        i = 1/0
except Exception as e:
    print(traceback.format_exc())
