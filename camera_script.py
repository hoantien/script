#*******************************************************************************
#                            REVISION HISTORY
#*******************************************************************************
# * 1.0.0	25-Feb-2016	Baseline 20160225_Release
# * 1.0.1	11-Mar-2016	Add -csi for streaming command
#   Syntax:  python camera_script.py -c [a1..c6]+ -s [on|off] -csi [0|1]+
#   Example: python camera_script.py -c a1 a2 -s on -csi 0 1
# * 1.0.2	25-Mar-2016	Support transaction Id and little endian
#*******************************************************************************

import argparse
import string
import subprocess
import sys
import time
import datetime

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
\t\t                  $ $$                      \n\
\t\t                $$   $$                     \n\
\t\t                $$   $$                     \n\
\t\t                  $$$                       \n\
\n\
\t\t-------------------------------------------\n\
\t\t-------------------V1.0.3------------------\n\
\t\t-----------------2016.03.25----------------\n"

atypecam = [ 'a1', 'a2', 'a3', 'a4', 'a5' ]

camera_group = [ 'AB', 'ab', 'BC', 'bc' ]

def execute(cmd):
    #print(cmd);
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()[0]

def split_bytes(arg):
    # assume the user always inputs 4 digits (i.e the leading nibbles
    # in each byte are nonzero, so we get 4 digits)
    int_input = len(arg)
    print int_input
    if (arg[:2] == '0x'):
        if (int_input < 6):
        	fstring = '0x' + arg[-2:] + ' 0x0' + arg[2:3]
        else:
    	    fstring = '0x' + arg[-2:] + ' ' +  arg[0:4]
        return fstring
    else:
       print "Not support this value"

def one_byte_hex(arg):
    # assume that the input is a string from 0 to 255.
    # the output will be one byte in hex.
    int_input = int(arg)
    if (int_input < 16):
        return '0x0' + hex(int_input)[2:]
    else:
        return '0x' + hex(int_input)[2:]

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

def convert_to_hex_8_bytes(arg):
    # outputs eight bytes in hex, delimited by '0x's
    fstring = arg
    rs = 0
    int_rs = 0;
    if arg.find("0x") != -1:
        print "Unsupported hexa number"
    else:
        int_rs =  int(arg)
	if (int_rs > 1500000000):
	    int_rs = 1500000000
        rs = hex(int_rs)

    if (int_rs <= 0xf): # one nibble
        fstring = '0x0' + rs[-1:] + ' 0x00 0x00 0x00 0x00 0x00 0x00 0x00'
    elif (int_rs <= 0xff): # two nibbles
        fstring = rs + ' 0x00 0x00 0x00 0x00 0x00 0x00 0x00'
    elif (int_rs <= 0xfff): # three nibbles
        fstring = '0x' + rs[-2:] + ' 0x0' + rs[-3:-2] + ' 0x00 0x00 0x00 0x00 0x00 0x00' 
    elif (int_rs <= 0xffff): # four nibbles
        fstring = '0x' + rs[-2:] + ' 0x'+ rs[-4:-2] + ' 0x00 0x00 0x00 0x00 0x00 0x00'
    elif (int_rs <= 0xfffff): # five nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x0'+ rs[-5:-4] + ' 0x00 0x00 0x00 0x00 0x00'
    elif (int_rs <= 0xffffff): # six nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x00 0x00 0x00 0x00 0x00' 
    elif (int_rs <= 0xfffffff): # seven nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x0' + rs[-7:-6] + ' 0x00 0x00 0x00 0x00'
    elif (int_rs <= 0xffffffff): # eight nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] + ' 0x00 0x00 0x00 0x00'
    elif (int_rs <= 0xfffffffff): # nine nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] +' 0x0' + rs[-9:-8] + ' 0x00 0x00 0x00'
    elif (int_rs <= 0xffffffffff): # ten nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] + ' 0x' + rs[-10:-8] + ' 0x00 0x00 0x00'
    elif (int_rs <= 0xfffffffffff): # eleven nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] + ' 0x' + rs[-10:-8] + ' 0x0' + rs[-11:-10] + ' 0x00 0x00'
    elif (int_rs <= 0xffffffffffff): # twelve nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] + ' 0x' + rs[-10:-8] + ' 0x' + rs[-12:-10] + ' 0x00 0x00'
    elif (int_rs <= 0xfffffffffffff): # thirteen nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] + ' 0x' + rs[-10:-8] + ' 0x' + rs[-12:-10] + ' 0x0' + rs[-13:-12] + ' 0x00'
    elif (int_rs <= 0xffffffffffffff): # fourteen nibbles
        fstring = '0x' + rs[-2:] + ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] + ' 0x' + rs[-10:-8] + ' 0x' + rs[-12:-10] + ' 0x' + rs[-14:-12] + '0x00'
    elif (int_rs <= 0xfffffffffffffff): # fifteen nibbles
        fstring = '0x' + rs[-2:]+ ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] + ' 0x' + rs[-10:-8] + ' 0x' + rs[-12:-10] + ' 0x' + rs[-14:-12] + ' 0x0' + rs[-15:-14]
    else: # sixteen nibbles
        fstring = '0x' + rs[-2:]+ ' 0x' + rs[-4:-2] + ' 0x'+ rs[-6:-4] + ' 0x' + rs[-8:-6] + ' 0x' + rs[-10:-8] + ' 0x' + rs[-12:-10] + ' 0x' + rs[-14:-12] + ' 0x' + rs[-16:-14]
    return fstring


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

