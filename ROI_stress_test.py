import argparse
import string
import subprocess
import sys
import time
import datetime

TID=0
TID_tex=""
ROI_Prefix = " 0xa8 0x07 0xe8 0x05 0x40 0x01 0x80 0x00  > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w\""
camera = [ 'a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5','c1', 'c2', 'c3', 'c4', 'c5', 'c6' ]

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

def slip_TID(x):
	# print x
	return x[2:] + " " + x[:2] + " "

def read_data(x):
	global TID
	time_out=0
	execute("adb shell \"echo 2 0xFFFF 0x7C 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w\"")
	execute("adb shell \"echo 4 0x027C > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br\"")
	data =  execute("adb shell \"cat /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br\"")
	test = slip_TID(x) + "01 00 "
	while (data.rstrip("\n") != test):
		execute("adb shell \"echo 2 0xFFFF 0x7C 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w\"")
		execute("adb shell \"echo 4 0x027C > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br\"")
		data =  execute("adb shell \"cat /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br\"")
		time_out = time_out +1
		if (time_out > 200):
			print data +"\t",
			return 0
	print data +"\t",
	return 1

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
def test_roi_cam(cam):
	print bcolors.HEADER,
	print ("\rROI calib for camera " + cam),
	print bcolors.ENDC + "\t",
	TID_tex = increase_TID()
	execute("adb shell \"echo 13 0x" + TID_tex +" 0x5a 0x80 " + module_bitmask(cam) + ROI_Prefix)
	if (read_data(TID_tex) == 1):
		print bcolors.OKBLUE,
		print bcolors.BOLD,
		print "Pass",
		print bcolors.ENDC
	else:
		print bcolors.FAIL,
		print bcolors.BOLD,
		print "Fail",
		print bcolors.ENDC

def reset_fw():
	print "Reset firmware ..."
	execute("adb shell \"cd /data/; ./prog_app_p2\"")
	time.sleep(10)
	print "Done"

############################################# Main script ################################################
i=1
reset_fw()
while (True):
	print bcolors.OKGREEN,
	print "\r--------------------- Start loop " + str(i) + " ---------------------",
	print bcolors.ENDC
	for c in camera:
		test_roi_cam (c)
	i=i+1
