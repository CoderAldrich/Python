# -*- coding: cp936 -*-
# ִ��logcat�Լ�Զ�̵�android_server�����򿪼����˿ڹ�IDA attach�����̽��е���

import os
import time

os.startfile("android_server.py")

time.sleep(2)

os.startfile("android_listen.py")

time.sleep(2)

os.startfile("android_logcat.py")
