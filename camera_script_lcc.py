#!/usr/bin/env python
#*******************************************************************************
#                            REVISION HISTORY
#*******************************************************************************
# * 1.0.0	23-Sep-2016	Baseline camera_script.py
#*******************************************************************************

import argparse
import string
import subprocess
import sys
import time
import datetime
import struct

print "\
\t\t--------------------------------------------\n\
\n\n\n\
\t\t $$                                         \n\
\t\t $$                    $$            $     \n\
\t\t $$                    $$           $$     \n\
\t\t $$                    $$           $$     \n\
\t\t $$            $$$     $$           $$$$$  \n\
\t\t $$    $$     $ $$$    $$  $$$      $$$$$  \n\
\t\t $$    $$    $   $$$   $$ $ $$$     $$     \n\
\t\t $$    $$   $$    $$   $$$   $$$    $$     \n\
\t\t $$    $$   $$    $$   $$     $$    $$     \n\
\t\t $$    $$    $$  $$    $$     $$    $$$ $  \n\
\t\t $$    $$     $$$$     $$     $$     $$$   \n\
\t\t                                            \n\
\t\t                  $$$                      \n\
\t\t                $$   $$                     \n\
\t\t                $$   $$                     \n\
\t\t                  $$$                       \n\
\n\
\t\t-------------------------------------------\n\
\t\t-------------------V3.0.0------------------\n\
\t\t-----------------2016.09.23----------------\n"

atypecam = [ 'a1', 'a2', 'a3', 'a4', 'a5' ]

camera_group = [ 'AB', 'ab', 'BC', 'bc' ]

lcc_path = "adb shell \"cd data;./lcc -m 0 -s 0 "
write_path = "-w -p "
read_path = "-r -p "
workflow = "-f "


def execute(cmd):
	print(cmd);
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	return proc.communicate()[0]

def one_byte_hex(arg):
	# assume that the input is a string from 0 to 255.
	# the output will be one byte in hex.
	int_input = int(arg)
	if (int_input < 16):
		return '0' + hex(int_input)[2:]
	else:
		return hex(int_input)[2:]

def convert_to_hex(arg):
	# outputs two bytes in hex, delimited by '0x's
	fstring = arg
	rs = 0
	int_rs = 0;
	if arg.find("0x") != -1:
		rs = arg
	else:
		int_rs =  int(arg)
		rs = hex(int_rs)
	if (int_rs <= 0xf): # one nibble
		fstring = '0' + rs[-1:] + ' 00'
	elif (int_rs <= 255): # two nibbles
		fstring = rs[-2:] + ' 00'
	elif (int_rs <= 4095): # three nibbles
		fstring = rs[-2:] + ' 0' + rs[-3:-2]
	else: # four nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2]
	return fstring

def convert_to_hex_4byte(arg):
	# outputs two bytes in hex, delimited by '0x's
	rs = 0
	int_rs = 0;
	if arg.find("0x") != -1:
		rs = arg
		int_rs = arg
	else:
		int_rs =  int(arg)
		rs = hex(int_rs)
	if (int_rs <= 0xF): # one nibble
		fstring = '0' + rs[-1:] + ' 00' + ' 00' + ' 00'
	elif (int_rs <= 0xFF) and (int_rs > 0xF): # two nibbles
		fstring = rs[2:] + ' 00' + ' 00'+ ' 00'
	elif (int_rs <= 0xFFF)and (int_rs > 0xFF): # three nibbles
		fstring = rs[-2:] + ' 0' + rs[-3:-2] + ' 00' + ' 00'
	elif (int_rs <= 0xFFFF)and (int_rs > 0xFFF): # four nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' 00' + ' 00'
	elif (int_rs <= 0xFFFFF)and (int_rs > 0xFFFF): # five nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' 0' + rs[-5:-4]  + ' 00'
	elif (int_rs <= 0xFFFFFF)and (int_rs > 0xFFFFF): # six nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' ' + rs[-6:-4] + ' 00'
	elif (int_rs <= 0xFFFFFFF)and (int_rs > 0xFFFFFF): # seven nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' ' + rs[-6:-4] + ' 0' + rs[-7:-6]
	else : # eight nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' ' + rs[-6:-4] + ' ' + rs[-8:-6]
	return fstring

