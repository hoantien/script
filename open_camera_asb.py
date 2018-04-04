#!/usr/bin/env python
import argparse
import string
import subprocess
import sys
import time
import datetime

def execute(cmd):
    #print(cmd);
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()[0]

def module_one_hot(x):
    return {
        'a1': 2,
        'a2': 4,
        'a3': 8,
        'a4': 16,
        'a5': 32,
        'b1': 64,
        'b2': 128,
        'b3': 256,
        'b4': 512,
        'b5': 1024,
        'c1': 2048,
        'c2': 4096,
        'c3': 8192,
        'c4': 16384,
        'c5': 32768,
        'c6': 65536,
        'g': 1,
        'a': 62,
        'b': 1984,
        'c': 129024
}[x]

def handle_endianness(in_string):
    # in_string should have an '0x' prepended
    # all cameras on (without global): 0x1FFFE
    in_string = in_string[2:]
    in_int = int(in_string, 16)
    print "in_int = " + hex(in_int)
    if (in_int <= 0xf): # one nibble
        output_string = '0x0' + in_string + ' 0x00 0x00'
    elif (in_int <= 255): # two nibbles
        output_string = '0x' + in_string[0] + in_string[1] + ' 0x00 0x00'
    elif (in_int <= 4095): # three nibbles
        output_string = '0x' + in_string[1] + in_string[2] + ' 0x0' + in_string[0] + ' 0x00'
    elif (in_int <= 65535): # four nibbles
        output_string = '0x' + in_string[2] + in_string[3] + ' 0x' + in_string[0] + in_string[1] + ' 0x00'
    else: # five nibbles
        output_string = '0x' + in_string[3] + in_string[4] + ' 0x' + in_string[1] + in_string[2] + ' 0x0' + in_string[0]
    print "output_string = "  + output_string
    return output_string

parser = argparse.ArgumentParser()
parser.add_argument("-on", "--open_camera", nargs='+',
                    help="select camera: from a1->a5, b1->b5 or c1->c6",
                    action="store")
parser.add_argument("-off", "--close_camera", nargs='+',
                    help="select camera: from a1->a5, b1->b5 or c1->c6",
                    action="store")
args = parser.parse_args()

if args.open_camera:
	fstring = ""
	byte_count = 5
	m_bitmask_int = 0
	for camera in args.open_camera:
		m_bitmask_int |= module_one_hot(camera)
	m_bitmask_str = hex(m_bitmask_int)
	print "m_bitmask_str = " + m_bitmask_str
	m_bitmask = handle_endianness(m_bitmask_str)
	print "m_bitmask = " + m_bitmask
	# check if we have non-35mm camera
	for camera in args.open_camera:
		m_bitmask_int |= module_one_hot(camera)
		# add the argument n number of times for n cameras
		fstring += "0x02 "
		byte_count += 1
#	print "open camera " + args.camera
	open_string = "adb shell \"echo " + str(byte_count) + " 0x0000 0x00 0x00 " + m_bitmask + " " + fstring + \
		"> /sys/class/i2c-adapter/i2c-11/i2c-0/0-0010/i2c_w\""
	print open_string
	execute(open_string)
	print ""

if args.close_camera:
    fstring = ""
    byte_count = 5
    m_bitmask_int = 0
    for camera in args.close_camera:
        m_bitmask_int |= module_one_hot(camera)
    m_bitmask_str = hex(m_bitmask_int)
    print "m_bitmask_str = " + m_bitmask_str
    m_bitmask = handle_endianness(m_bitmask_str)
    print "m_bitmask = " + m_bitmask
    # check if we have non-35mm camera
    for camera in args.close_camera:
        m_bitmask_int |= module_one_hot(camera)
        # add the argument n number of times for n cameras
        fstring += "0x00 "
        byte_count += 1
#   print "open camera " + args.camera
    open_string = "adb shell \"echo " + str(byte_count) + " 0x0000 0x00 0x00 " + m_bitmask + " " + fstring + \
        "> /sys/class/i2c-adapter/i2c-11/i2c-0/0-0010/i2c_w\""
    print open_string
    execute(open_string)
    print ""