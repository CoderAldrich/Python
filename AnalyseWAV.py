# -*- coding: cp936 -*-
# 解析WAV格式的文件-Leo
import os
import binascii

# 定义一个字典用来存储WAV文件的HEADER
WAV_HEADER = {
	"flag_RIFF":		0,
	"length_File":		0,
	"flag_WAVE":		0,
	"flag_FMT":			0,
	"sizeof_PCMWAVEFORMAT":		0,
	"PCMWAVEFORMAT":	0,
	"Channel":			0,
	"Frequency":		0,
	"Rate":				0,
	"length_DATA":		0,
	"wide_PCM":			0,
	"flag_DATA":		0,
	"sizeof_DATA":		0
}

file_path = raw_input("input WAV file path for analyse:")

with open(file_path, 'rb') as input_file:

    flag_RIFF = input_file.read(4)

    input_file.seek(4,1)

    flag_WAVE = input_file.read(4)

# 判断文件是否是wav文件
    if cmp(flag_RIFF, 'RIFF') or cmp(flag_WAVE, 'WAVE'):

        print "input file is not a WAV file!"

        exit(0)

    input_file.seek(0,0)
    
    WAV_HEADER["flag_RIFF"] = input_file.read(4).decode()

    print "flag_RIFF:", WAV_HEADER["flag_RIFF"]

    WAV_HEADER["length_File"] = input_file.read(4)

    print "length_File:", binascii.hexlify(WAV_HEADER["length_File"])

    WAV_HEADER["flag_WAVE"] = input_file.read(4).decode()

    print "flag_WAVE:", WAV_HEADER["flag_WAVE"]

    WAV_HEADER["flag_FMT"] = input_file.read(4).decode()

    print "flag_FMT:", WAV_HEADER["flag_FMT"]

    WAV_HEADER["sizeof_PCMWAVEFORMAT"] = input_file.read(4)

    print "sizeof_PCMWAVEFORMAT:", binascii.hexlify(WAV_HEADER["sizeof_PCMWAVEFORMAT"])

    WAV_HEADER["PCMWAVEFORMAT"] = input_file.read(2)

    print "PCMWAVEFORMAT:", binascii.hexlify(WAV_HEADER["PCMWAVEFORMAT"])

    WAV_HEADER["Channel"] = input_file.read(2)

    print "Channel:", binascii.hexlify(WAV_HEADER["Channel"])

    WAV_HEADER["Frequency"] = input_file.read(4)

    print "Frequency:", binascii.hexlify(WAV_HEADER["Frequency"])

    WAV_HEADER["Rate"] = input_file.read(4)

    print "Rate:", binascii.hexlify(WAV_HEADER["Rate"])

    WAV_HEADER["length_DATA"] = input_file.read(2)

    print "length_DATA:", binascii.hexlify(WAV_HEADER["length_DATA"])

    WAV_HEADER["wide_PCM"] = input_file.read(2)

    print "wide_PCM:", binascii.hexlify(WAV_HEADER["wide_PCM"])

    WAV_HEADER["flag_DATA"] = input_file.read(4)

    print "flag_DATA:", binascii.hexlify(WAV_HEADER["flag_DATA"])

    WAV_HEADER["sizeof_DATA"] = input_file.read(4)

    print "sizeof_DATA:", binascii.hexlify(WAV_HEADER["sizeof_DATA"])

    os.system('pause')