def resolution_convert_to_hex(arg):
	def res_x_y(x,y):
		ret = convert_to_hex_4byte(x) + " "
		ret += convert_to_hex_4byte(y)
		return ret
	return {
		'3M' : res_x_y('2104','1560'),
		'13M' : res_x_y('4208','3120'),
		'720P': res_x_y('1280','720'),
		'1080P': res_x_y('1920','1080'),
		'4K_UHD' : res_x_y('3840','2160'),
		'4K_CINEMA': res_x_y('4096','2160')
	}[arg]

def print_resolution(arg):
	return {
		'3M' : "2104 x 1560",
		'13M' : "4208 x 3120",
		'720P': "1280 x 720",
		'1080P': "1920 x 1080",
		'4K_UHD' : "3840 x 2160",
		'4K_CINEMA': "4096 x 2160"
	}[arg]

def convert_to_hex_8_bytes(arg):
	# outputs eight bytes in hex, delimited by '0x's
	fstring = arg
	rs = 0
	int_rs = 0;
	if arg.find("0x") != -1:
		print "Unsupported hexa number"
	else:
		int_rs =  int(arg)
		rs = hex(int_rs)
	if (int_rs <= 0xf): # one nibble
		fstring = '0' + rs[-1:] + ' 00 00 00 00 00 00 00'
	elif (int_rs <= 0xff): # two nibbles
		fstring = rs + ' 00 00 00 00 00 00 00'
	elif (int_rs <= 0xfff): # three nibbles
		fstring = rs[-2:] + ' 0' + rs[-3:-2] + ' 00 00 00 00 00 00'
	elif (int_rs <= 0xffff): # four nibbles
		fstring = rs[-2:] + ' '+ rs[-4:-2] + ' 00 00 00 00 00 00'
	elif (int_rs <= 0xfffff): # five nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' 0'+ rs[-5:-4] + ' 00 00 00 00 00'
	elif (int_rs <= 0xffffff): # six nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' 00 00 00 00 00'
	elif (int_rs <= 0xfffffff): # seven nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' 0' + rs[-7:-6] + ' 00 00 00 00'
	elif (int_rs <= 0xffffffff): # eight nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] + ' 00 00 00 00'
	elif (int_rs <= 0xfffffffff): # nine nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] +' 0' + rs[-9:-8] + ' 00 00 00'
	elif (int_rs <= 0xffffffffff): # ten nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] + ' ' + rs[-10:-8] + ' 00 00 00'
	elif (int_rs <= 0xfffffffffff): # eleven nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] + ' ' + rs[-10:-8] + ' 0' + rs[-11:-10] + ' 00 00'
	elif (int_rs <= 0xffffffffffff): # twelve nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] + ' ' + rs[-10:-8] + ' ' + rs[-12:-10] + ' 00 00'
	elif (int_rs <= 0xfffffffffffff): # thirteen nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] + ' ' + rs[-10:-8] + ' ' + rs[-12:-10] + ' 0' + rs[-13:-12] + ' 00'
	elif (int_rs <= 0xffffffffffffff): # fourteen nibbles
		fstring = rs[-2:] + ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] + ' ' + rs[-10:-8] + ' ' + rs[-12:-10] + ' ' + rs[-14:-12] + ' 00'
	elif (int_rs <= 0xfffffffffffffff): # fifteen nibbles
		fstring = rs[-2:]+ ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] + ' ' + rs[-10:-8] + ' ' + rs[-12:-10] + ' ' + rs[-14:-12] + ' 0' + rs[-15:-14]
	else: # sixteen nibbles
		fstring = rs[-2:]+ ' ' + rs[-4:-2] + ' '+ rs[-6:-4] + ' ' + rs[-8:-6] + ' ' + rs[-10:-8] + ' ' + rs[-12:-10] + ' ' + rs[-14:-12] + ' ' + rs[-16:-14]
	return fstring

