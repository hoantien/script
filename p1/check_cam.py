#!/usr/bin/env python
import argparse
import string
import subprocess
import sys
import time
import datetime
from timeit import default_timer
from subprocess import Popen, PIPE, STDOUT

def execute(cmd):
	time.sleep(1)
	subprocess.call(cmd, shell=True)

def execute_tien(cmd):
	time.sleep(1)
	p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT,\
				close_fds=True)
	return p.stdout.read()

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class stream_on_simgle:
	a1 = "adb shell \"echo 8 0x0000 0x02 0x00 0x02 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a2 = "adb shell \"echo 8 0x0000 0x02 0x00 0x04 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a3 = "adb shell \"echo 8 0x0000 0x02 0x00 0x08 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a4 = "adb shell \"echo 8 0x0000 0x02 0x00 0x10 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a5 = "adb shell \"echo 8 0x0000 0x02 0x00 0x20 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b1 = "adb shell \"echo 8 0x0000 0x02 0x00 0x40 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b2 = "adb shell \"echo 8 0x0000 0x02 0x00 0x80 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b3 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x01 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b4 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x02 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b5 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x04 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c1 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x08 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c2 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x10 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c3 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x20 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c4 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x40 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c5 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x80 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c6 = "adb shell \"echo 8 0x0000 0x02 0x00 0x00 0x00 0x01 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""

class stream_on_dual:
	a1_a2 = "adb shell \"echo 11 0x0000 0x02 0x00 0x06 0x00 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_a3 = "adb shell \"echo 11 0x0000 0x02 0x00 0x0A 0x00 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_a4 = "adb shell \"echo 11 0x0000 0x02 0x00 0x12 0x00 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_a5 = "adb shell \"echo 11 0x0000 0x02 0x00 0x22 0x00 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b1 = "adb shell \"echo 11 0x0000 0x02 0x00 0x42 0x00 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b2 = "adb shell \"echo 11 0x0000 0x02 0x00 0x82 0x00 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b3 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x01 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b4 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x02 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b5 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x04 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c1 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x08 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c2 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x10 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c3 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x20 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c4 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x40 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c5 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x80 0x00 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c6 = "adb shell \"echo 11 0x0000 0x02 0x00 0x02 0x00 0x01 0x11 0x00 0x00 0x21 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""

class stream_off:
	off_all = "adb shell \"echo 11 0x0000 0x02 0x00 0x01 0x00 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""

class read_stream_on_simgle:
	a1 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a2 = "adb shell \"echo 5 0x0000 0x02 0x00 0x04 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a3 = "adb shell \"echo 5 0x0000 0x02 0x00 0x08 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a4 = "adb shell \"echo 5 0x0000 0x02 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a5 = "adb shell \"echo 5 0x0000 0x02 0x00 0x20 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b1 = "adb shell \"echo 5 0x0000 0x02 0x00 0x40 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b2 = "adb shell \"echo 5 0x0000 0x02 0x00 0x80 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b3 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b4 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x02 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b5 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x04 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c1 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x08 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c2 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x10 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c3 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x20 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c4 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x40 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c5 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x80 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c6 = "adb shell \"echo 5 0x0000 0x02 0x00 0x00 0x00 0x01 > /sys/class/light_ccb/i2c_interface/i2c_w\""

class read_stream_on_dual:
	a1_a2 = "adb shell \"echo 5 0x0000 0x02 0x00 0x06 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_a3 = "adb shell \"echo 5 0x0000 0x02 0x00 0x0A 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_a4 = "adb shell \"echo 5 0x0000 0x02 0x00 0x12 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a2_a5 = "adb shell \"echo 5 0x0000 0x02 0x00 0x22 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b1 = "adb shell \"echo 5 0x0000 0x02 0x00 0x42 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b2 = "adb shell \"echo 5 0x0000 0x02 0x00 0x82 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b3 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b4 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x02 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b5 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x04 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c1 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x08 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c2 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x10 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c3 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x20 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c4 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x40 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c5 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x80 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c6 = "adb shell \"echo 5 0x0000 0x02 0x00 0x02 0x00 0x01 > /sys/class/light_ccb/i2c_interface/i2c_w\""

class get_stream_return_data:
	return_data_stream = 'adb shell "echo 0x18,0x0002 > /sys/class/light_ccb/i2c_interface/i2c_addr"'
	get_return_data_stream = 'adb shell "echo 3 > /sys/class/light_ccb/i2c_interface/i2c_br"'
	get_return_data_stream_mul = 'adb shell "echo 6 > /sys/class/light_ccb/i2c_interface/i2c_br"'
	cat_return_data_stream = 'adb shell "cat /sys/class/light_ccb/i2c_interface/i2c_br"'

