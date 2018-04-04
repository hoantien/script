import argparse
import string
import subprocess
import sys

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
\t\t-------------------------------------------\n"

atypecam = [ 'a1', 'a2', 'a3', 'a4', 'a5' ]
camera_simple_mask = ['g', 'a1', 'a2', 'a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6']

def execute(cmd,display=1):
    if display:
        print cmd
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=True)
    return proc.communicate()[0]
    pass

def execute_eep(cmd,display=1):
    if display:
        print cmd
    proc = subprocess.Popen(cmd,  stdout=subprocess.PIPE, shell=True)
    data = proc.communicate()[0]
    return data

def convert_to_hex(arg):
    fstring = arg
    rs = 0
    if arg.find("0x") != -1:
        rs = arg
    else:
        rs =  hex(int(arg))
    #print rs
    tmp = str(rs)
    if len(tmp) > 4:
        if len(fstring) == 6 :
            fstring = tmp[0:4]
            fstring = fstring + " 0x" + tmp[4:]
        else:
            fstring = "0x0" + tmp[2:3] + " 0x" + tmp[3:]
    else:
        fstring = "0x00 " + str(rs)
    print "Output: " + fstring
    return fstring

def convert_to_hex_3bytes_nrev(arg): # Convert to hex 3 bytes and revert
    fstring = arg
    rs = 0
    if arg.find("0x") != -1:
        rs = arg
    else:
        rs =  hex(int(arg))
    tmp = str(rs)
    if len(tmp) <= 6:
        c = convert_to_hex(tmp)
        fstring = c[5:] + " "
        fstring = fstring + c[0:4] + " "
        fstring = fstring + "0x00"
    else:
        s = "0x" + tmp[len(tmp)-4:]
        c = convert_to_hex(s)
        fstring = c[5:] + " "
        fstring = fstring + c[0:4] + " "
        fstring = fstring + tmp[0:len(tmp)-4]
    return fstring

def calculate_bitmask(cam):
    print "Not support"
    exit()

def require_camera(cam):
    if cam:
        if cam in camera_simple_mask:
            return module_bitmask(cam)
        else:
            return calculate_bitmask(cam)
    else:
        print "This feature require a specific camera."
        print "Use option: -c <camera> to indicate the camera"
        #parser.print_help()
        exit()

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
    }[x]

def command_map(x):
    return {
        'resolution'        : "00 2C",
        'vcmposition'       : "00 3C",
        'lenscalibration'   : "00 60",
        'mirrorcalibration' : "00 62",
        'streaming'         : "00 02",
        'opening'           : "00 00",
        'focusdistance'     : "00 48",
        'lenposition'       : "00 40",
        'mirrorposition'    : "00 44",
        'exposure'          : "00 32",
        'sensitivity'       : "00 30"
    }[x]

parser = argparse.ArgumentParser()
parser.add_argument("-v, --verbose", help="increase output verbosity",
                    action="store")
parser.add_argument("-c", "--camera", help="select camera: from a1->a5, b1->b5 or c1->c6",
                    action="store")
parser.add_argument("-f", "--focus", help="select focus distance",
                    action="store")
parser.add_argument("-dac", "--vcmposition", help="select vcm focus DAC code",
                    action="store")
parser.add_argument("-m", "--mirror", help="select mirror angle",
                    action="store")
parser.add_argument("-e", "--exposure", help="select exposure value",
                    action="store")
parser.add_argument("-s", "--stream", help="stream on/off a camera",
                    action="store", choices=['on', 'off'])
parser.add_argument("-g", "--gain", help="select gain value",
                    action="store")
parser.add_argument("-r", "--reset", help="reset STM",
                    action="store_true")
parser.add_argument("-fps", "--fps", help="select FPS",
                    action="store")
parser.add_argument("-res", "--resolution", help="select resolution",
                    action="store", choices=['1080', '8MB'])
parser.add_argument("-cap", "--capture", help="capture an image of streamed on camera",
                    action="store_true")
parser.add_argument("-eep", "--readeeprom", help="read eeprom",
                    action="store")
parser.add_argument("-cal", "--calibrate", help="calibrate LENS/MIRROR",
                    action="store", choices=['L', 'M'])
parser.add_argument("-apk", "--apkcontrol", help="Open or close the Camera app",
                    action="store", choices=['open', 'close'])
parser.add_argument("-fpga", "--flashfpga", help="flash FPGA software",
                    action="store")
parser.add_argument("-stm", "--flashstm", help="flash STM firmware",
                    action="store")

args = parser.parse_args()



if not len(sys.argv) > 1:
    parser.print_help()
    exit
else:
    execute('adb root',0)
    #execute('adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"',0)

if args.resolution:
    m_bitmask = require_camera(args.camera)
    resolution_cmd = 'adb shell "echo 11 0x002C ' + m_bitmask + ' 0x00 0x00 0x07 0x80 0x00 0x00 0x04 0x38 > /sys/class/light_ccb/i2c_interface/i2c_w"'
    if args.resolution == "8MB":
        resolution_cmd = 'adb shell "echo 11 0x002C ' + m_bitmask + ' 0x00 0x00 0x0C 0xC0 0x00 0x00 0x09 0x90 > /sys/class/light_ccb/i2c_interface/i2c_w"'
    execute(resolution_cmd)

if args.fps:
    m_bitmask = require_camera(args.camera)
    fps_val = convert_to_hex(args.fps)
    fps_cmd = 'adb shell "echo 5 0x0050 ' + m_bitmask + ' ' + fps_val + ' > /sys/class/light_ccb/i2c_interface/i2c_w"'
    execute(fps_cmd)