def handle_endianness(in_string):
	# in_string should have an '0x' prepended
	# all cameras on (without global): 0x1FFFE
	in_string = in_string[2:]
	in_int = int(in_string, 16)
	#print "in_int = " + hex(in_int)
	if (in_int <= 0xf): # one nibble
		output_string = '0' + in_string + ' 00 00'
	elif (in_int <= 255): # two nibbles
		output_string = in_string[0] + in_string[1] + ' 00 00'
	elif (in_int <= 4095): # three nibbles
		output_string = in_string[1] + in_string[2] + ' 0' + in_string[0] + ' 00'
	elif (in_int <= 65535): # four nibbles
		output_string = in_string[2] + in_string[3] + ' ' + in_string[0] + in_string[1] + ' 00'
	else: # five nibbles
		output_string = in_string[3] + in_string[4] + ' ' + in_string[1] + in_string[2] + ' 0' + in_string[0]
	#print "output_string = "  + output_string
	return output_string

def dutycycle_lookup(x):
	return {
		'light' : "00 80", # 12.8%
		'Light' : "00 80",
		'medium': "00 C8", # 20%
		'Medium': "00 C8",
		'heavy' : "01 18", # 28%
		'Heavy' : "01 18"
	}[x]

def convert_dutycycle(arg):
	# converts a percentage argument into the correct 0xXX format
	# min: 0&
	# max: 28.0&
	output_string = ""

	# easy presets
	if arg == "light"  or arg == "Light" \
	or arg == "medium" or arg == "Medium"\
	or arg == "heavy"  or arg == "Heavy":
		return dutycycle_lookup(arg)

	# allow the user to enter '%' at the end if they wish
	if arg[-1:] == '%':
		arg = arg[:-1]
	arg_float = string.atof(arg)
	arg_dec = int(arg_float * 10)
	hex_string = hex(arg_dec)
	if len(hex_string) == 3:
		output_string = "00 " + hex_string[:2] + "0" + hex_string[2:]
	elif len(hex_string) == 4:
		# prepend an 0x00
		output_string = "00 " + hex_string
	elif len(hex_string) == 5:
		# prepend an 0x0, take the third character of the input, and append 0xXX
		# hacky...but it works
		output_string = "0" + hex_string[2] + " " + hex_string[-2:]
	else:
		print "hex_string = " + hex_string
		print "Should never get here. Check your duty cycle input."
		exit()
	return output_string

def list_little_endian(number):
	# takes an input and splits it into a list of bytes, LSB to MSB
	output = []
	number = int(number) # sanitize input
	# clamp for two bytes
	if number >= 65535:
		number = 65535
	#print "number = " + hex(number)
	while (number > 0):
		LSB = number & 255;
		#print "LSB = " + hex(LSB)
		output.append(LSB)
		number = number >> 8;
	# need to pad for 4 bytes
	while (len(output) < 4):
		output.append(0)
	return output

def two_byte_little_endian(input_string):
	# input format:
	# 0xXXXX
	# 0xXXX
	# 0xXX
	# 0xX
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
	return output_string;

def module_bitmask(x):
	return {
		'g' : "01 00 00",
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
		'c6': "00 00 01",
		'a' : "3E 00 00",
		'b' : "C0 07 00",
		'c' : "00 F8 01",
		'ab': "FE 07 00",
		'bc': "C0 FF 00"
	}[x]

def module_one_hot(x):
	return {
		'g' : 1,
		'a1': 2,
		'a2': 4,
		'a3': 8,
		'a4': 16,
		'a5': 32,
		'b1': 64,
		'b2': 128,
		'b3': 256,
		'b4': 512,
		'b5': 1024,
		'c1': 2048,
		'c2': 4096,
		'c3': 8192,
		'c4': 16384,
		'c5': 32768,
		'c6': 65536
}[x]

def ucid_to_hex(x):
	return {
		'preview'	: "03 00",
		'hires'		: "05 00",
		'focal'		: "06 00",
		'hdr'		: "07 00",
		'video'		: "04 00"
	}[x]

def open_byte(x):
	return {
		'hw' : "01",
		'sw' : "02",
		'cl': "00"
	}[x]

def data_type(x):
	return {
		'RAW_10'	: " 2b ",
		'LIGHT_RAW'	: " 30 "
	}[x]

def float_to_hex(f):
	return hex(struct.unpack('<I', struct.pack('<f', f))[0])

parser = argparse.ArgumentParser()

