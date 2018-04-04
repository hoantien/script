#!/usr/bin/env python
import argparse
import string
import subprocess
import sys
import time
import datetime
from timeit import default_timer
from subprocess import Popen, PIPE, STDOUT

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
	p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT,\
				close_fds=True)
	return p.stdout.read()

def execute_output(cmd):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	return proc.communicate()[0]

def file_len(fname):
	with open(fname) as f:
		for k, l in enumerate(f):
			pass
	return k + 1

def open_cam():
	execute("python mipi_test.py -o a1")
	time.sleep(2)
	execute("python mipi_test.py -o a2")
	time.sleep(2)

def read_file(file_name,line_num):
	f = open(file_name, 'r')
	for i in range(0,line_num):     
		a = f.readline()
		b = a.rstrip('\r\n')
		if (b[len(b)-26:] == " No such file or directory"):
			return "FAILED"
	return b

def rm_rawfile():
	execute("adb shell \" rm /data/misc/camera/*.raw\"")

def reset_fw():
	execute("adb shell \"cd data; ./prog_app_v02\"")

################################################################################
parser = argparse.ArgumentParser()

args = parser.parse_args()

################################################################################
##                                MAIN SCRIPT                                 ##
################################################################################

capture_AB="adb shell \"cd data; ./lcc -m 0 -s 0 -f 1 FE 07 00 11 21 00\""
capture_BC="adb shell \"cd data; ./lcc -m 0 -s 0 -f 1 C0 FF 01 11 21 00\""
capture_C="adb shell \"cd data; ./lcc -m 0 -s 0 -f 1 00 F8 01 11 21 00\""
capture_ABC="adb shell \"cd data; ./lcc -m 0 -s 0 -f 1 FE FF 01 11 21 00\""

print bcolors.HEADER,
print "\r----------------------- START CAPTURE TESTTING --------------------------",
print bcolors.ENDC
i=0
while i <=1:
	# rm_rawfile()
	# time.sleep(3)

	# reset_fw()
	# print "tien"
	# execute_output('adb shell "miniterm -s 115200 /dev/ttyHSL1" 2>&1 | tee ASIC1_log.txt &')
	# execute_output('adb shell "miniterm -s 115200 /dev/ttyHSL2" 2>&1 | tee ASIC2_log.txt &')
	# execute_output('adb shell "miniterm -s 115200 /dev/ttyHSL3" 2>&1 | tee ASIC3_log.txt &')

	# i=i+1
	# # execute_output(capture_BC)
	reset_fw()
	execute_output('adb shell "miniterm -s 115200 /dev/ttyHSL1" 1> ASIC1_log.txt &')
	i=i+1


print bcolors.HEADER,
print "\r------------------------ CAPTURE TESTTING END ---------------------------",
print bcolors.ENDC