class open_simgle:
	a1 = "adb shell \"echo 6 0x0000 0x00 0x00 0x02 0x00 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a2 = "adb shell \"echo 6 0x0000 0x00 0x00 0x04 0x00 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a3 = "adb shell \"echo 6 0x0000 0x00 0x00 0x08 0x00 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a4 = "adb shell \"echo 6 0x0000 0x00 0x00 0x10 0x00 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a5 = "adb shell \"echo 6 0x0000 0x00 0x00 0x20 0x00 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b1 = "adb shell \"echo 6 0x0000 0x00 0x00 0x40 0x00 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b2 = "adb shell \"echo 6 0x0000 0x00 0x00 0x80 0x00 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b3 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x01 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b4 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x02 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	b5 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x04 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c1 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x08 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c2 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x10 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c3 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x20 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c4 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x40 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c5 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x80 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	c6 = "adb shell \"echo 6 0x0000 0x00 0x00 0x00 0x00 0x01 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""

class open_dual:
	a1_a2 = "adb shell \"echo 7 0x0000 0x00 0x00 0x06 0x00 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_a3 = "adb shell \"echo 7 0x0000 0x00 0x00 0x0A 0x00 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_a4 = "adb shell \"echo 7 0x0000 0x00 0x00 0x12 0x00 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_a5 = "adb shell \"echo 7 0x0000 0x00 0x00 0x22 0x00 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b1 = "adb shell \"echo 7 0x0000 0x00 0x00 0x42 0x00 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b2 = "adb shell \"echo 7 0x0000 0x00 0x00 0x82 0x00 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b3 = "adb shell \"echo 7 0x0000 0x00 0x00 0x02 0x01 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b4 = "adb shell \"echo 7 0x0000 0x00 0x00 0x02 0x02 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_b5 = "adb shell \"echo 7 0x0000 0x00 0x00 0x02 0x04 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c1 = "adb shell \"echo 7 0x0000 0x00 0x00 0x02 0x08 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c2 = "adb shell \"echo 7 0x0000 0x00 0x00 0x02 0x10 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c3 = "adb shell \"echo 6 0x0000 0x00 0x00 0x02 0x20 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c4 = "adb shell \"echo 7 0x0000 0x00 0x00 0x02 0x40 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c5 = "adb shell \"echo 7 0x0000 0x00 0x00 0x02 0x80 0x00 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""
	a1_c6 = "adb shell \"echo 7 0x0000 0x00 0x00 0x02 0x00 0x01 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w\""

class module_status:
	a1 = 'adb shell " echo 5 0x0000 0x28 0x80 0x02 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	a2 = 'adb shell " echo 5 0x0000 0x28 0x80 0x04 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	a3 = 'adb shell " echo 5 0x0000 0x28 0x80 0x08 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	a4 = 'adb shell " echo 5 0x0000 0x28 0x80 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	a5 = 'adb shell " echo 5 0x0000 0x28 0x80 0x20 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	b1 = 'adb shell " echo 5 0x0000 0x28 0x80 0x40 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	b2 = 'adb shell " echo 5 0x0000 0x28 0x80 0x80 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	b3 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	b4 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x02 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	b5 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x04 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	c1 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x08 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	c2 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x10 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	c3 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x20 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	c4 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x40 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	c5 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x80 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"'
	c6 = 'adb shell " echo 5 0x0000 0x28 0x80 0x00 0x00 0x01 > /sys/class/light_ccb/i2c_interface/i2c_w"'

class get_module_return_data:
	return_data_module = 'adb shell "echo 0x18,0x0028 > /sys/class/light_ccb/i2c_interface/i2c_addr"'
	get_return_data_module = 'adb shell "echo 4 > /sys/class/light_ccb/i2c_interface/i2c_br"'
	get_return_data_module_mul = 'adb shell "echo 8 > /sys/class/light_ccb/i2c_interface/i2c_br"'
	cat_return_data_module = 'adb shell "cat /sys/class/light_ccb/i2c_interface/i2c_br"'

def reboot_fpga():
	execute_tien("adb shell fpga_off.sh")
	execute_tien("adb shell fpga_on.sh")
	execute_tien("adb shell fpga_on.sh")
	execute_tien("adb shell \"echo 4 0x0000 0x00 0x90 0x03 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\"")
	execute_tien("adb shell \"echo 00 00 02 19 00 1F 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write\"")

