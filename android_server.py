# 本程序执行android手机的android_server以便IDA附加到进程进行调试
import os

os.system("adb shell /data/local/tmp/android_server")
