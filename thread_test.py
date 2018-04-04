#!/usr/bin/python

import argparse
import string
import subprocess
import sys
import time
import datetime
import struct
import os
# import thread
from multiprocessing import Process


def execute(cmd):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	return proc.communicate()[0]

def info(title):
	print title
	print 'module name:', __name__
	if hasattr(os, 'getppid'):  # only available on Unix
		print 'parent process:', os.getppid()
	print 'process id:', os.getpid()

def f(name):
	info('function f')
	while 1:
		print 'hello', name
		time.sleep(1)


p = Process(target=f, args=('bob',))
p.start()
# p.join()
print "tien"
time.sleep(1)
p.join()