def dutycycle_lookup(x):
    return {
        'light' : "0x00 0x80", # 12.8%
        'Light' : "0x00 0x80",
        'medium': "0x00 0xC8", # 20%
        'Medium': "0x00 0xC8",
        'heavy' : "0x01 0x18", # 28%
        'Heavy' : "0x01 0x18"
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
        output_string = "0x00 " + hex_string[:2] + "0" + hex_string[2:]
    elif len(hex_string) == 4:
        # prepend an 0x00
        output_string = "0x00 " + hex_string
    elif len(hex_string) == 5:
        # prepend an 0x0, take the third character of the input, and append 0xXX
        # hacky...but it works
        output_string = "0x0" + hex_string[2] + " 0x" + hex_string[-2:]
    else:
        print "hex_string = " + hex_string
        print "Should never get here. Check your duty cycle input."
        exit()
    return output_string

def list_little_endian(number):
    # takes an input and splits it into a list of bytes, LSB to MSB
    output = []
    number = int(number) # sanitize input
    #print "number = " + str(number)

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

    #print "output = "
    #print output
    return output

def convert_pwm2(percentage, period):
    # frequency = 128 kHz
    # one period = 7.8125 us
    # period is now CONFIGURABLE, given in microseconds
    # multiply number of pulses by period in microseconds to get
    # number of microseconds
    # convert to hex afterwards
    float_percentage = float(percentage)
    #print "percentage = " + str(float_percentage)
    div_100 = float_percentage/100
    # high_time = div_100 * 7.8125
    high_time = div_100 * period
    #print "high_time = " + str(high_time)
    scale_nanosec = (high_time * 1000) / 20
    #print "scale_nanosec = " + str(scale_nanosec)
    hex_output = hex(int(round(scale_nanosec)))
    hex_output = hex_output[2:]
    #print "hex_output = " + hex_output
    #print "\n"

    # we need to write one byte at a time to the CPLD, LSB to MSB
    # therefore, simply take the integer value of each byte
    # and append to a list for easier indexing later
    output = []
    scale_nanosec_int = int(round(scale_nanosec))
    while (scale_nanosec_int > 0):
        LSB = scale_nanosec_int & 255;
        output.append(LSB)
        scale_nanosec_int = scale_nanosec_int >> 8;

    # need to pad for 4 bytes
    while (len(output) < 4):
        output.append(0)

    #print "output = "
    #print output
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
        output_string = '0x0' + input_string + ' 0x00'
    elif len(input_string) == 2: # two nibbles
        output_string = '0x' + input_string[0] + input_string[1]  + ' 0x00'
    elif len(input_string) == 3: # three nibbles
        output_string = '0x' + input_string[1] + input_string[2]  + ' 0x0' + input_string[0]
    elif len(input_string) == 4: # four nibbles
        output_string = '0x' + input_string[2] + input_string[3] + ' 0x' + input_string[0] + input_string[1]
    return output_string;

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

def module_channelid(x):
    return {
        'a1': "0x01",
        'a2': "0x02",
        'a3': "0x03",
        'a4': "0x04",
        'a5': "0x05",
        'b1': "0x06",
        'b2': "0x07",
        'b3': "0x08",
        'b4': "0x09",
        'b5': "0x0a",
        'c1': "0x0b",
        'c2': "0x0c",
        'c3': "0x0d",
        'c4': "0x0e",
        'c5': "0x0f",
        'c6': "0x10"
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

def cpld_bitmask(x):
    # the CPLD has a separate bitmask, for two different registers:
    # 0x02: {3'b000, CamLensGrpB[4:0]}; {B1, B2, B3, B5, B4}
    # 0x03: {2'b00,  CamLensGrpC[5:0]}; {C5, C6, C3, C4, C2, C1}
    return {
        'b1': 16,
        'b2': 8,
        'b3': 4,
        'b4': 1,
        'b5': 2,

        'c1': 1,
        'c2': 2,
        'c3': 8,
        'c4': 4,
        'c5': 32,
        'c6': 16,
    }[x]

def ucid_to_hex(x):
    return {
        'preview' : "0x03 0x00",
        'hires'   : "0x05 0x00",
        'focal'   : "0x06 0x00",
        'hdr'     : "0x07 0x00",
        'video'   : "0x04 0x00"
    }[x]

# turn on manual mode
execute('adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"')

parser = argparse.ArgumentParser()
parser.add_argument("-v, --verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-c", "--camera", nargs='+',
                    help="select camera: from a1->a5, b1->b5 \                                            or c1->c6",
                    action="store")
parser.add_argument("-s", "--stream", help="stream on or off",
                    action="store", choices=['on', 'off', 'sync'])
parser.add_argument("-u", "--ucid", help="ucid for setting",
                    action="store", choices=['preview', 'hires', 'focal', 'video', 'hdr'])
parser.add_argument("-f", "--focus", help="select focus distance for 35mm cameras",\
                    action="store")
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
parser.add_argument("-e", "--exposure", help="select exposure value",
                    action="store")
parser.add_argument("-g", "--gain", help="select gain value",
                    action="store")
parser.add_argument("-cal", "--calibrate", help="calibrate 70mm and 150mm lenses",
                    action="store_true")
parser.add_argument("-i", "--iterations", help="select number of iterations",
                    action="store")
parser.add_argument("-ptc_ms", "--pwm_test_cpld_mode_switch", help="Configure the CPLD behavior for standard or new PWM control",
                    action="store")
parser.add_argument("-ptc_c", "--pwm_test_cpld_config", help="Write the configuration settings for the CPLD in PWM testing mode",
                    action="store", nargs=17)
parser.add_argument("-ptc_s", "--pwm_test_cpld_start", help="Start the CPLD's PWM test",
                    action="store_true")
parser.add_argument("-ptc_e", "--pwm_test_cpld_end", help="End the CPLD's PWM test",
                    action="store_true")
parser.add_argument("-csc", "--cpld_stm_config", help="Configure the CPLD through the STM firmware",
                    action="store", nargs=16)
parser.add_argument("-css", "--cpld_stm_start", help="Start PWM generation through STM firmware",
                    action="store_true")
parser.add_argument("-rhsv", "--read_hall_sensor_value", help="Read the hall sensor for a given 70mm or 150mm camera",
                    action="store_true")
parser.add_argument("-ghsv", "--go_to_hall_sensor_value", nargs='+', help="Command a given 70mm or 150mm camera to move to a given hall sensor position",
                    action="store")
parser.add_argument("-fn", "--fine_nudge", help="Nudge in fine increments",
                    action="store_true")
parser.add_argument("-mul", "--multiplier", help="Multiplier for the fine nudge command",
                    action="store")
parser.add_argument("-csi", "--csi_interface", nargs='+', help="CSI interface",
                    action="store", choices=['0', '1'])
parser.add_argument("-tol", "--tolerance", help="tolerance value",
                    action="store")

args = parser.parse_args()

if args.camera:
    # OR the one-hot encoded cameras together into one bitmask
    print "Camera(s) are " + str(args.camera)
    m_bitmask_int = 0
    for camera in args.camera:
        m_bitmask_int |= module_one_hot(camera)
    m_bitmask_str = hex(m_bitmask_int)
    #print "m_bitmask_str = " + m_bitmask_str
    m_bitmask = handle_endianness(m_bitmask_str)
    print "m_bitmask = " + m_bitmask
    camera_string = ""
    stream_string = ""
    if args.stream:
        idx = 0
        byte_count = 5
        for camera in args.camera:
            if (len(args.camera) == len(args.csi_interface)):
                if (args.csi_interface[idx] == "0"):
                    stream_string += "0x1"
                else:
                    stream_string += "0x2"
                if (args.stream == 'on'):
                    stream_string += "1 "
                else:
                    stream_string += "0 "
                stream_string += "0x00 0x00 "
            else:                
                if (args.stream == 'on'):
                    stream_string += "0x11 "
                else:
                    stream_string += "0x10 "
                stream_string += " 0x00 0x00 "
            idx += 1
            byte_count += 3
        camera_string = "adb shell \"echo " + str(byte_count) + " 0x0000 0x02 0x00 " + m_bitmask \
                        + " " + stream_string + "> /sys/class/light_ccb/i2c_interface/i2c_w\""
        print camera_string
        execute(camera_string)
else:
    if not args.pwm_test_cpld_mode_switch and \
       not args.pwm_test_cpld_config and \
       not args.pwm_test_cpld_start and \
       not args.pwm_test_cpld_end and \
       not args.cpld_stm_config and \
       not args.ucid:
        parser.print_help()

if args.ucid:
    if not args.camera:
        # Light active ucid
        str = "adb shell 'echo 4 0x0000 0x00 0x10 " + ucid_to_hex(args.ucid) + " > /sys/class/light_ccb/i2c_interface/i2c_w'"
        print "Sending LIGHT_ACTIVE_UCID %s \n" % (args.ucid)
        print str
        execute(str)
        exit()

if args.focus:

    fstring = ""
    byte_count = 5
    # check if we have non-35mm camera
    for camera in args.camera:
        # add the argument n number of times for n cameras
        fstring += convert_to_hex(args.focus)
        fstring += " 0x00 0x00"
        byte_count += 4
        fstring += " "

    print "Focus is " + args.focus
    if args.ucid:
        ucid = ucid_to_hex(args.ucid)
        focus_string = "adb shell \"echo " + str(byte_count + 2) + " 0x0000 0x48 0x00 " + m_bitmask + " " + ucid + " " + fstring + \
        " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    else:
        focus_string = "adb shell \"echo " + str(byte_count) + " 0x0000 0x48 0x00 " + m_bitmask + " " + fstring + \
        " > /sys/class/light_ccb/i2c_interface/i2c_w\""

    print focus_string
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
        #                                      > /sys/class/light_ccb/i2c_interface/i2c_w"
        if args.direction and args.dutycycle and args.duration:
            direction_string = one_byte_hex(args.direction)
            dutycycle_string = convert_dutycycle(args.dutycycle)
            duration_string = one_byte_hex(args.duration)
            lens_string = "adb shell \"echo 9 0x0000 0x51 0x00 " + m_bitmask + " "\
                           + direction_string + " " + dutycycle_string + \
                           " " + duration_string + \
                           " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    print "Lens:"
    print lens_string
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
        #                            > /sys/class/light_ccb/i2c_interface/i2c_w"
        if args.direction and args.dutycycle and args.duration:
            direction_string = one_byte_hex(args.direction)
            dutycycle_string = convert_dutycycle(args.dutycycle)
            duration_string = one_byte_hex(args.duration)
            mirror_string = "adb shell \"echo 9 0x0000 0x47 0x00 " + m_bitmask + " "\
                           + direction_string + " " + dutycycle_string + \
                           " " + duration_string + \
                           " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    print mirror_string
    execute(mirror_string)
    print ""

if args.exposure:
    if args.camera:
        fstring = ""
        byte_count = 5
        for camera in args.camera:
            # add the argument n number of times for n cameras
            fstring += convert_to_hex_8_bytes(args.exposure)
            fstring += " "
            byte_count += 8

        #fstring = args.exposure
        print "Exposure is " + args.exposure
        if args.ucid:
            ucid = ucid_to_hex(args.ucid)
            exposure_string = "adb shell \"echo " + str(byte_count + 2) + " 0x0000 0x32 0x00 " + m_bitmask + " " + \
            ucid + " " + fstring + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        else:
            exposure_string = "adb shell \"echo " + str(byte_count) + " 0x0000 0x32 0x00 " + m_bitmask + " " + \
            fstring + " > /sys/class/light_ccb/i2c_interface/i2c_w\""

        print exposure_string
        execute(exposure_string)
        print ""
    else:
        print "Please provide a camera argument."

if args.gain:
    if args.camera:
        fstring = ""
        byte_count = 5
        for camera in args.camera:
            # add the argument n number of times for n cameras
            fstring += split_bytes(args.gain)
            fstring += " 0x00 0x00 "
            byte_count += 4

        print "Gain is " + args.gain
        if args.ucid:
            ucid = ucid_to_hex(args.ucid)
            gain_string = "adb shell \"echo " + str(byte_count + 2) + " 0x0000 0x30 0x00 " + m_bitmask + " " + ucid + " "\
            + fstring + \
            " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        else:
            gain_string = "adb shell \"echo " + str(byte_count) + " 0x0000 0x30 0x00 " + m_bitmask + " "\
            + fstring + \
            " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        print gain_string
        execute(gain_string)
        print ""
    else:
        print "Please provide a camera argument."

if args.calibrate:
    if (args.camera in atypecam):
        print "Cannot calibrate 35mm cameras. Choose a 70mm camera."
        exit()
    else:
        #if args.dutycycle and args.iterations:
        #    dutycycle = convert_dutycycle(args.dutycycle)
        #    iterations = one_byte_hex(args.iterations)
        #    calibrate_string = "adb shell 'echo 6 0x0061" + " " + m_bitmask + \
        #                       " " + iterations + " " + dutycycle + " " +\
        #                       "> /sys/class/light_ccb/i2c_interface/i2c_w'"
        #    print calibrate_string
        #    execute(calibrate_string)
        #else:
        #    print "Need a duty cycle and number of iterations for calibration"
        if args.camera:
            for camera in args.camera:
                m_bitmask_int |= module_one_hot(camera)
            m_bitmask_str = hex(m_bitmask_int)
            m_bitmask = handle_endianness(m_bitmask_str)
            print "m_bitmask = " + m_bitmask
            camera_string = "adb shell \"echo 6 0x0000 0x60 0x00 " + m_bitmask \
            + " 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
            print camera_string
            execute(camera_string)
        else:
            print "Need a camera argument. Please supply a 70mm or 150mm camera argument."

if args.pwm_test_cpld_mode_switch:
    cpld_mode = args.pwm_test_cpld_mode_switch
    cpld_mode_string = one_byte_hex(cpld_mode)
    debug_test_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x06 " + cpld_mode_string + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    #b_module_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x02 0xFF > /sys/class/light_ccb/i2c_interface/i2c_w\""
    #c_module_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x03 0xFF > /sys/class/light_ccb/i2c_interface/i2c_w\""
    print debug_test_string
    #print b_module_string
    #print c_module_string
    execute(debug_test_string)
    #execute(b_module_string)
    #execute(c_module_string)

if args.pwm_test_cpld_config:

    # Argument order:
    #    0 - module name (one module only)
    #    1 - frequency in kHz
    #    2 to 7 - duty cycles
    #    8 to 15 - repetitions

    # program 0x02 and 0x03 - the module selection registers
    # currently can only program the test for one module at a time
#    module = args.pwm_test_cpld_config[0]
#    print "Configuring for module: " + module
#    module_int = cpld_bitmask(module)
#    if module[0] == 'b':
#        b_module_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x02 " + one_byte_hex(module_int) + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
#        c_module_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x03 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
#    elif module[0] == 'c':
#        b_module_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x02 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
#        c_module_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x03 " + one_byte_hex(module_int) + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
#    else:
#        print "Invalid input for module. Input B1-B5 or C1-C6. "
#        exit()

    # turn on ALL modules for now
    b_module_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x02 0x1F > /sys/class/light_ccb/i2c_interface/i2c_w\""
    c_module_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x03 0x3F > /sys/class/light_ccb/i2c_interface/i2c_w\""

    execute(b_module_string)
    execute(c_module_string)

    # configure the frequency of the input PWM signal
    frequency = args.pwm_test_cpld_config[1]
    print "frequency = " + str(frequency) + " kHz"
    period = (1/(float(frequency) / 1000000)) / 1000
    print "period = " + str(period) + " us"

    frequency_reg_value = (period * 1000) / 20
    frequency_reg_value = int(round(frequency_reg_value))
    #print "frequency_reg_value = " + str(frequency_reg_value)
    frequency_list = list_little_endian(frequency_reg_value)
    #print frequency_list

    dutycycle_lists = []
    num_pulses_list = []

    # convert_pwm2 returns a list of bytes, LSB to MSB
    # need to write each byte one at a time to the CPLD
    # dutycycle_lists and num_pulses_list are both 2D lists to handle
    # the byte-by-byte writes to the CPLD
    for i in xrange(2, 8):
        dutycycle_lists.append(convert_pwm2(args.pwm_test_cpld_config[i], period))

    for i in xrange(8, 17):
        num_pulses_list.append(list_little_endian(args.pwm_test_cpld_config[i]))

    # program the frequency configuration registers
    for i in xrange(0, 2):
        offset_value = 128 + i # 128 = 0x80
        offset = one_byte_hex(offset_value)
        freq_value = one_byte_hex(str(frequency_list[i]))
        output_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 " + offset + " " + freq_value + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        print output_string
        execute(output_string)

    # program the frequency configuration registers
#    offset_value = 128 # 128 = 0x80
#    offset = one_byte_hex(offset_value)
#
#    str_freq_list = map(one_byte_hex, map(str, frequency_list))
#    freq_str = reduce(lambda x, y : x + " " + y, str_freq_list)
#    output_string = "adb shell \"echo 8 0x0000 0x91 0x00 0x05 0x02 " + offset + " " + freq_str + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
#    print output_string
#    execute(output_string)

    # adb shell "echo 5 0x0000 0x90 0x00 0x02 0x0a 0x00"
    # program the high time for each pulse
    # print "len(dutycycle_lists) = " + str(len(dutycycle_lists))

    print "dutycycle_lists" + str(dutycycle_lists)
    for i in xrange(0, len(dutycycle_lists)):
        #print " "
        #print "i = " + str(i)
        dc_list = dutycycle_lists[i]
        for j in xrange(0, 2): # two byte duty cycles
            # duty cycles are in addresses 0x0a to 0x15, two bytes each
            offset_value = 10 + i * 2 + j
            offset = one_byte_hex(str(offset_value))
            if (offset_value > 21): # 0x15
                print "Invalid address for duty cycle!"
                exit()

            output_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 " + offset + " " + one_byte_hex(str(dc_list[j])) + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
            print output_string
            execute(output_string)

#    offset_value = 10 # 10 = 0x0a
#    offset = one_byte_hex(offset_value)
#    collection = ""
#    for l in dutycycle_lists:
#        temp = map(one_byte_hex, l)
#        temp = reduce(lambda x, y: x + " " + y, temp)
#        collection += temp + " "
#    #print collection
#
#    output_string = "adb shell \"echo 29 0x0000 0x91 0x00 0x18 0x02 " + offset + " " + collection + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
#    print output_string
#    execute(output_string)

    # program the number of pulses for each pair
    # print "len(num_pulses_list) = " + str(len(num_pulses_list))
#    print "num_pulses_list" + str(num_pulses_list)
#    single_pair_string = ""
#    double_pair_string = ""
#    overall_string = ""
#    pulse_list = []
#    for l in num_pulses_list:
#        temp = map(one_byte_hex, l)
#        temp = reduce(lambda x, y: x + " " + y, temp)
#        pulse_list.append(temp)
#
#    for i in xrange(0, len(pulse_list)):
#        if i <= 5:
#            single_pair_string += pulse_list[i] + " "
#        elif i <= 7:
#            double_pair_string += pulse_list[i] + " "
#        else:
#            overall_string += pulse_list[i] + " "
#
#    output_string = "adb shell \"echo 29 0x0000 0x91 0x00 0x18 0x02 " + "0x20" + " " + single_pair_string + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
#    print output_string
#    execute(output_string)
#    output_string = "adb shell \"echo 13 0x0000 0x91 0x00 0x08 0x02 " + "0x50" + " " + double_pair_string + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
#    print output_string
#    execute(output_string)
#    output_string = "adb shell \"echo 9 0x0000 0x91 0x00 0x04 0x02 " + "0x70" + " " + overall_string + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
#    print output_string
#    execute(output_string)
    for i in xrange(0, len(num_pulses_list)):
        #print " "
        #print "i = " + str(i)
        pulse_list = num_pulses_list[i]
        for j in xrange(0, 4): # four byte pulse counts
            # pulse counts are stored in addresses 0x20 to 0x37, four bytes each
            if i <= 5:
                start_address = 32 # 0x20
            elif i <= 7:
                start_address = 56 # 0x38 = 0x20 + (0x50 - 0x37) - 1
                #start_address =  # 0x38 = 0x20 + (0x50 - 0x37) - 1
            else:
                start_address = 80 # 0x50 = 0x20 + (0x50 - 0x37) + (0x70 - 0x57) - 2
                #start_address =  # 0x50 = 0x20 + (0x50 - 0x37) + (0x70 - 0x57) - 2

            offset_value = start_address + i * 4 + j
            offset = one_byte_hex(str(offset_value))
            if (offset_value > 115): # 0x73
                print "Invalid address for pulse count!"
                exit()

            output_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 " + offset + " " + one_byte_hex(str(pulse_list[j])) + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
            print output_string
            execute(output_string)

if args.pwm_test_cpld_start:
    # send the start signal
    start_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x07 0x01 > /sys/class/light_ccb/i2c_interface/i2c_w\""
    print start_string
    execute(start_string)

if args.pwm_test_cpld_end:
    stop_string  = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 0x08 0x01 > /sys/class/light_ccb/i2c_interface/i2c_w\""
    print stop_string
    execute(stop_string)

if args.cpld_stm_config:

    # Argument order:
    #    0 - frequency in kHz
    #    1 to 6 - duty cycles
    #    7 to 14 - repetitions

    # configure the frequency of the input PWM signal
    frequency = args.cpld_stm_config[0]
    print "frequency = " + str(frequency) + " kHz"
    period = (1/(float(frequency) / 1000000)) / 1000
    print "period = " + str(period) + " us"

    frequency_reg_value = (period * 1000) / 20
    frequency_reg_value = int(round(frequency_reg_value))
    print "frequency_reg_value = " + str(frequency_reg_value)
    frequency_list = list_little_endian(frequency_reg_value)
    print frequency_list

    dutycycle_lists = []
    num_pulses_list = []

    output_string = "adb shell \"echo 52 0x0000 0x92 0x00"
    byte_count = 0

    # convert_pwm2 returns a list of bytes, LSB to MSB
    # need to write each byte one at a time to the CPLD
    # dutycycle_lists and num_pulses_list are both 2D lists to handle
    # the byte-by-byte writes to the CPLD
    for i in xrange(1, 7):
        dutycycle_lists.append(convert_pwm2(args.cpld_stm_config[i], period))

    for i in xrange(7, 16):
        num_pulses_list.append(list_little_endian(args.cpld_stm_config[i]))

    # adb shell "echo 5 0x0000 0x90 0x00 0x02 0x0a 0x00"
    # program the high time for each pulse
    # print "len(dutycycle_lists) = " + str(len(dutycycle_lists))
    for i in xrange(0, len(dutycycle_lists)):
        #print " "
        #print "i = " + str(i)
        dc_list = dutycycle_lists[i]
        for j in xrange(0, 2): # two byte duty cycles
            # duty cycles are in addresses 0x0a to 0x15, two bytes each
            #offset_value = 10 + i * 2 + j
            #offset = one_byte_hex(str(offset_value))
            #if (offset_value > 21): # 0x15
            #    print "Invalid address for duty cycle!"
            #    exit()
            dutycycle_value = one_byte_hex(str(dc_list[j]))
            output_string += dutycycle_value + " "
            byte_count += 1
            #output_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 " + offset + " " + dutycycle_value + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
            #print output_string
            #execute(output_string)

    # program the number of pulses for each pair
    # print "len(num_pulses_list) = " + str(len(num_pulses_list))
    for i in xrange(0, len(num_pulses_list)):
        #print " "
        #print "i = " + str(i)
        pulse_list = num_pulses_list[i]
        for j in xrange(0, 4): # four byte pulse counts
            # pulse counts are stored in addresses 0x20 to 0x37, four bytes each
            #if i <= 5:
            #    start_address = 32 # 0x20
            #elif i <= 7:
            #    start_address = 56 # 0x38 = 0x20 + (0x50 - 0x37) - 1
            #else:
            #    start_address = 80 # 0x50 = 0x20 + (0x50 - 0x37) + (0x70 - 0x57) - 2

            #offset_value = start_address + i * 4 + j
            #offset = one_byte_hex(str(offset_value))
            #if (offset_value > 115): # 0x73
            #    print "Invalid address for pulse count!"
            #    exit()
            pulse_value = one_byte_hex(str(pulse_list[j]))
            output_string += pulse_value + " "
            byte_count += 1

            #output_string = "adb shell \"echo 5 0x0000 0x90 0x00 0x02 " + offset + " " + pulse_value + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
            #print output_string
            #execute(output_string)

    # program the frequency configuration registers
    for i in xrange(0, 2):
        offset_value = 128 + i # 128 = 0x80
        offset = one_byte_hex(offset_value)
        freq_value = one_byte_hex(str(frequency_list[i]))
        output_string += freq_value + " "
        byte_count += 1
        #output_string = "adb shell \"echo 3 0x0090 0x02 " + offset + " " + freq_value + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        #print output_string
        #execute(output_string)

    output_string += "> /sys/class/light_ccb/i2c_interface/i2c_w\""
    print output_string
    execute(output_string)
    print "byte_count = " + str(byte_count)


if args.cpld_stm_start:
    if not args.camera:
        print "You must select a camera to start the PWM signal."
        exit()

    output_string = 'adb shell \"echo 7 0x0000 0x93 0x00 ' +\
                    m_bitmask + ' 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\"'
    print output_string
    execute(output_string)

if args.read_hall_sensor_value:
    if not args.camera:
        print "You must provide a camera to read a hall sensor."
        exit()

    if args.lens:
        print "Reading lens hall sensor..."
        output_string = 'adb shell \"echo 5 0x0000 0x40 0x00 ' +\
                        m_bitmask + ' > /sys/class/light_ccb/i2c_interface/i2c_w\"'
        print output_string
        execute(output_string)

    if args.mirror:
        print "Reading mirror hall sensor..."
        output_string = "adb shell \"echo 5 0x0000 0x44 0x00 " + m_bitmask + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        print output_string
        execute(output_string)

if args.go_to_hall_sensor_value:
    if not args.camera:
        print "You must provide a camera to command to move."
        exit()

    if args.lens:
        destination_string = ""
        if args.tolerance:
            if int(args.tolerance) > 15:
                print "Tolerance value need to be smaller than 16"
                exit()
            else:
                destination_string = one_byte_hex(args.tolerance)
        else:
            print "Need input tolerance value"
            exit()
        if len(args.camera) != len(args.go_to_hall_sensor_value):
            print "Not enough arguments. For each camera selected, provide a destination."
            exit()
        for i in xrange( 0, len(args.camera)):
            destination_string = destination_string + " " + two_byte_little_endian(args.go_to_hall_sensor_value[i])
            print "Moving lens "  + str(args.camera[i]) + " to "  + args.go_to_hall_sensor_value[i] + " ..."
        args_len =  6 + (len(args.camera) * 2)
        output_string = "adb shell \"echo " + str(args_len)  +" 0x0000 0x40 0x00 " + m_bitmask + " " + \
        destination_string + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        print output_string
        execute(output_string)

    if args.mirror:
        print "args.go_to_hall_sensor_value: " + args.go_to_hall_sensor_value[0]
        destination_string = two_byte_little_endian(args.go_to_hall_sensor_value[0])
        print "Destination is " + args.go_to_hall_sensor_value[0]

        print "Moving mirror "  + str(args.camera[0]) + " to "  + args.go_to_hall_sensor_value[0] + " ..."
        output_string = "adb shell \"echo 7 0x0000 0x44 0x00 " + m_bitmask + " " + \
        destination_string + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
        print output_string
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
            output_string = "adb shell \"echo 8 0x0000 0x51 0x00 " + m_bitmask + " " + \
            one_byte_hex(direction) + " " + two_byte_little_endian(hex(int(multiplier))) + \
            " " + "> /sys/class/light_ccb/i2c_interface/i2c_w\""
        if args.mirror:
            output_string = "adb shell \"echo 8 0x0000 0x52 0x00 " + m_bitmask + " " + \
            one_byte_hex(direction) + " " + two_byte_little_endian(hex(int(multiplier))) + \
            " " + "> /sys/class/light_ccb/i2c_interface/i2c_w\""

        print output_string
        execute(output_string)

    else:
        print "Please provide a camera argument. "
        exit()

