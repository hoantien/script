import argparse
import string
import subprocess
import sys
import time
import datetime
import random
import xlwt
from datetime import datetime
import os
import getpass
import time
import ctypes

camera = ['a1','a2','a3','a4','a5','b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','c6']
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
	}[x]

def two_byte_little_endian(input_string):
	if input_string.find("-0x") != -1:
		input_string = input_string[3:]
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

def move_vcm(cam,postion):
	destination_string= " " + two_byte_little_endian(str(postion))
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
	data = data[208:-3]
	data = data[3:] + data[:2]
	# print data
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

def tohex(val, nbits):
	return hex((val + (1 << nbits)) % (1 << nbits))

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
	move_lens(cam,0x8001)
	time.sleep(2)
	data[0]=read_lens(cam)
	move_lens(cam,0x7fff)
	time.sleep(2)
	data[1]=read_lens(cam)
	# if data[1] == '7FFF':
	# 	move_lens(cam,0x7fff)
	# 	time.sleep(5)
	# 	data[1]=read_lens(cam)
	# if data[1] == '7FFF':
	# 	data[1]='8001'
	print data
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
parser.add_argument("-o", "--file_name", action="store")
parser.add_argument("-s", "--size",type=int, action="store")
parser.add_argument("-v", "--variance",type=int, action="store")
parser.add_argument("-r", "--random", action="store_true")
parser.add_argument("-l", "--lens", action="store_true")
parser.add_argument("-m", "--mirror", action="store_true")
parser.add_argument("-c", "--camera", nargs='+',help="select camera: b1->b5 or c1->c6", action="store")
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
def generate_html(r={}):
	'''
	@summary	: Generate HTML code of a table from input dictionary
	@param	  : specific function
	@return	 : {status, output}
	@attention  : Generate HTML code of a table from input dictionary
	'''
	det = r['details']
	sum = r['summary']
	#Report summary
	s_table = "\t\t\t<p style=\"font-weight: bold;\">TEST SUMMARY</p>\n"
	s_table += "<table style=\"width:100%\" border=\"1\">\r\n"
	# Generate header
	s_table += "<tr>\r\n"
	s_table += "<th width=\"40%\">brief</th>\r\n"
	s_table += "<th width=\"15%\">total</th>\r\n"
	s_table += "<th width=\"15%\">passed</th>\r\n"
	s_table += "<th width=\"15%\">failed</th>\r\n"
	s_table += "<th width=\"15%\">result</th>\r\n"
	s_table += "</tr>\r\n"
	# Generate column
	for tc in sum.keys():
		s_table += '<tr>\r\n'
		s_table += '<td> <a href=\"#' + sum[tc]['id'] + '\">'  + sum[tc]['id'] + '</a></td>\r\n'
		s_table += '<td>' + str(sum[tc]['total'])  + '</td>\r\n'
		s_table += '<td>' + str(sum[tc]['passed'])  + '</td>\r\n'
		s_table += '<td>' + str(sum[tc]['failed'])  + '</td>\r\n'
		if(sum[tc]['result'] == "PASSED"):
			s_table += '<td style=\"background-color:green\">' + \
						sum[tc]['result'] + '</td>\r\n'
		else:
			s_table += '<td style=\"background-color:red\">' + \
					   sum[tc]['result'] + '</td>\r\n'
		s_table += '</tr>\r\n'
	s_table += "</table>\r\n"
	#Report details
	s_table += "\t\t\t<p style=\"font-weight: bold;\">REPORT DETAILS</p>\n"
	for tc in det.keys():
		s_table += "<table style=\"width:100%\" border=\"1\">\r\n"
		s_table += "\t\t\t<h id="+ tc + ">" + tc + " <a href=\"#top\">Top</a></h>\n"
		# Generate header
		s_table += "<tr>\r\n"
		s_table += "<th width=\"20%\">id</th>\r\n"
		s_table += "<th width=\"20%\">expected</th>\r\n"
		s_table += "<th width=\"20%\">actual</th>\r\n"
		s_table += "<th width=\"20%\">tolerance</th>\r\n"
		s_table += "<th width=\"20%\">result</th>\r\n"
		s_table += "</tr>\r\n"
		# Generate column
		for i in range(len(det[tc]['id'])):
			s_table += '<tr>\r\n'
			s_table += '<td>' + det[tc]['id'][i]	+ '</td>\r\n'
			s_table += '<td>' + det[tc]['expected'][i]	  + '</td>\r\n'
			s_table += '<td>' + det[tc]['actual'][i] + '</td>\r\n'
			s_table += '<td>' + det[tc]['tolerance'][i]   + '</td>\r\n'
			if (det[tc]['result'][i] == "PASSED"):
				s_table += '<td style=\"background-color:green\">' \
							+ det[tc]['result'][i]   + '</td>\r\n'
			else:
				s_table += '<td style=\"background-color:red\">' \
						   + det[tc]['result'][i]   + '</td>\r\n'
			s_table += '</tr>\r\n'
		s_table += "</table>"
	return s_table
