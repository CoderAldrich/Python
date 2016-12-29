#!/usr/bin/python
# coding: utf-8

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
                if line.upper().find(key.upper())!=-1:
                    filenum = filenum + 1            
                    print filepath
    except Exception , e:
        if e == 5:
            return filenum
    return filenum
##############################################################

keystr = raw_input('input the key words of file name: ')

#currentdir = os.getcwd()

systemdri = os.getenv("systemdrive")

flag = ord(systemdri[0])

currentdir = '%c%s' % (chr(flag), ':\\')

print 'key string is:',keystr
print 'start to search...'

while flag <= 132:
    if not os.path.exists(currentdir):
        break
    searchfile(currentdir, keystr)
    flag = flag + 1
    currentdir = '%c%s' % (chr(flag), ':\\')

os.system('pause')
