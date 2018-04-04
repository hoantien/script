import argparse
import string
import subprocess
import sys
import time
import datetime
import random
import getpass

camera = ['b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','c6']
lcc_path = "adb shell \"cd data;./lcc -m 0 -s 0 "
write_path = "-w -p "
read_path = "-r -p "
isr_bit='0'
TID=0

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

html_table = ""
html_table += "\t\t<table style=\"width:100%\" border=\"1\">\n"
html_table += "\t\t\t<tr>\n"
html_table += "\t\t\t\t<th width=\"10%\">CAM</th>\n"
html_table += "\t\t\t\t<th width=\"20%\">SET VALUE</th>\n"
html_table += "\t\t\t\t<th width=\"20%\">ACTUAL</th>\n"
html_table += "\t\t\t\t<th width=\"5%\">VARIANT</th>\n"
html_table += "\t\t\t\t<th width=\"3%\">RESULT</th>\n"
html_table += "\t\t\t\t<th width=\"45%\">LOG</th>\n"
html_table += "\t\t\t</tr>\n"

d   = time.strftime("%b_%d_%Y", time.gmtime())
t   = time.strftime("%H:%M:%S", time.gmtime())
usr = getpass.getuser()
header = "\
<!DOCTYPE html>\n\
<html>\n\
\t<head>\n\
\t\t<title style=\"text-align: right;\">LENS/MIRROR TEST REPORT</title>\n\
\t\t<p style=\"text-align: center;color:red;font-weight: bold\">LENS/MIRROR TEST REPORT</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">PROJECT : Light</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">Company : Light Co.</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">Reporter: " + usr + "</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">Date    : " + time.strftime("%b-%d-%Y") + "</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">Finished: " + t + "</p>\n\
\t\t<style>\
table, th, td { \
	border: 1px solid black; \
	border-collapse: collapse; \
}\
th {\
	background-color: #4CAF10;\
	color: white;\
}\
\t\t</style>\
\t</head>\n"

def update(a, b):
	html = open("report.html", "w+")    
	html.write(a)
	html.write(b)
	html.close()
def toint(x):
	return {
		'1': 1,
		'2': 2,
		'3': 3,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 7,
		'8': 8,
		'9': 9,
		'0': 0,
		'a': 0xa,
		'b': 0xb,
		'c': 0xc,
		'd': 0xd,
		'e': 0xe,
		'f': 0xf,
		'A': 0xa,
		'B': 0xb,
		'C': 0xc,
		'D': 0xd,
		'E': 0xe,
		'F': 0xf,
	}[x]
def module_bitmask(x):
	return {
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
		'c6': "00 00 01",
	}[x]

def two_byte_little_endian(input_string):
	if input_string.find("0x") != -1:
		input_string = input_string[2:]
	if len(input_string) == 1:   # one nibble
		output_string = '0' + input_string + ' 00'
	elif len(input_string) == 2: # two nibbles
		output_string = input_string[0] + input_string[1]  + ' 00'
	elif len(input_string) == 3: # three nibbles
		output_string = input_string[1] + input_string[2]  + ' 0' + input_string[0]
	elif len(input_string) == 4: # four nibbles
		output_string = input_string[2] + input_string[3] + ' ' + input_string[0] + input_string[1]
	return output_string

def execute(cmd):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	return proc.communicate()[0]

def reset_fw(x):
	print "Reset firmware ..."
	execute("adb shell \"cd /data/; ./prog_app_p2\"")
	time.sleep(x)
	print "Done"

def increase_TID():
	global TID
	TID = TID+1
	if (TID<0x10):
		return " 00 0"+str(hex(TID))[2:]
	elif ((TID>0xF) & (TID < 0x100)):
		return " 00 "+str(hex(TID))[2:]
	elif ((TID>0xFF) & (TID < 0x1000)):
		return " 0"+str(hex(TID))[2:-2] + " " + str(hex(TID))[3:]
	else:
		return " " +str(hex(TID))[2:-2] + " " + str(hex(TID))[4:]