if args.readeeprom:
    retry_cnt = 10
    tmp = require_camera(args.camera).replace("0x","")
    m_bitmask = tmp[6:8] + " " + tmp[3:5] + " " + tmp[0:2]
    bytetoread = convert_to_hex(args.readeeprom).replace("0x","")   
    step1 = "adb shell \"echo 02 72 " + m_bitmask + " 00 00 " + bytetoread + " > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write\""
    step2 = 'adb shell "echo 1 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/read"'
    step3 = 'adb shell "echo 02 76 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"'
    step4 = "adb shell \"echo " + args.readeeprom + " > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/read\""
    step5 = 'adb shell "cat /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/read"'
    execute(step1,1)
    data = ""
    while data.find("0x01") == -1:
        retry_cnt = retry_cnt - 1
        if retry_cnt <= 0:
            print "Time out reading eeprom"
            exit(1)
        execute_eep(step2,0)
        execute_eep('sleep 1',0)
        data = execute_eep(step5,0)
        ready = "True" if data.find("0x01") != -1 else "False"
        print "Check if eeprom is ready => " + ready 
        
    execute(step3,0)
    execute('sleep 0.5',0)
    execute(step4,0)
    execute('sleep 0.5',0)
    execute(step5)


if args.flashfpga:
    print "We will flash " + args.flashfpga + " to FPGA."
    ans = raw_input("Continue? (Y/n)")
    if ans == "Y":
        execute("adb push " + args.flashfpga + " /sdcard/fpga.bit")
        execute("adb shell flash_fpga.sh")
        execute("adb shell reboot")
        print "Done. Wait for Android reboot"
    else:
        print "End"

if args.flashstm:
    print "We will flash " + args.flashstm + " to STM."
    execute("adb push " + args.flashstm + " /sdcard/stm.bin")
    execute("adb shell flashstm32.sh")

if args.vcmposition:
    m_bitmask = require_camera(args.camera)
    fstring = convert_to_hex(args.vcmposition)
    focus_string = "adb shell \"echo 5 0x003C " + m_bitmask + " "\
                       + fstring + \
                      " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    execute(focus_string)

if args.reset:
    execute('sleep 0.5',0)
    execute('adb shell "echo gpio-85 low > /sys/class/gpio/control"',0)
    execute('sleep 0.5',0)
    execute('adb shell "echo gpio-85 high > /sys/class/gpio/control"',0)

if args.apkcontrol:
    if args.apkcontrol == "open":
        execute("adb shell am start -n co.light.rawtest.app/co.light.rawtest.app.ActivityMain")
    else:
        execute("adb shell am force-stop co.light.rawtest.app")

if args.calibrate:
    m_bitmask = require_camera(args.camera)

    calibrate_lens = "adb shell \"echo 3 0x0060 " + m_bitmask  \
                    + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    calibrate_mirror = "adb shell \"echo 3 0x0062 " + m_bitmask  \
                    + " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    if (args.camera in atypecam):
        print "Not support for A type cameras"
        exit()
    else:
        if args.calibrate == "L":
            execute(calibrate_lens)
        else:
            execute(calibrate_mirror)

if args.capture:
    execute('adb shell input tap 1 1')


if args.stream:
    m_bitmask = require_camera(args.camera)
    cam_on_str = "adb shell \"echo 5 0x0002 " + m_bitmask \
                    + " 0x00 0x01 > /sys/class/light_ccb/i2c_interface/i2c_w\""
    cam_off_str = "adb shell \"echo 5 0x0002 " + m_bitmask \
                    + " 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w\""
    if args.stream == "on":
        execute(cam_on_str)
    else:
        execute(cam_off_str)

if args.focus:
    m_bitmask = require_camera(args.camera)
    fstring = convert_to_hex(args.focus)
    print "Focus is " + args.focus
    if (args.camera in atypecam):
        # 35mm

        focus_string = "adb shell \"echo 7 0x0048 " + m_bitmask \
                       + "0x00 0x00 " + fstring + \
                       " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    else: 
        # 70m
        focus_string = "adb shell \"echo 5 0x0040 " + m_bitmask + " "\
                       + fstring + \
                       " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    execute(focus_string)

if args.mirror:
    m_bitmask = require_camera(args.camera)
    fstring = convert_to_hex(args.mirror)
    print "Mirror is " + args.mirror
    if (args.camera in atypecam):
        # 35mm
        print "no mirrors for 35mm, exiting"
        exit()
    else:
        mirror_string = "adb shell \"echo 5 0x0044 " + m_bitmask + " " +\
                         fstring + \
                         " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    execute(mirror_string)

if args.exposure:
    m_bitmask = require_camera(args.camera)
    fstring = convert_to_hex(args.exposure)
    print "Exposure is " + args.exposure
    exposure_string = "adb shell \"echo 11 0x0032 " + m_bitmask + " 0x00 0x00 0x00 0x00 0x00 0x00 "\
                       + fstring + \
                      " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    execute(exposure_string)

if args.gain:
    m_bitmask = require_camera(args.camera)
    fstring = convert_to_hex(args.gain)
    print "Gain is " + args.gain
    gain_string = "adb shell \"echo 7 0x0030 " + m_bitmask + " 0x00 0x00 "\
                   +  fstring + \
                    " > /sys/class/light_ccb/i2c_interface/i2c_w\""
    execute(gain_string)
