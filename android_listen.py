# 监听23946端口
import os

os.system("adb forward tcp:23946 tcp:23946")
