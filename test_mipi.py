import argparse
import string
import subprocess
import sys
import time
import datetime

####################################################################
def execute(cmd):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	return proc.communicate()[0]

def file_len(fname):
	with open(fname) as f:
		for k, l in enumerate(f):
			pass
	return k + 1

def open_cam():
	execute("python mipi_test.py -o a1")
	time.delay(2)
	execute("python mipi_test.py -o a2")
	time.dalay(2)

def read_file(file_name,line_num):
	f = open(file_name, 'r')
	for i in range(0,line_num):		
		a = f.readline()
		b = a.rstrip('\r\n')
		if (b[len(b)-26:] == " No such file or directory")|(b == ""):
			return "FAILED"
			exit()
	return b

def check_hex_file(PATH,type_check):	
	str = open(PATH,"rb").read()
	hexStr=""
	for x in range(0, len(str)):
		if hex(ord(str[x])) == "0x0":
			break
		else:
			hexStr=hex(ord(str[x]))
			if type_check == "0_VC12_128_S":
				if (x % 2) == 0:
					if hexStr != "0x88":
						print "FAILED"
						exit()
				else:
					if hexStr != "0x99":
						print "FAILED"
						exit()
			elif type_check == "1_VC12_128_S":
			elif type_check == "0_VC13_128_S":
			elif type_check == "2_VC13_128_S":
			elif type_check == "1_VC23_128_S":
			elif type_check == "2_VC23_128_S":
			elif type_check == "0_VC123_128_S":
			elif type_check == "1_VC123_128_S":
			elif type_check == "3_VC123_128_S":
			elif type_check == "1_VC12_256_S":
			elif type_check == "0_VC13_256_S":
			elif type_check == "2_VC13_256_S":
			elif type_check == "1_VC23_256_S":
			elif type_check == "2_VC23_256_S":
			elif type_check == "0_VC123_256_S":
			elif type_check == "1_VC123_256_S":
			elif type_check == "3_VC123_256_S":
			elif type_check == "VC2_128_D":
			elif type_check == "VC3_128_D":
			elif type_check == "0_VC23_128_D":
			elif type_check == "1_VC23_128_D":
			elif type_check == "VC2_256_D":
			elif type_check == "VC3_256_D":
			elif type_check == "0_VC23_256_D":
			elif type_check == "1_VC23_256_D":
	print x
	print "PASS"


def single_preview_init():
	execute("adb reboot bootloader")
	execute("set -o errexit")
	execute("sudo fastboot -i 0x18d1 flash boot single_preview/boot.img")
	execute("sudo fastboot -i 0x18d1 flash system single_preview/system.img")
	execute("sudo fastboot -i 0x18d1 reboot")
	execute("adb wait-for-devices")
	execute("adb root")

def dual_preview_init():
	execute("adb reboot bootloader")
	execute("set -o errexit")
	execute("sudo fastboot -i 0x18d1 flash boot dual_preview/boot.img")
	execute("sudo fastboot -i 0x18d1 flash system dual_preview/system.img")
	execute("sudo fastboot -i 0x18d1 reboot")
	execute("adb wait-for-devices")
	execute("adb root")
######################################################################
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--delay", help="review delay", action="store")
args = parser.parse_args()

wait_for_apk_open = 2
wait_for_reset = 2

#---------------------------------------------------------------------#
# Single preview test                                                 #
#---------------------------------------------------------------------#
single_preview_init()
#*********************************************************************#
# Frame size 128x100 init
execute("sudo ./isp_app_p1_5 -f 1080p_128x100.bin -m program")
time.delay(10)

