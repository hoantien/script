import argparse
import string
import subprocess
import sys
import time
import datetime
import os
import signal
from timeit import default_timer

trans_ID = 1

def change_trans_ID (x):
    ID = hex(int(x))
    ID_string=''
    if len(ID) <=3:
        ID_string = '0x000'+ID[2:]
    elif len(ID) <=4:
        ID_string = '0x00'+ID[2:]
    elif len(ID) <=5:
        ID_string = '0x0'+ID[2:]    
    else:
        ID_string = ID
    return str(ID_string)

def execute(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()[0]

def file_len(fname):
    with open(fname) as f:
        for k, l in enumerate(f):
            pass
    return k + 1

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
        fstring = '0x0' + rs[-1:] + ' 0x00' 
    elif (int_rs <= 255): # two nibbles
        fstring = rs + ' 0x00' 
    elif (int_rs <= 4095): # three nibbles
        fstring = '0x' + rs[-2:] + ' 0x0' + rs[-3:-2] 
    else: # four nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2]

    return fstring

def split_bytes(arg):
    # assume the user always inputs 4 digits (i.e the leading nibbles
    # in each byte are nonzero, so we get 4 digits)
    int_input = len(arg)
    # print int_input
    if (arg[:2] == '0x'):
        if (int_input < 6):
        	fstring = '0x' + arg[-2:] + ' 0x0' + arg[2:3]
        else:
    	    fstring = '0x' + arg[-2:] + ' ' +  arg[0:4]
        return fstring
    else:
       print "Not support this value"

def handle_endianness(in_string):
    # in_string should have an '0x' prepended

    # all cameras on (without global): 0x1FFFE
    in_string = in_string[2:]
    in_int = int(in_string, 16)
    #print "in_int = " + hex(in_int)
    if (in_int <= 0xf): # one nibble
        output_string = '0x0' + in_string + ' 0x00 0x00'
    elif (in_int <= 255): # two nibbles
        output_string = '0x' + in_string[0] + in_string[1] + ' 0x00 0x00'
    elif (in_int <= 4095): # three nibbles
        output_string = '0x' + in_string[1] + in_string[2] + ' 0x0' + in_string[0] + ' 0x00'
    elif (in_int <= 65535): # four nibbles
        output_string = '0x' + in_string[2] + in_string[3] + ' 0x' + in_string[0] + in_string[1] + ' 0x00'
    else: # five nibbles
        output_string = '0x' + in_string[3] + in_string[4] + ' 0x' + in_string[1] + in_string[2] + ' 0x0' + in_string[0]
    #print "output_string = "  + output_string
    return output_string

def module_one_hot(x):
    return {
    	'g':1,
        'a1': 2,
        'a2': 4,
        'a3': 8,
        'a4': 16,
        'a5': 32,
    	'a': 62,
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

def command_status(x):
    line = '02 00 00 00 '
    while line == '02 00 00 00 ':
        status_string = "adb shell \"echo 4 " + change_trans_ID(x) +" 0x24 0x80 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_addr\""
        execute(status_string)
        execute("adb shell \"echo 0x18,0x0024 > /sys/class/light_ccb/i2c_interface/i2c_addr\"")
        execute("adb shell \"echo 4 > /sys/class/light_ccb/i2c_interface/i2c_br\"")
        execute("adb shell \"cat /sys/class/light_ccb/i2c_interface/i2c_br\" > test_speed.txt")
        f = open('test_speed.txt', 'r')
        line = f.readline()

def get_len_value(bitmask_t):
    len_value_string = "adb shell \"echo 5 " + change_trans_ID(trans_ID) +" 0x40 0x80 "+ bitmask_t +" > /sys/class/light_ccb/i2c_interface/i2c_w\""
    execute(len_value_string)
    execute("adb shell \"echo 0x18,0x0040 > /sys/class/light_ccb/i2c_interface/i2c_addr\"")
    execute("adb shell \"echo 2 > /sys/class/light_ccb/i2c_interface/i2c_br\"")
    execute("adb shell \"cat /sys/class/light_ccb/i2c_interface/i2c_br\" > len_position.txt")
    f = open('len_position.txt', 'r')
    line = f.readline()
    return line

def read_temp(bitmask_t):
    read_temp_string = "adb shell \"echo 5 " + change_trans_ID(trans_ID) +" 0xA5 0x80 "+ bitmask_t +" > /sys/class/light_ccb/i2c_interface/i2c_w\""
    execute(read_temp_string)
    execute("adb shell \"echo 0x18,0x00A5 > /sys/class/light_ccb/i2c_interface/i2c_addr\"")
    execute("adb shell \"echo 2 > /sys/class/light_ccb/i2c_interface/i2c_br\"")
    execute("adb shell \"cat /sys/class/light_ccb/i2c_interface/i2c_br\" > temp_value.txt")
    f = open('temp_value.txt', 'r')
    line = f.readline()
    temp_value = line[3:-1]+line[:3]
    temp_value = int(temp_value,16)
    return temp_value

def camera(arg):
    m_bitmask_int = 0
    ostring = ""
    byte_count = 5
    ostring += " 0x02"
    byte_count += 1
    open_string = "adb shell \"echo " + str(byte_count) + " 0x0000 0x00 0x80 " + m_bitmask + ostring +\
     " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    ucid_string = "adb shell \"echo 4 0x0000 0x00 0x90 0x03 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
    execute(open_string)
    execute(ucid_string)

def end(cam,bitmask_t,pos):
    fstring = ""
    byte_count = 7
    fstring += convert_to_hex(pos)
    fstring += " 0x00 0x00"
    byte_count += 4
    fstring += " "
    end_string = "adb shell \"echo " + str(byte_count) + " " + change_trans_ID(trans_ID) + " 0x48 0x00 " + str(bitmask_t) + " 0x03 0x00 " + fstring + \
    " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    start_timer = default_timer()
    execute(end_string)
    command_status(trans_ID)
    len_value =  get_len_value(bitmask_t) 
    duration = default_timer() - start_timer
    camera_temp = read_temp(bitmask_t)
    print "Camera: " + cam + " focus distance: " + pos + " hal value: " + len_value \
    + " execution time: " + str(duration) + "(s)" + " camera temperature " + str(camera_temp)    

### Parser #############################################
parser = argparse.ArgumentParser()

parser.add_argument("-cycle", "--cycle", help="start value", type=int,
                    action="store")
args = parser.parse_args()
########################################################

camras_ID = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "c6"]
a_distance_arrays = ["100","200","1000","300","500","900","700","1500","1100","400"]
b_distance_arrays = ["400","500","1500","700","900","600","1900","1700","2000","2500"]
c_distance_arrays = ["1000","1500","3000","1700","1900","3500","2100","2600","2500","2900"]
for i in range(1,args.cycle +1):
    print "############################################"
    print "Cycle " + str(i)
    for j in range(0,len(a_distance_arrays)):
        print "---"
        print "Move cameras group A to focus distance " + a_distance_arrays[j] +" (mm)"
        print "Move cameras group B to focus distance " + b_distance_arrays[j] +" (mm)"
        print "Move cameras group C to focus distance " + c_distance_arrays[j] +" (mm)"
        for cam in camras_ID:
            if cam[0:1] == "a":
                d = a_distance_arrays[j]
            elif cam[0:1] == "b":
                d = b_distance_arrays[j]
            else:
                d = c_distance_arrays[j]
            m_bitmask_int = module_one_hot(cam)
            m_bitmask_str = hex(m_bitmask_int)
            m_bitmask = handle_endianness(m_bitmask_str)
            camera(m_bitmask)
            end(cam,m_bitmask,d)