def reset_fpga():
	execute_tien("adb shell fpga_on.sh")
	execute_tien("adb shell \"echo 4 0x0000 0x00 0x90 0x03 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\"")
	execute_tien("adb shell \"echo 00 00 02 19 00 1F 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write\"")

def check_data(data,cam):
	#print data
	if (data.strip("\n") == "00 00 11 "):
		print bcolors.OKBLUE + "Camera",
		print bcolors.BOLD + cam + bcolors.ENDC,
		print bcolors.OKBLUE + "is PASSED" + bcolors.ENDC
	else:
		print bcolors.FAIL + "Camera",
		print bcolors.BOLD + cam + bcolors.ENDC,
		print bcolors.FAIL + "is FAILED" + bcolors.ENDC
		reboot_fpga()

##################################################################
print bcolors.WARNING + "\rWaiting for FPGA reset" + bcolors.ENDC
reboot_fpga()
print bcolors.WARNING + "\rFPGA is ready for testing" + bcolors.ENDC

# #test a1
# reset_fpga()
# execute(open_simgle.a1)
# execute(stream_on_simgle.a1)
# execute(read_stream_on_simgle.a1)
# execute(get_stream_return_data.return_data_stream)
# execute(get_stream_return_data.get_return_data_stream)
# tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
# check_data(tmp,"A1")

# #test a2
# reset_fpga()
# execute(open_simgle.a2)
# execute(stream_on_simgle.a2)
# execute(read_stream_on_simgle.a2)
# execute(get_stream_return_data.return_data_stream)
# execute(get_stream_return_data.get_return_data_stream)
# tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
# check_data(tmp,"A2")

# #test a3
# reset_fpga()
# execute(open_simgle.a3)
# execute(stream_on_simgle.a3)
# execute(read_stream_on_simgle.a3)
# execute(get_stream_return_data.return_data_stream)
# execute(get_stream_return_data.get_return_data_stream)
# tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
# check_data(tmp,"A3")

# #test a4
# reset_fpga()
# execute(open_simgle.a4)
# execute(stream_on_simgle.a4)
# execute(read_stream_on_simgle.a4)
# execute(get_stream_return_data.return_data_stream)
# execute(get_stream_return_data.get_return_data_stream)
# tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
# check_data(tmp,"A4")

# #test a5
# reset_fpga()
# execute(open_simgle.a5)
# execute(stream_on_simgle.a5)
# execute(read_stream_on_simgle.a5)
# execute(get_stream_return_data.return_data_stream)
# execute(get_stream_return_data.get_return_data_stream)
# tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
# check_data(tmp,"A5")

#test b1
reset_fpga()
execute(open_simgle.b1)
execute(stream_on_simgle.b1)
execute(read_stream_on_simgle.b1)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"B1")

#test b2
reset_fpga()
execute(open_simgle.b2)
execute(stream_on_simgle.b2)
execute(read_stream_on_simgle.b2)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"B2")

#test b3
reset_fpga()
execute(open_simgle.b3)
execute(stream_on_simgle.b3)
execute(read_stream_on_simgle.b3)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"B3")

#test b4
reset_fpga()
execute(open_simgle.b4)
execute(stream_on_simgle.b4)
execute(read_stream_on_simgle.b4)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"B4")

#test b5
reset_fpga()
execute(open_simgle.b5)
execute(stream_on_simgle.b5)
execute(read_stream_on_simgle.b5)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"B5")

#test c1
reset_fpga()
execute(open_simgle.c1)
execute(stream_on_simgle.c1)
execute(read_stream_on_simgle.c1)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"C1")

#test c2
reset_fpga()
execute(open_simgle.c2)
execute(stream_on_simgle.c2)
execute(read_stream_on_simgle.c2)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"C2")

#test c3
reset_fpga()
execute(open_simgle.c3)
execute(stream_on_simgle.c3)
execute(read_stream_on_simgle.c3)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"C3")

#test c4
reset_fpga()
execute(open_simgle.c4)
execute(stream_on_simgle.c4)
execute(read_stream_on_simgle.c4)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"C4")

#test c5
reset_fpga()
execute(open_simgle.c5)
execute(stream_on_simgle.c5)
execute(read_stream_on_simgle.c5)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"C5")

#test c6
reset_fpga()
execute(open_simgle.c6)
execute(stream_on_simgle.c6)
execute(read_stream_on_simgle.c6)
execute(get_stream_return_data.return_data_stream)
execute(get_stream_return_data.get_return_data_stream)
tmp=execute_tien(get_stream_return_data.cat_return_data_stream)
check_data(tmp,"C6")