def move_lens(cam,postion):
	destination_string= " " + two_byte_little_endian(str(hex(postion)))
	string = lcc_path + write_path + increase_TID() + " 40 "\
			+isr_bit+"0 " + module_bitmask(cam) + destination_string + "\""
	execute(string)

def move_mirror(cam,postion):
	destination_string= " " + two_byte_little_endian(str(hex(postion)))
	string = lcc_path + write_path + increase_TID() + " 44 "\
			+isr_bit+"0 " + module_bitmask(cam) + destination_string + "\""
	execute(string)

def read_lens(cam):
	string = lcc_path + read_path + increase_TID() + " 40 00 "+ \
					module_bitmask(cam) + "\""
	data = execute(string)
	data = data.replace("\r", " ")
	data = data.replace("\n", " ")
	data = data[36:-3]
	data = data[3:] + data[:2]
	return data

def read_mirror(cam):
	string = lcc_path + read_path + increase_TID() + " 44 00 "+ \
					module_bitmask(cam) + "\""
	data = execute(string)
	data = data.replace("\r", " ")
	data = data.replace("\n", " ")
	data = data[36:-3]
	data = data[3:] + data[:2]
	return data

def StrtoHex(s):
	if (len(s) == 4) :
		data = toint(s[:1])*0x1000 + toint(s[1:2])*0x100 + toint(s[2:3])*0x10 + toint(s[3:])
	elif (len(s) == 3):
		data = toint(s[:1])*0x100 + toint(s[1:2])*0x10 + toint(s[2:])*0x1
	elif (len(s) == 2):
		data = toint(s[:1])*0x10 + toint(s[1:])*0x1
	elif (len(s) == 1):
		data = toint(s)*0x1
	else:
		print s
		print "Invalid"
		exit()
	return data

def calib_lens(cam):
	data = ['','']
	move_lens(cam,0)
	time.sleep(2)
	data[0]=read_lens(cam)
	move_lens(cam,0xffff)
	time.sleep(2)
	if data[1] == 'FFFF':
		move_lens(cam,0xffff)
		time.sleep(5)
		data[1]=read_lens(cam)
	if data[1] == 'FFFF':
		data[1]='0000'
	return data

def calib_mirror(cam):
	data = ['','']
	move_mirror(cam,0)
	time.sleep(3)
	data[0]=read_mirror(cam)
	move_mirror(cam,0xffff)
	time.sleep(3)
	data[1]=read_mirror(cam)
	if data[1] == 'FFFF':
		move_mirror(cam,0xffff)
		time.sleep(5)
		data[1]=read_mirror(cam)
	if data[1] == 'FFFF':
		data[1]='0000'
	return data

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--count",type=int, action="store")
parser.add_argument("-s", "--size",type=int, action="store")
parser.add_argument("-r", "--random", action="store_true")
parser.add_argument("-l", "--lens", action="store_true")
parser.add_argument("-m", "--mirror", action="store_true")
parser.add_argument("-c", "--camera", nargs='+',help="select camera: b1->b5 or c1->c6",
					choices=['b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','c6'], action="store")
args = parser.parse_args()

def move_camera(cam,position):
	if args.lens:
		move_lens(cam,position)
	elif args.mirror:
		move_mirror(cam,position)

def read_camera(cam):
	if args.lens:
		data=read_lens(cam)
	elif args.mirror:
		data=read_mirror(cam)
	return data

def calib(cam):
	data = ['','']
	if args.lens:
		data=calib_lens(cam)
	elif args.mirror:
		data=calib_mirror(cam)
	return data