def report(r={}):
	d   = time.strftime("%b_%d_%Y", time.gmtime())
	t   = time.strftime("%H:%M:%S", time.gmtime())
	usr = getpass.getuser()
	header = "\
<!DOCTYPE html>\n\
<html>\n\
\t<head>\n\
\t\t<title style=\"text-align: right;\">FACTORY TEST REPORT</title>\n\
\t\t<p style=\"text-align: center;color:red;font-weight: bold\">FACTORY TEST REPORT</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">PROJECT : Light</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">Company : Light Co.</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">Reporter: " + usr + "</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">Date	: " + time.strftime("%b-%d-%Y") + "</p>\n\
\t\t<p style=\"text-align: left;color:blue;\">Finished: " + t + "</p>\n\
\t\t<style>\
table, th, td { \
	border: 1px solid black; \
	border-collapse: collapse; \
}\
th {\
	background-color: #4CAF50;\
	color: white;\
}\
\t\t</style>\
\t</head>\n"
	# Create new file 
	if os.path.exists(	"FTM_Test_Report_" + d + ".html"):
		os.system("rm " + "FTM_Test_Report_" + d + ".html")
	html = open("FTM_Test_Report_" + d + ".html", "w+")
	# Write header of report
	html.write(header)
	# Write test body
	html.write("\t<body>\n")
	html.write(generate_html(r))
	html.write("\t</body>\n")
	html.write("</html>\n")
	html.close()
################################################################################

