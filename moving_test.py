import argparse
import string
import subprocess
import sys
import time
import datetime

read_len = "adb shell \"echo 2 0x0040 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br\""
read_mirror = "adb shell \"echo 2 0x0044 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br\""
cat = "adb shell \"cat /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br\""

camera = [ 'a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5','c1', 'c2', 'c3', 'c4', 'c5', 'c6' ]
camera_bc= [ 'b1', 'b2', 'b3', 'b4', 'b5','c1', 'c2', 'c3', 'c4', 'c5', 'c6' ]
move=['0','A00', '700','ffff']
move_mirror=['0','150', '170','ffff']
test = ['c6']
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def execute(cmd):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	return proc.communicate()[0]

def increase_TID():
	global TID
	TID = TID+1
	if (TID<0x10):
		return "000"+str(hex(TID))[2:]
	elif ((TID>0xF) & (TID < 0x100)):
		return "00"+str(hex(TID))[2:]
	elif ((TID>0xFF) & (TID < 0x1000)):
		return "0"+str(hex(TID))[2:]
	else:
		return str(hex(TID))[2:]

def module_bitmask(x):
	return {
		'g' : "0x01 0x00 0x00",
		'a1': "0x02 0x00 0x00",
		'a2': "0x04 0x00 0x00",
		'a3': "0x08 0x00 0x00",
		'a4': "0x10 0x00 0x00",
		'a5': "0x20 0x00 0x00",
		'b1': "0x40 0x00 0x00",
		'b2': "0x80 0x00 0x00",
		'b3': "0x00 0x01 0x00",
		'b4': "0x00 0x02 0x00",
		'b5': "0x00 0x04 0x00",
		'c1': "0x00 0x08 0x00",
		'c2': "0x00 0x10 0x00",
		'c3': "0x00 0x20 0x00",
		'c4': "0x00 0x40 0x00",
		'c5': "0x00 0x80 0x00",
		'c6': "0x00 0x00 0x01",
		'a' : "0x3E 0x00 0x00",
		'b' : "0xC0 0x07 0x00",
		'c' : "0x00 0xF8 0x01",
		'ab': "0xFE 0x07 0x00",
		'bc': "0xC0 0xFF 0x00"
	}[x]

def reset_fw():
	print "Reset firmware ..."
	execute("adb shell \"cd /data/; ./prog_app_p2\"")
	time.sleep(20)
	print "Done"

def change_to_hex(x):
	test = x[3:-1]+x[:3]
	return test

def read_hall_lens(cam,read):
	execute("python camera_script_asb.py -c "+cam+" -rhsv -l")
	execute(read)
	data = execute(cat)
	print "Camera " +cam + "\t",
	print change_to_hex(data)


def read_hall_mirror(cam,read):
	execute("python camera_script_asb.py -c "+cam+" -rhsv -m")
	execute(read)
	data = execute(cat)
	print "Camera " +cam + "\t",
	print change_to_hex(data)

############################################# Main script ################################################
# reset_fw()
# for i in camera:
# 	read_hall(i,read_len)
# reset_fw()
# for i in camera:
# 	read_hall(i,read_len)
# reset_fw()
# execute("python camera_script_asb.py -c g -o sw")
# time.sleep(5)
# for i in camera:
# 	read_hall(i,read_len)

for i in camera_bc:
	for j in move:
			execute("python camera_script_asb.py -c "+i+" -ghsv "+j+" -l")
			time.sleep(2)
			read_hall_lens(i,read_len)
print "----------"
for i in camera_bc:
	for j in move_mirror:
			execute("python camera_script_asb.py -c "+i+" -ghsv "+j+" -m")
			time.sleep(2)
			read_hall_mirror(i,read_mirror)

