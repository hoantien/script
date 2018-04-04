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

def rm_rawfile():
	execute("adb shell \"rm /data/misc/camera/*.lri\"")

def reset_fw():
	execute("adb shell \"cd /data/; ./prog_app_v02\"")

def check_raw_file():
	tien = execute_output("adb shell \"ls /data/misc/camera/*.lri\"")
	tien = tien.rstrip('\r\n')[len(tien)- 27:]
	if (tien == "No such file or directory"):
		return 0
	else:
		num=int(execute_output("adb shell \"cd /data/misc/camera;ls *lri | wc -l\""))
		return num

def read_file(file_name,line_num):
	f = open(file_name, 'r')
	for i in range(0,line_num):		
		a = f.readline()
		b = a.rstrip('\r\n')
		if (b[len(b)-26:] == " No such file or directory"):
			return "FAILED"
	return b

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

camera = [ 'a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5','c1', 'c2', 'c3', 'c4', 'c5', 'c6' ]
ab_camera = [ 'a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5' ]
bc_camera = [ 'b1', 'b2', 'b3', 'b4', 'b5','c1', 'c2', 'c3', 'c4', 'c5', 'c6' ]
c_camera = [ 'c1', 'c2', 'c3', 'c4', 'c5', 'c6' ]
exposure_time = [4000000000, 31250, 62500, 125000, 250000, 500000, 1000000, 2000000, 4000000, 8000000, 33333333, \
				125000000, 250000000, 500000000, 1000000000, 2000000000]
group_camera = [ 'ab', 'bc', 'c', 'abc' ]

################################################################################
##                                MAIN SCRIPT                                 ##
################################################################################
print bcolors.HEADER,
print "\r----------------------- START TESTTING --------------------------",
print bcolors.ENDC

# execute("adb root")
# num=check_raw_file()
# print num
rm_rawfile()
test = 0#len(exposure_time)
print test
for i in camera:
	for j in exposure_time:
		print ("python camera_script_asb.py -c " + i + " -u hires -o sw")
		print ("python camera_script_asb.py -c " + i + " -u hires -e "+str(j))
		print ("./capture_lcc "+i)
	file_num = check_raw_file()
	if (file_num == test):
		print bcolors.OKBLUE + bcolors.BOLD,
		print "\rPass capture camera " + i,
		print bcolors.ENDC
		execute("mkdir camera_" + i)
		execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
		execute("cd ..")
	elif (file_num != test) and (file_num != 0):
		print bcolors.FAIL + bcolors.BOLD,
		print "\rMissing " + str(test - file_num) + " files",
		print bcolors.ENDC
		execute("mkdir camera_" + i)
		execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
		execute("cd ..")
	else:
		print bcolors.FAIL + bcolors.BOLD,
		print "\rCapture camera " + i + " failed",
		print bcolors.ENDC
	rm_rawfile()

for i in group_camera:
	if (i=="ab"):
		for k in exposure_time:
			for j in ab_camera:
				print ("python camera_script_asb.py -c " + j + " -u hires -o sw")
				print ("python camera_script_asb.py -c " + j + " -u hires -e "+str(k))
			print ("./capture_lcc "+i)
		file_num = check_raw_file()
		if (file_num == test):
			print bcolors.OKBLUE + bcolors.BOLD,
			print "\rPass capture camera " + i,
			print bcolors.ENDC
			execute("mkdir camera_" + i)
			execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
			execute("cd ..")
		elif (file_num != test) and (file_num != 0):
			print bcolors.FAIL + bcolors.BOLD,
			print "\rMissing " + str(test - file_num) + " files",
			print bcolors.ENDC
			execute("mkdir camera_" + i)
			execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
			execute("cd ..")
		else:
			print bcolors.FAIL + bcolors.BOLD,
			print "\rCapture camera " + i + " failed",
			print bcolors.ENDC
	elif(i=="bc"):
		for k in exposure_time:
			for j in bc_camera:
				print ("python camera_script_asb.py -c " + j + " -u hires -o sw")
				print ("python camera_script_asb.py -c " + j + " -u hires -e "+str(k))
			print ("./capture_lcc "+i)
		file_num = check_raw_file()
		if (file_num == test):
			print bcolors.OKBLUE + bcolors.BOLD,
			print "\rPass capture camera " + i,
			print bcolors.ENDC
			execute("mkdir camera_" + i)
			execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
			execute("cd ..")
		elif (file_num != test) and (file_num != 0):
			print bcolors.FAIL + bcolors.BOLD,
			print "\rMissing " + str(test - file_num) + " files",
			print bcolors.ENDC
			execute("mkdir camera_" + i)
			execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
			execute("cd ..")
		else:
			print bcolors.FAIL + bcolors.BOLD,
			print "\rCapture camera " + i + " failed",
			print bcolors.ENDC
	elif(i=="c"):
		for k in exposure_time:
			for j in c_camera:
				print ("python camera_script_asb.py -c " + j + " -u hires -o sw")
				print ("python camera_script_asb.py -c " + j + " -u hires -e "+str(k))
			print ("./capture_lcc "+i)
		file_num = check_raw_file()
		if (file_num == test):
			print bcolors.OKBLUE + bcolors.BOLD,
			print "\rPass capture camera " + i,
			print bcolors.ENDC
			execute("mkdir camera_" + i)
			execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
			execute("cd ..")
		elif (file_num != test) and (file_num != 0):
			print bcolors.FAIL + bcolors.BOLD,
			print "\rMissing " + str(test - file_num) + " files",
			print bcolors.ENDC
			execute("mkdir camera_" + i)
			execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
			execute("cd ..")
		else:
			print bcolors.FAIL + bcolors.BOLD,
			print "\rCapture camera " + i + " failed",
			print bcolors.ENDC
	else:
		for k in exposure_time:
			for j in camera:
				print ("python camera_script_asb.py -c " + j + " -u hires -o sw")
				print ("python camera_script_asb.py -c " + j + " -u hires -e "+str(k))
			print ("./capture_lcc "+i)
		file_num = check_raw_file()
		if (file_num == test):
			print bcolors.OKBLUE + bcolors.BOLD,
			print "\rPass capture camera " + i,
			print bcolors.ENDC
			execute("mkdir camera_" + i)
			execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
			execute("cd ..")
		elif (file_num != test) and (file_num != 0):
			print bcolors.FAIL + bcolors.BOLD,
			print "\rMissing " + str(test - file_num) + " files",
			print bcolors.ENDC
			execute("mkdir camera_" + i)
			execute("cd camera_"+ i +" ; adb pull /data/misc/camera/")
			execute("cd ..")
		else:
			print bcolors.FAIL + bcolors.BOLD,
			print "\rCapture camera " + i + " failed",
			print bcolors.ENDC




print bcolors.HEADER,
print "\r------------------------ TESTTING END ---------------------------",
print bcolors.ENDC