# move_lens('a5',0)
# read_lens('a5')
pass_num=0
fail_num=0
wb = xlwt.Workbook()
styleNormal = xlwt.easyxf('font: name Times New Roman')
styleHeading = xlwt.easyxf('font: name Times New Roman,color-index black, bold on')
styleFail = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')
stylePass = xlwt.easyxf('font: name Times New Roman, color-index green, bold on')
details = {}
summary = {}
rp = {}
for i in args.camera:
	ws = wb.add_sheet(i+' Test result')
	pass_num=0
	fail_num=0
	index=0
	row=0
	col=0
	ws.write(row, col, 'Expected',styleHeading)
	col = col + 1
	ws.write(row, col, 'Actual Position',styleHeading)
	col = col + 1
	ws.write(row, col, 'Tolerance',styleHeading)
	col = col + 1
	ws.write(row, col, 'Judgment',styleHeading)
	row= row + 1
	hardstop=calib(i)
	print hardstop
	sum = {}
	tc_details = {}
	if args.count:
		tc_id       = []
		tc_exp      = []
		tc_act      = []
		tc_tor      = []
		tc_result   = []
		tc_total    = 0
		tc_pass     = 0
		tc_failed   = 0
		tc_judgment = 1
		while index < args.count:
			index=index+1
			tc_id.append(i + "_%04d" % index)
			if args.random:
				if ((StrtoHex(hardstop[1])-StrtoHex(hardstop[0]))> 10):
					hallcode = random.randint(StrtoHex(hardstop[0]),StrtoHex(hardstop[1]))
					move_camera(i,hallcode)
					actual=read_camera(i)
					variance = StrtoHex(actual) - hallcode
					if variance <=2 and variance >=-2:
						pass_num = pass_num + 1
						result = bcolors.OKBLUE + 'PASS' + bcolors.ENDC
						result_t='PASS'
						tc_judgment &= 1
						tc_pass += 1
					else:
						fail_num = fail_num + 1
						result = bcolors.FAIL + 'FAIL' + bcolors.ENDC
						result_t='FAIL'
						tc_judgment &= 0
						tc_failed   += 1
					print "Camera " + i + "\tExp: " + str(hex(hallcode)) + "\tActual: " + actual + "\tVariance: " + str(variance) + "\t" + result
					col = 0
					ws.write(row, col, str(hex(hallcode)),styleNormal)
					col = col + 1
					ws.write(row, col, actual,styleNormal)
					col = col + 1
					ws.write(row, col, str(variance),styleNormal)
					col = col + 1
					if result_t == 'PASS':
						ws.write(row, col, result_t, stylePass)
					else:
						ws.write(row, col, result_t, styleFail)
					col = col + 1
					row = row + 1
					tc_exp.append(str(hex(hallcode)))
					tc_act.append(actual)
					tc_tor.append(str(variance))
					tc_result.append(result_t)
					tc_total += 1
			elif args.size:
				hallcode = ctypes.c_int16(StrtoHex(hardstop[0])).value
				while hallcode < ctypes.c_int16(StrtoHex(hardstop[1])).value:
					hallcode = hallcode + ctypes.c_int16(args.size).value
					if hallcode > ctypes.c_int16(StrtoHex(hardstop[1])).value:
						hallcode = ctypes.c_int16(StrtoHex(hardstop[1])).value
					# print str(tohex(hallcode,16))
					move_vcm(i,tohex(hallcode,16))
					actual=read_camera(i)
					variance = ctypes.c_int16(StrtoHex(actual)).value - hallcode
					if variance <=args.variance and variance >=(-1*args.variance):
						pass_num = pass_num + 1
						result = bcolors.OKBLUE + 'PASS' + bcolors.ENDC
						result_t='PASS'
						tc_judgment &= 1
						tc_pass += 1
					else:
						fail_num = fail_num + 1
						result = bcolors.FAIL + 'FAIL' + bcolors.ENDC
						result_t='FAIL'
						tc_judgment &= 0
						tc_failed   += 1
					print "Camera " + i + "\tExp: " + str(hallcode) + "\tActual: " + str(ctypes.c_int16(StrtoHex(actual)).value) + "\tVariance: " + str(variance) + "\t" + result
					col = 0
					ws.write(row, col, str(hex(hallcode)),styleNormal)
					col = col + 1
					ws.write(row, col, actual,styleNormal)
					col = col + 1
					ws.write(row, col, str(variance),styleNormal)
					col = col + 1
					if result_t == 'PASS':
						ws.write(row, col, result_t, stylePass)
					else:
						ws.write(row, col, result_t, styleFail)
					col = col + 1
					row = row + 1
					tc_exp.append(str(hex(hallcode)))
					tc_act.append(actual)
					tc_tor.append(str(variance))
					tc_result.append(result_t)
					tc_total += 1
				while hallcode > StrtoHex(hardstop[0]):
					hallcode = hallcode-args.size
					if hallcode < StrtoHex(hardstop[0]):
						hallcode = StrtoHex(hardstop[0])
					move_camera(i,hallcode)
					actual=read_camera(i)
					variance = StrtoHex(actual) - hallcode
					if variance <=2 and variance >=-2:
						pass_num = pass_num + 1
						result = bcolors.OKBLUE + 'PASS' + bcolors.ENDC
						result_t='PASS'
						tc_judgment &= 1
						tc_pass += 1
					else:
						fail_num = fail_num + 1
						result = bcolors.FAIL + 'FAIL' + bcolors.ENDC
						result_t='FAIL'
						tc_judgment &= 0
						tc_failed   += 1
					print "Camera " + i + "\tExp: " + str(hex(hallcode)) + "\tActual: " + actual + "\tVariance: " + str(variance) + "\t" + result
					col = 0
					ws.write(row, col, str(hex(hallcode)),styleNormal)
					col = col + 1
					ws.write(row, col, actual,styleNormal)
					col = col + 1
					ws.write(row, col, str(variance),styleNormal)
					col = col + 1
					if result_t == 'PASS':
						ws.write(row, col, result_t, stylePass)
					else:
						ws.write(row, col, result_t, styleFail)
					col = col + 1
					row = row + 1
					tc_exp.append(str(hex(hallcode)))
					tc_act.append(actual)
					tc_tor.append(str(variance))
					tc_result.append(result_t)
					tc_total += 1
		tc_details['expected'] = tc_exp
		tc_details['actual']   = tc_act
		tc_details['tolerance']= tc_tor
		tc_details['result']   = tc_result
		tc_details['id']       = tc_id
	sum['passed'] = tc_pass
	sum['failed'] = tc_failed
	sum['total']  = tc_total
	sum['id']     = "Test camera " + i
	sum['result'] = ""
	if (sum['failed'] == 0):
		sum['result'] = "PASSED"
	else:
		sum['result'] = "FAILED"
	summary[i] = sum
	details[i] = tc_details
	print " Camera " + i + "\t" + str(pass_num) + " PASS" + "\t" +str(fail_num) +" FAIL"
	row = row + 5
	col=0
	ws.write(row, col, 'Camera module',styleHeading)
	col = col + 1
	ws.write(row, col, 'PASS',stylePass)
	col = col + 1
	ws.write(row, col, 'FAIL',styleFail)
	row= row + 1
	col = 0
	ws.write(row, col, i,styleHeading)
	col = col + 1
	ws.write(row, col, pass_num,stylePass)
	col = col + 1
	ws.write(row, col, fail_num,styleFail)
	col = col + 1
rp['summary'] = summary
rp['details'] = details
# report(rp)
if args.file_name:
	wb.save(args.file_name + '.xls')
else:
	wb.save(str(datetime.now())+'_actuator_result.xls')

