import argparse
import string
import subprocess
import sys

def execute(cmd):
    print "command is : " + cmd;
    subprocess.call(cmd, shell=True)
def chang_to_hex_str(x):
	chuoi_hex = 0
	if int(x) <= 0xf:
		chuoi_hex = "0x0" + hex(int(x))[2:]
	elif int(x) <= 0xff:
		chuoi_hex = "0x" + hex(int(x))[2:]
	elif int(x) <= 0xfff:
		chuoi_hex = "0x0" + hex(int(x))[2:3] + " " + "0x" + hex(int(x))[3:]
	elif int(x) <= 0xffff:
		chuoi_hex = "0x" + hex(int(x))[2:4] + " " + "0x" + hex(int(x))[3:]
	elif int(x) <= 0xfffff:
		chuoi_hex = "0x0" + hex(int(x))[2:3] + " " + "0x" + hex(int(x))[3:5] + " " + "0x" + hex(int(x))[5:]
	elif int(x) <= 0xffffff:
		chuoi_hex = "0x" + hex(int(x))[2:4] + " " + "0x" + hex(int(x))[4:6] + " " + "0x" + hex(int(x))[6:]
	else:
		print("Unsupport")
		exit()
	return chuoi_hex

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="Change dec to hex",
                    action="store")

args = parser.parse_args()
print "\n======================================================"

if args.number:
	print "number = " + str(args.number)
	print "hex = " + str(hex(int(args.number)))
	chuoi = chang_to_hex_str(args.number)
	print "number hex = " + chuoi

file = open("log.txt", "r")
print file.name
line = file.read()
line = line[:3]
print line

print "======================================================\n"