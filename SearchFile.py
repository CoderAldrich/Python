#!/usr/bin/python
# coding: utf-8
# 本模块利用递归调用的方法打印出给定的目录及子目录下，文件名中包含指定关键字的文件路径

import os

def searchfile(directory, key):
    filenum = 0
    try:
        list = os.listdir(directory)
        lenoflist = len(list)
        #print lenoflist
        if lenoflist == 0:
            return filenum
        for line in list:
            filepath = os.path.join(directory, line)
            #print filepath
            if os.path.isdir(filepath):
                searchfile(filepath, key)
                continue
            else:
                if line.find(key)!=-1:
                    filenum = filenum + 1            
                    print filepath
    except Exception , e:
        if e == 5:
            return filenum
    return filenum
##############################################################

keystr = raw_input('input the key words of file name: ')

currentdir = os.getcwd()

print 'current directory is',currentdir,',key string is',keystr

searchfile(currentdir, keystr)

os.system('pause')