# test case 1: single preview VC0, snapshot VC1&2, frame size 128x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --preview_x_snapshot vc12")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
# Check Raw file 1
execute("ls *0.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"0_VC12_128_S")
# Check Raw file 2
execute("ls *1.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"1_VC12_128_S")

# test case 2: single preview VC0, snapshot VC1&3, frame size 128x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --preview_x_snapshot vc13")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
# Check Raw file 1
execute("ls *0.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"0_VC13_128_S")
# Check Raw file 2
execute("ls *2.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"2_VC13_128_S")

# test case 3: single preview VC0, snapshot VC2&3, frame size 128x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --preview_x_snapshot vc23")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
# Check Raw file 1
execute("ls *1.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"1_VC23_128_S")
# Check Raw file 2
execute("ls *2.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"2_VC23_128_S")

# test case 4: single preview VC0, snapshot VC1,2&3, frame size 128x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --preview_x_snapshot vc123")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
execute("adb pull " + read_file("test.txt", 3))
# Check Raw file 1
execute("ls *0.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"0_VC123_128_S")
# Check Raw file 2
execute("ls *1.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"1_VC123_128_S")
# Check Raw file 3
execute("ls *2.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"2_VC123_128_S")

#*********************************************************************#
# Frame size 128x100 init
execute("sudo ./isp_app_p1_5 -f 1080P_256x100.bin -m program")
time.delay(10)

# test case 5: single preview VC0, snapshot VC1&2, frame size 250x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --preview_x_snapshot vc12")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
# Check Raw file 1
execute("ls *0.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"0_VC12_256_S")
# Check Raw file 2
execute("ls *1.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"1_VC12_256_S")

# test case 6: single preview VC0, snapshot VC1&3, frame size 250x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --preview_x_snapshot vc13")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
# Check Raw file 1
execute("ls *0.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"0_VC13_256_S")
# Check Raw file 2
execute("ls *2.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"2_VC13_256_S")

# test case 7: single preview VC0, snapshot VC2&3, frame size 250x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --preview_x_snapshot vc23")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
# Check Raw file 1
execute("ls *1.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"1_VC23_256_S")
# Check Raw file 2
execute("ls *2.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"2_VC23_256_S")

# test case 8: single preview VC0, snapshot VC1,2&3, frame size 250x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --preview_x_snapshot vc123")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
execute("adb pull " + read_file("test.txt", 3))
# Check Raw file 1
execute("ls *0.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"0_VC123_256_S")
# Check Raw file 2
execute("ls *1.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"1_VC123_256_S")
# Check Raw file 3
execute("ls *2.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"2_VC123_256_S")

#---------------------------------------------------------------------#
# Dual preview test                                                   #
#---------------------------------------------------------------------#
dual_preview_init()
#*********************************************************************#
# Frame size 128x100 init
execute("sudo ./isp_app_p1_5 -f 1080p_128x100.bin -m program")
time.delay(10)

# test case 9: Dual preview VC0&1, snapshot VC2, frame size 128x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --dual_preview_snapshot vc2")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
# Check Raw file 1
execute("ls *.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"VC2_128_D")

# test case 10: Dual preview VC0&1, snapshot VC3, frame size 128x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --dual_preview_snapshot vc3")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
# Check Raw file 1
execute("ls *.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"VC3_128_D")

# test case 11: Dual preview VC0&1, snapshot VC2&3, frame size 128x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --dual_preview_snapshot vc23")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
# Check Raw file 1
execute("ls *0.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"0_VC23_128_D")
# Check Raw file 1
execute("ls *1.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"1_VC23_128_D")

#*********************************************************************#
# Frame size 128x100 init
execute("sudo ./isp_app_p1_5 -f 1080p_128x100.bin -m program")
time.delay(10)

# test case 12: Dual preview VC0&1, snapshot VC2, frame size 256x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --dual_preview_snapshot vc2")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
# Check Raw file 1
execute("ls *.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"VC2_256_D")

# test case 13: Dual preview VC0&1, snapshot VC3, frame size 256x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --dual_preview_snapshot vc3")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
# Check Raw file 1
execute("ls *.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"VC3_256_D")

# test case 14: Dual preview VC0&1, snapshot VC2&3, frame size 256x100
execute("python mipi_test.py -r")
time.dalay(wait_for_reset)
execute("rm test.txt *.raw")
execute("adb shell \"rm /data/misc/camera/*.raw\"")
open_cam()
execute("python mipi_test.py --dual_preview_snapshot vc23")
time.dalay(wait_for_apk_open)
# Wait for capture
execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
while (read_file("test.txt", 1) == "FAILED"):
	execute("adb shell \"ls /data/misc/camera/*.raw\" > test.txt")
time.delay(args.delay)
# Get raw file
execute("adb pull " + read_file("test.txt", 1))
execute("adb pull " + read_file("test.txt", 2))
# Check Raw file 1
execute("ls *0.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"0_VC23_256_D")
# Check Raw file 1
execute("ls *1.raw > test.txt")
check_hex_file(read_file("test.txt", 1),"1_VC23_256_D")
