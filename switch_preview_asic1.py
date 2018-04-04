import argparse
import string
import subprocess
import sys
import time
import datetime

camera= [ 'a1', 'a5', 'b2', 'b4', 'b5','c5']
lcc_write = "adb shell \"cd \data; ./lcc -m 0 -s 0 -w -p "
lcc_read = "adb shell \"cd \data; ./lcc -m 0 -s 0 -r -p "

TID=2

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

def open_cam_asic1():
	global TID
	for i in camera:
		execute(lcc_write + increase_TID() + "00 00 " + module_bitmask(i) + " 02\"")
		time.sleep(2)
	execute(lcc_write + increase_TID() + "00 10 " " 03 00\"")
