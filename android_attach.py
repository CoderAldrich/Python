# -*- coding: cp936 -*-
# 执行logcat以及远程的android_server，并打开监听端口供IDA attach到进程进行调试

import os
import time

os.startfile("android_server.py")

time.sleep(2)

os.startfile("android_listen.py")

time.sleep(2)

os.startfile("android_logcat.py")
