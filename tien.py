import argparse
import string
import subprocess
import sys
import time
import datetime

camera_bc= [ 'b2', 'b4', 'b5','c5' ]
camera_a = [ 'a1', 'a5']
camera = [ 'b2','b5' ]
lcc_write = "adb shell \"cd \data; ./lcc -m 0 -s 0 -w -p "
lcc_read = "adb shell \"cd \data; ./lcc -m 0 -s 0 -r -p "

TID=6

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
		'g': "01 00 00",
		'a1': "02 00 00",
		'a2': "04 00 00",
		'a3': "08 00 00",
		'a4': "10 00 00",
		'a5': "20 00 00",
		'b1': "40 00 00",
		'b2': "80 00 00",
		'b3': "00 01 00",
		'b4': "00 02 00",
		'b5': "00 04 00",
		'c1': "00 08 00",
		'c2': "00 10 00",
		'c3': "00 20 00",
		'c4': "00 40 00",
		'c5': "00 80 00",
		'c6': "00 00 01"
	}[x]

def increase_TID():
	global TID
	TID = TID+1
	if (TID<0x10):
		return "00 0"+str(hex(TID))[2:] + " "
	elif ((TID>0xF) & (TID < 0x100)):
		return "00 "+str(hex(TID))[2:]+ " "
	elif ((TID>0xFF) & (TID < 0x1000)):
		return "0"+str(hex(TID))[2:-2]+ " " + str(hex(TID))[3:]+ " "
	else:
		return str(hex(TID))[2:-2]+ " "+str(hex(TID))[4:]+" "

def reset_fw():
	print "Reset firmware ..."
	execute("adb shell \"cd /data/; ./prog_app_p2\"")
	time.sleep(20)
	print "Done"

def string(x):
	if (x<0x10):
		return " 0"+str(hex(x))[2:] + " 00"
	elif ((x>0xF) & (x < 0x100)):
		return " "+str(hex(x))[2:]+ " 00"
	elif ((x>0xFF) & (x < 0x1000)):
		return " " + str(hex(x))[3:]+ " 0"+str(hex(x))[2:-2]
	else:
		return " "+str(hex(x))[4:]+ " "+str(hex(x))[2:-2]

def string_bigendian(x):
	if (x<0x10):
		return "00"+"0"+str(hex(x))[2:] 
	elif ((x>0xF) & (x < 0x100)):
		return "00" + str(hex(x))[2:]
	elif ((x>0xFF) & (x < 0x1000)):
		return "0"+str(hex(x))[2:-2]+str(hex(x))[3:]
	else:
		return str(hex(x))[2:-2]+str(hex(x))[4:]

def read_hall_lens(cam,pos):
	global TID
	# data="0123"
	time = execute(lcc_write + increase_TID() + "40 80 "+ module_bitmask(cam) + string(pos) +"\"")
	# data = execute(lcc_read + increase_TID()+ "40 00 "+ module_bitmask(cam)+"\"")
	# data = data.replace("\r", " ")
	# data = data.replace("\n", " ")
	# data = data[36:-3]
	# data = data[3:] + data[:2]
	# print "  "+cam +"\t   " +string_bigendian(pos) +"\t\t  " + data
	time = time.replace("\r", " ")
	time = time.replace("\n", " ")
	time = time[70:-3]
	print "  "+cam +"\t   " +string_bigendian(pos) +"\t\t" + time


def read_hall_mirror(cam,pos):
	global TID
	time = execute(lcc_write + increase_TID() + "44 80 "+ module_bitmask(cam) + string(pos) +"\"")
	# data = execute(lcc_read + increase_TID()+ "44 00 "+ module_bitmask(cam)+"\"")
	# data = data.replace("\r", " ")
	# data = data.replace("\n", " ")
	# data = data[36:-3]
	# data = data[3:] + data[:2]
	# print "  "+cam +"\t     " +string_bigendian(pos) +"\t    " + data

	time = time.replace("\r", " ")
	time = time.replace("\n", " ")
	time = time[70:-3]
	print "  "+cam +"\t   " +string_bigendian(pos) +"\t\t" + time

print bcolors.WARNING + bcolors.BOLD,
print "\rCamera\tVCM position\tRead data" + bcolors.ENDC
execute(lcc_write + increase_TID() + "00 00 " + module_bitmask("a2") + " 02\"")
time.sleep(2)
for i in camera_a:
	read_hall_lens(i, 0x0000)
	read_hall_lens(i, 0x0500)
	read_hall_lens(i, 0x0800)
	read_hall_lens(i, 0x0490)
	read_hall_lens(i, 0x0700)
	read_hall_lens(i, 0x0A00)
	read_hall_lens(i, 0xffff)
	print "--"
print " "
print bcolors.HEADER,
print "\r####################################" + bcolors.ENDC
print bcolors.WARNING + bcolors.BOLD,
print "\rCamera\tLen position\t  Read data" + bcolors.ENDC
for i in camera_bc:
	read_hall_lens(i, 0x0000)
	read_hall_lens(i, 0x0500)
	read_hall_lens(i, 0x0800)
	read_hall_lens(i, 0x0490)
	read_hall_lens(i, 0x0700)
	read_hall_lens(i, 0x0A00)
	read_hall_lens(i, 0xffff)
	print "--"

print " "
print bcolors.HEADER,
print "\r####################################" + bcolors.ENDC
print bcolors.WARNING + bcolors.BOLD,
print "\rCamera\tMirror position\t  Read data" + bcolors.ENDC
for i in camera:
	read_hall_mirror(i, 0x0000)
	read_hall_mirror(i, 0x0100)
	read_hall_mirror(i, 0x0200)
	read_hall_mirror(i, 0x010F)
	read_hall_mirror(i, 0x0150)
	read_hall_mirror(i, 0x0170)
	read_hall_mirror(i, 0xffff)
	print "--"