parser.add_argument("-c", "--camera", nargs='+',
					help="select camera: from a1->a5, b1->b5 or c1->c6", action="store")
parser.add_argument("-o", "--open", nargs='+', help="open or close camera",
					action="store", choices=['hw', 'sw', 'cl'])
parser.add_argument("-auto", "--auto", help="turn on/off auto mode",
					action="store", choices=['on', 'off'])
parser.add_argument("-manual", "--manual", help="turn on/off manual mode",
					action="store", choices=['on', 'off'])
parser.add_argument("-s", "--stream", nargs='+', help="stream on or off",
					action="store", choices=['on', 'off', 'sync'])
parser.add_argument("-u", "--ucid", help="ucid for setting",
					action="store", choices=['preview', 'hires', 'focal', 'video', 'hdr'])
parser.add_argument("-f", "--focus", help="select focus distance for 35mm cameras",\
					action ="store" )
parser.add_argument("-read", "--read", help="read value",
					action="store_true")
parser.add_argument("-l_m", "--lens_manual", help="nudge lens",
					action="store_true")
parser.add_argument("-m_m", "--mirror_manual", help="nudge mirror",
					action="store_true")
parser.add_argument("-l", "--lens", help="lens",
					action="store_true")
parser.add_argument("-m", "--mirror", help="mirror",
					action="store_true")
parser.add_argument("-dir", "--direction", help="direction to nudge",
					action="store")
parser.add_argument("-dc", "--dutycycle", help="duty cycle to nudge",
					action="store")
parser.add_argument("-dur", "--duration", help="duration to nudge",
					action="store")
parser.add_argument("-r", "--resolution", help="select resolution value",
					action="store", choices=['3M', '13M', '720P', '1080P', '4K_UHD', '4K_CINEMA'])
parser.add_argument("-e", "--exposure", help="select exposure value",
					action="store")
parser.add_argument("-g", "--gain", help="select gain value",type=float,
					action="store")
parser.add_argument("-fps", "--fps", help="select fps value",
					action="store")
parser.add_argument("-rhsv", "--read_hall_sensor_value",
					help="Read the hall sensor for a given 70mm or 150mm camera",
					action="store_true")
parser.add_argument("-ghsv", "--go_to_hall_sensor_value", nargs='+',
					help="Command a given 70mm or 150mm camera to move to a given hall sensor position",
					action="store")
parser.add_argument("-fn", "--fine_nudge", help="Nudge in fine increments",
					action="store_true")
parser.add_argument("-mul", "--multiplier", help="Multiplier for the fine nudge command",
					action="store")
parser.add_argument("-tx", "--tx_channel", nargs='+', help="TX channel",
					action="store", choices=['0', '1'])
parser.add_argument("-vc", "--virtual_channel", nargs='+', help="Virtual channel",
					action="store")
parser.add_argument("-dt", "--data_type", nargs='+', help="Virtual channel",
					action="store", choices=['RAW_10','LIGHT_RAW'])
parser.add_argument("-tol", "--tolerance", help="tolerance value",
					action="store")
parser.add_argument("-b", "--burst", help="burst value", action="store")
parser.add_argument("-i", "--interrupt", help="interrupt bit",
					action="store_true")

args = parser.parse_args()

isr_bit = '0'
isr_bit_ucid='1'
if args.interrupt:
	isr_bit='8'
	isr_bit_ucid='9'

