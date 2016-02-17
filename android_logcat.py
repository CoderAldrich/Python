import os

tag = raw_input("input the tag of log:")

command = "adb logcat -s " + tag + ":v"

#print os.popen(command).read()
os.system(command)