################################################################################
for i in args.camera:
	index=0
	hardstop=calib(i)
	if args.count:
		while index < args.count:
			index=index+1
			print bcolors.WARNING,
			print "\rLoop " + str(index) + bcolors.ENDC
			if args.random:
				hallcode = random.randint(StrtoHex(hardstop[0]),StrtoHex(hardstop[1]))
				move_camera(i,hallcode)
				actual=read_camera(i)
				variance = StrtoHex(actual) - hallcode
				if variance <=2 and variance >=-2:
					result = bcolors.OKBLUE + 'PASS' + bcolors.ENDC
				else:
					result = bcolors.FAIL + 'FAIL' + bcolors.ENDC
				print "Camera " + i + "\tExp: " + str(hex(hallcode)) + "\tActual: " + actual + "\tVariance: " + str(variance) + "\t" + result
				html_table += "\t\t\t<tr>\n"
				html_table += "\t\t\t\t<td>" + i + "</td>\n"
				html_table += "\t\t\t\t<td>" + str(hex(hallcode)) + "</td>\n"
				html_table += "\t\t\t\t<td>" + actual + "</td>\n"
				html_table += "\t\t\t\t<td>" + str(variance) + "</td>\n"
				#html_table += "\t\t\t\t<td>" + result + "</td>\n"
				if "PASS" in result:
					html_table += "\t\t\t\t<td style=\"background-color:green\">PASSED</td>\n"
				else:
					html_table += "\t\t\t\t<td style=\"background-color:red\">FAILED</td>\n"
			elif args.size:
				hallcode = StrtoHex(hardstop[0])
				while hallcode < StrtoHex(hardstop[1]):
					hallcode = hallcode+args.size
					move_camera(i,hallcode)
					actual=read_camera(i)
					variance = StrtoHex(actual) - hallcode
					if variance <=2 and variance >=-2:
						result = bcolors.OKBLUE + 'PASS' + bcolors.ENDC
					else:
						result = bcolors.FAIL + 'FAIL' + bcolors.ENDC
					print "Camera " + i + "\tExp: " + str(hex(hallcode)) + "\tActual: " + actual + "\tVariance: " + str(variance) + "\t" + result
					html_table += "\t\t\t<tr>\n"
					html_table += "\t\t\t\t<td>" + i + "</td>\n"
					html_table += "\t\t\t\t<td>" + str(hex(hallcode)) + "</td>\n"
					html_table += "\t\t\t\t<td>" + actual + "</td>\n"
					html_table += "\t\t\t\t<td>" + str(variance) + "</td>\n"
					# html_table += "\t\t\t\t<td>" + result + "</td>\n"
					if "PASS" in result:
						html_table += "\t\t\t\t<td style=\"background-color:green\">PASSED</td>\n"
					else:
						html_table += "\t\t\t\t<td style=\"background-color:red\">FAILED</td>\n"
				while hallcode > StrtoHex(hardstop[0]):
					hallcode = hallcode-args.size
					move_camera(i,hallcode)
					actual=read_camera(i)
					variance = StrtoHex(actual) - hallcode
					if variance <=2 and variance >=-2:
						result = bcolors.OKBLUE + 'PASS' + bcolors.ENDC
					else:
						result = bcolors.FAIL + 'FAIL' + bcolors.ENDC
					print "Camera " + i + "\tExp: " + str(hex(hallcode)) + "\tActual: " + actual + "\tVariance: " + str(variance) + "\t" + result
					html_table += "\t\t\t<tr>\n"
					html_table += "\t\t\t\t<td>" + i + "</td>\n"
					html_table += "\t\t\t\t<td>" + str(hex(hallcode)) + "</td>\n"
					html_table += "\t\t\t\t<td>" + actual + "</td>\n"
					html_table += "\t\t\t\t<td>" + str(variance) + "</td>\n"
					#html_table += "\t\t\t\t<td>" + result + "</td>\n"
					if "PASS" in result:
						html_table += "\t\t\t\t<td style=\"background-color:green\">PASSED</td>\n"
					else:
						html_table += "\t\t\t\t<td style=\"background-color:red\">FAILED</td>\n"    
html_table += "\t\t\t\t<td></td>\n"
html_table += "\t\t\t</tr>\n"
html_table += "\t\t</table>\n"
update(header, html_table)