if args.camera:
	# OR the one-hot encoded cameras together into one bitmask
	print "Camera(s) are " + str(args.camera)
	m_bitmask_int = 0
	for camera in args.camera:
		m_bitmask_int |= module_one_hot(camera)
	m_bitmask_str = hex(m_bitmask_int)
	# print "m_bitmask_str = " + m_bitmask_str
	m_bitmask = handle_endianness(m_bitmask_str)
	print "m_bitmask = " + m_bitmask
	print "\t\t********* Start to send commands *********\n"
	camera_string = ""
	stream_string = ""
	open_string = ""
	ucid_string = ""
	if args.open:
		print "Open %s camera" % (args.open)
		fstring = ""
		idx = 0
		for camera in args.camera:
			fstring += open_byte(args.open[idx])
			fstring += " "
			idx += 1
		open_string = lcc_path + write_path + " 00 00 00 "+isr_bit+"0 " + m_bitmask + " "\
		+ fstring +"\""
		#print open_string
		execute(open_string)
		print ""
		if args.ucid:
			ucid_string = lcc_path + write_path + " 00 00 00 "+isr_bit_ucid+"0 " + ucid_to_hex(args.ucid) + "\""
			print "Sending LIGHT_ACTIVE_UCID %s" % (args.ucid)
			#print ucid_string
			execute(ucid_string)
			print ""
	if args.stream:
		idx = 0
		for camera in args.camera:
			if (args.tx_channel or args.virtual_channel):
				if (len(args.camera) == len(args.tx_channel)) and (len(args.camera) == len(args.virtual_channel)):
					if (args.tx_channel[idx] == "0"):
						stream_string += "1"
					else:
						stream_string += "2"
					if (args.stream[idx] == 'on'):
						stream_string += "1 "
					else:
						stream_string += "0 "
					if (int(args.virtual_channel[idx]) >= 0):
						stream_string += ""
						stream_string += args.virtual_channel[idx]
					if (args.data_type and (len(args.camera) == len(args.data_type))):
						stream_string += data_type(args.data_type[idx])
					else:
						stream_string += " 00 "
				else:
					if (args.stream == 'on'):
						stream_string += "11 "
					else:
						stream_string += "10 "
					stream_string += " 00 00 "
			else:
				if (args.stream == 'on'):
					stream_string += "11"
				else:
					stream_string += "10"
				stream_string += " 00 00 "
			idx += 1
		camera_string = lcc_path + write_path + " 00 00 02 "+isr_bit+"0 "\
						+ m_bitmask + " " + stream_string + "\""
		#print camera_string
		execute(camera_string)
		print ""
else:
	if args.auto is not None or args.manual is not None :
		if args.auto == args.manual:
			print "Cannot input the same value for these args"
			exit()
		fstring = ""
		if args.auto == "on" or args.manual == "off":
			fstring = "adb shell \"echo 0 > /sys/class/light_ccb/common/manual_control\""
		else :
			fstring = "adb shell \"echo 1 > /sys/class/light_ccb/common/manual_control\""
		execute(fstring)
	elif args.burst:
		burst_string = lcc_path + write_path + " 00 00 10 "+isr_bit+"0 "\
		+ one_byte_hex(args.burst) + "\""
		execute(burst_string)
		exit()
	else:
		if not args.ucid:
			parser.print_help()

if args.ucid:
	if not args.camera:
		# Light active ucid
		ucid_string = lcc_path + write_path + " 00 00 00 "+isr_bit_ucid+"0 " + ucid_to_hex(args.ucid) + "\""
		print "Sending LIGHT_ACTIVE_UCID %s" % (args.ucid)
		#print ucid_string
		execute(ucid_string)
		exit()
if args.focus:
	fstring = ""
	# check if we have non-35mm camera
	if args.read:
		# TODO:
		print "Not yet implement"
	else:
		for camera in args.camera:
			# add the argument n number of times for n cameras
			fstring += convert_to_hex_4byte(args.focus)
			fstring += " "
		print "Focus is " + args.focus
		if args.ucid:
			ucid = ucid_to_hex(args.ucid)
			focus_string = lcc_path + write_path + " 00 00 48 "+isr_bit+"0 " + m_bitmask + \
			" " + ucid + " " + fstring + "\""
		else:
			focus_string = lcc_path + write_path + " 00 00 48 "+isr_bit+"0 " + m_bitmask +\
			" " + fstring + "\""
		#print focus_string
		execute(focus_string)
		print ""

if args.lens_manual:
	if (args.camera in atypecam):
		# 35mm
		print "Use the -f focus argument for 35mm cameras."
		exit()
	else:
		# 70mm, 150mm
		#   adb shell "echo 9 0x0000 0x51 0x00 < 3 byte module bitmask >
		#                                      < 1 byte direction >
		#                                      < 2 byte duty cycle >
		#                                      < 1 byte duration >
		#                                      > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		if args.direction and args.dutycycle and args.duration:
			direction_string = one_byte_hex(args.direction)
			dutycycle_string = convert_dutycycle(args.dutycycle)
			duration_string = one_byte_hex(args.duration)
			lens_string = lcc_path + write_path + " 00 00 51 "+isr_bit+"0 " + m_bitmask + " "\
						   + direction_string + " " + dutycycle_string + \
						   " " + duration_string + "\""
	print "Lens:"
	#print lens_string
	execute(lens_string)
	print ""

