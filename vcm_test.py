#!/usr/bin/python
import subprocess
import os
import argparse
import sys

### Define function ####################################
def execute(shell_string):
    subprocess.call(shell_string, shell=True)

def file_len(fname):
    with open(fname) as f:
        for k, l in enumerate(f):
            pass
    return k + 1

def read_line(fname,fline):
	j=0
	l_t=""
	while j < int(fline):
		l_t = fname.readline()
		j = i+1
	return l_t 

def split_bytes(arg):
    # assume the user always inputs 4 digits (i.e the leading nibbles
    # in each byte are nonzero, so we get 4 digits)
    int_input = len(arg)
    # print int_input
    if (arg[:2] == '0x'):
        if (int_input < 6):
        	fstring = '0x' + arg[-2:] + ' 0x0' + arg[2:3]
        else:
    	    fstring = '0x' + arg[-2:] + ' ' +  arg[0:4]
        return fstring
    else:
       print "Not support this value"

def handle_endianness(in_string):
    # in_string should have an '0x' prepended

    # all cameras on (without global): 0x1FFFE
    in_string = in_string[2:]
    in_int = int(in_string, 16)
    #print "in_int = " + hex(in_int)
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
    #print "output_string = "  + output_string
    return output_string

def module_one_hot(x):
    return {
    	'g':1,
        'a1': 2,
        'a2': 4,
        'a3': 8,
        'a4': 16,
        'a5': 32,
    	'a': 62,
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
        'c6': 65536
}[x]

def read_vcm(x):
	i = 1
	time = 20
	while i<=int(time):
		execute('python vcm_test.py -c '+x+' -r_v')
		execute('python vcm_test.py -result ' + str(i))		
		i+=1

### Parser #############################################
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--camera", nargs='+',
                    help="select camera: from g, a1->a5, b1->b5 or c1->c6",
                    action="store")
parser.add_argument("-vcm", "--vcm", help="vcm value",
                    action="store")
parser.add_argument("-r_v", "--read_vcm", help="read vcm value",
                    action="store_true")
parser.add_argument("-test", "--test", help="test vcm",
                    action="store_true")
parser.add_argument("-result", "--result", help="result vcm",
                    action="store")
args = parser.parse_args()
########################################################

if args.camera:
    # OR the one-hot encoded cameras together into one bitmask
    # print "Camera(s) are " + str(args.camera)
    m_bitmask_int = 0
    for camera in args.camera:
        m_bitmask_int |= module_one_hot(camera)
    m_bitmask_str = hex(m_bitmask_int)
    #print "m_bitmask_str = " + m_bitmask_str
    m_bitmask = handle_endianness(m_bitmask_str)
    # print "m_bitmask = " + m_bitmask
    camera_string = ""
    stream_string = ""

if args.vcm:
    if args.camera:
        fstring = ""
        byte_count = 7
        for camera in args.camera:
	        if camera == 'a':
	        	i=1
	        	while i<=5:
		        	fstring += split_bytes(args.vcm)
		        	fstring += " "
		        	byte_count += 2
		        	i=i+1
	        else:
		        fstring += split_bytes(args.vcm)
		        byte_count += 2
        # print "vcm is " + args.vcm
        vcm_string = "adb shell \"echo " + str(byte_count) + " 0x0000 0x3C 0x80 " + m_bitmask + " 0x03 0x00 "\
        + fstring + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        # print vcm_string
        execute(vcm_string)
        # print ""
    else:
        print "Please provide a camera argument."
if args.read_vcm:
	if camera:
		# print camera
		camera_count = 0
		for camera in args.camera:
			camera_count +=2
		if camera == 'a':
			camera_count = 10
		if camera == 'g':
			camera_count = 32
		vcm_string = "adb shell \"echo 5 0x0000 0x40 0x80 " + m_bitmask +\
		 " > /sys/class/light_ccb/i2c_interface/i2c_w\""
		# print vcm_string
        execute(vcm_string)
        # print ('adb shell "echo 0x18,0x0040 > /sys/class/light_ccb/i2c_interface/i2c_addr"')
        execute('adb shell "echo 0x18,0x0040 > /sys/class/light_ccb/i2c_interface/i2c_addr"')
        # print ('adb shell "echo ' + str(camera_count) + ' > /sys/class/light_ccb/i2c_interface/i2c_br"')
        execute('adb shell "echo ' + str(camera_count) +' > /sys/class/light_ccb/i2c_interface/i2c_br"')
        # print ('adb shell "cat /sys/class/light_ccb/i2c_interface/i2c_br" 1>adb_output.txt')
        execute('adb shell "cat /sys/class/light_ccb/i2c_interface/i2c_br" 1>adb_output.txt')
        # print ""
if args.result:
	print("\rResult "+args.result+":")
	f = open('adb_output.txt', 'r')
	line = f.readline()
	if line != ' ':
		a1_vcm = line[3:5] + line[0:2]
		print " a1_vcm = " +a1_vcm ,
		a2_vcm = line[9:11] + line[6:8]
		print " a2_vcm = " +a2_vcm ,
		a3_vcm = line[15:17] + line[12:14]
		print " a3_vcm = " +a3_vcm ,
		a4_vcm = line[21:23] + line[18:20]
		print " a4_vcm = " +a4_vcm ,
		a5_vcm = line[27:29] + line[24:26]
		print " a5_vcm = " +a5_vcm ,
	else:
		print("   No test result")

if args.test:
	print "\n********* Start script *************"
	print "- Move to macro - hall code = 0x8001 -"
	execute('python vcm_test.py -c a -vcm 0x8001')
	read_vcm('a')

	print "\n- Move to infinity - hall code = 0x7fff -"
	execute('python vcm_test.py -c a -vcm 0x7fff')
	read_vcm('a')
	print "\n--- Move to hall code = 0x838 -----"
	execute('python vcm_test.py -c a -vcm 0x838')
	read_vcm('a')

	print "\n--- Move to hall code = 0x2500 -----"
	execute('python vcm_test.py -c a -vcm 0x2500')
	read_vcm('a')