if args.mirror_manual:
	if (args.camera in atypecam):
		# 35mm
		print "no mirrors for 35mm, exiting"
		exit()
	else:
		# 70mm, 150mm
		#   adb shell "echo 7 0x0043 < 3 byte module bitmask >
		#                            < 1 byte direction >
		#                            < 2 byte duty cycle>
		#                            < 1 byte duration >
		#                            > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		if args.direction and args.dutycycle and args.duration:
			direction_string = one_byte_hex(args.direction)
			dutycycle_string = convert_dutycycle(args.dutycycle)
			duration_string = one_byte_hex(args.duration)
			mirror_string = lcc_path + write_path + " 00 00 47 "+isr_bit+"0 " + m_bitmask + " "\
						   + direction_string + " " + dutycycle_string + \
						   " " + duration_string + "\""
	#print mirror_string
	execute(mirror_string)
	print ""

if args.exposure:
	if args.camera:
		if args.read:
			# TODO:
			print "Not yet implement"
		else:
			fstring = ""
			for camera in args.camera:
				# add the argument n number of times for n cameras
				fstring += convert_to_hex_8_bytes(args.exposure)
				fstring += " "
			print "Exposure is " + args.exposure + " ns"
			if args.ucid:
				ucid = ucid_to_hex(args.ucid)
				exposure_string = lcc_path + write_path+ " 00 00 32 "+isr_bit+"0 " + m_bitmask + " " + \
				ucid + " " + fstring + "\""
			else:
				exposure_string = lcc_path + write_path+ " 00 00 32 "+isr_bit+"0 " + m_bitmask + " " + \
				fstring + "\""
			#print exposure_string
			execute(exposure_string)
			print ""
	else:
		print "Please provide a camera argument."
if args.gain:
	if args.camera:
		if args.read:
			# TODO:
			print "Not yet implement"
		else:
			fstring = ""
			for camera in args.camera:
				# add the argument n number of times for n cameras
				fstring += convert_to_hex_4byte(float_to_hex(args.gain))
				fstring += " "
			print "Total gain is " + str(args.gain)
			if args.ucid:
				ucid = ucid_to_hex(args.ucid)
				gain_string = lcc_path + write_path+ " 00 00 30 "+isr_bit+"0 " + m_bitmask\
				+ " " + ucid + " "+ fstring + "\""
			else:
				gain_string = lcc_path + write_path+ " 00 00 30 "+isr_bit+"0 " + m_bitmask\
				+ " "+ fstring +"\""
			#print gain_string
			execute(gain_string)
			print ""
	else:
		print "Please provide a camera argument."

if args.fps:
	if args.camera:
		if args.read:
			# TODO:
			print "Not yet implement"
		else:
			fstring = ""
			for camera in args.camera:
				# add the argument n number of times for n cameras
				fstring += convert_to_hex(args.fps)
				fstring += " "
			print "FPS is " + args.fps
			if args.ucid:
				ucid = ucid_to_hex(args.ucid)
				fps_string = lcc_path + write_path + " 00 00 50 "+isr_bit+"0 " + m_bitmask\
				+ " " + ucid + " "+ fstring + "\""
			else:
				fps_string = lcc_path + write_path + " 00 00 50 "+isr_bit+"0 " + m_bitmask\
				+ " "+ fstring +"\""
			#print fps_string
			execute(fps_string)
			print ""
	else:
		print "Please provide a camera argument."

if args.resolution:
	if args.camera:
		if args.read:
			# TODO:
			print "Not yet implement"
		else:
			fstring = ""
			for camera in args.camera:
				# add the argument n number of times for n cameras
				fstring += resolution_convert_to_hex(args.resolution)
				fstring += " "
			print "Resolution is " + print_resolution(args.resolution)
			if args.ucid:
				ucid = ucid_to_hex(args.ucid)
				resolution_string = lcc_path + write_path + " 00 00 2C "+isr_bit+"0 " \
				+ m_bitmask + " " + ucid + " " + fstring + "\""
			else:
				resolution_string = lcc_path + write_path + " 00 00 2C "+isr_bit+"0 " \
				+ m_bitmask + " " + fstring + "\""
			#print resolution_string
			execute(resolution_string)
			print ""
	else:
		print "Please provide a camera argument."

if args.read_hall_sensor_value:
	if not args.camera:
		print "You must provide a camera to read a hall sensor."
		exit()
	byte_count=0
	for camera in args.camera:
		if camera == 'g':
			byte_count = 2*16
			break
		else:
			byte_count +=2
	if args.lens:
		print "Reading lens hall sensor..."
		output_string = 'adb shell \"echo 5 0x0000 0x40 0x80 ' +\
			m_bitmask + ' > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w\"'
		#print output_string
		execute(output_string)
		#read_string = "adb shell \"echo " + str(byte_count) + " 0x0040 "+"> /sys/class/i2c-adapter/i2c-11/i2c-0/0-0010/i2c_br\""
		#print read_string
		#execute(read_string)
	if args.mirror:
		print "Reading mirror hall sensor..."
		output_string = "adb shell \"echo 5 0x0000 0x44 0x80 " + m_bitmask + " > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w\""
		#print output_string
		execute(output_string)
		#read_string = "adb shell \"echo " + str(byte_count) + " 0x0044 "+"> /sys/class/i2c-adapter/i2c-11/i2c-0/0-0010/i2c_br\""
		#print read_string
		#execute(read_string)

if args.go_to_hall_sensor_value:
	if not args.camera:
		print "You must provide a camera to command to move."
		exit()
	if args.lens:
		destination_string = ""
		if len(args.camera) != len(args.go_to_hall_sensor_value):
			print "Not enough arguments. For each camera selected, provide a destination."
			exit()
		for i in xrange( 0, len(args.camera)):
			destination_string = destination_string + " " + two_byte_little_endian(args.go_to_hall_sensor_value[i])
			print "Moving lens "  + str(args.camera[i]) + " to "  + args.go_to_hall_sensor_value[i] + " ..."
		args_len =  5 + (len(args.camera) * 2)
		output_string = lcc_path + write_path + " 00 00 40 "+isr_bit+"0 " + m_bitmask\
		+ destination_string + "\""
		#print output_string
		execute(output_string)
	if args.mirror:
		print "args.go_to_hall_sensor_value: " + args.go_to_hall_sensor_value[0]
		destination_string = two_byte_little_endian(args.go_to_hall_sensor_value[0])
		print "Destination is " + args.go_to_hall_sensor_value[0]
		print "Moving mirror "  + str(args.camera[0]) + " to "  + args.go_to_hall_sensor_value[0] + " ..."
		output_string = lcc_path + write_path + " 00 00 44 "+isr_bit+"0 " + m_bitmask\
		+ " " + destination_string + "\""
		#print output_string
		execute(output_string)

if args.fine_nudge:
	output_string = ""
	multiplier = 1
	direction = 1
	if args.camera:
		if args.multiplier:
			multiplier = args.multiplier
		else:
			print "No multiplier given. Using the default value of 1. "

		if args.direction:
			direction = args.direction
		else:
			print "No direction given. Using the default value of 1. "

		if args.lens:
			output_string = lcc_path + write_path + " 00 00 51 "+isr_bit+"0 " + m_bitmask + " " + \
			one_byte_hex(direction) + " " + two_byte_little_endian(hex(int(multiplier))) + \
			" " + "\""
		if args.mirror:
			output_string = lcc_path + write_path + " 00 00 52 "+isr_bit+"0 " + m_bitmask + " " + \
			one_byte_hex(direction) + " " + two_byte_little_endian(hex(int(multiplier))) + \
			" " + "\""
		#print output_string
		execute(output_string)
	else:
		print "Please provide a camera argument. "
		exit()

if args.burst:
	burst_string = lcc_path + write_path + " 00 00 10 "+isr_bit+"0 " + one_byte_hex(args.burst) + "\""
	execute(burst_string)
