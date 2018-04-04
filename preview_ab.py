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
\t\t-------------------V1.1--------------------\n"

atypecam = [ 'a1', 'a2', 'a3', 'a4', 'a5' ]

camera_group = [ 'AB', 'ab', 'BC', 'bc' ]

def execute(cmd):
    #print(cmd);
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()[0]


# Run preview across all 10 cams
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x01  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x02  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x03  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x04  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x05  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x06  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x07  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x08  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x09  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)
prev_string = "adb shell  \"echo 5 0x004E 0x00 0x01 0x02 0xB4 0x0a  > /sys/class/light_ccb/i2c_interface/i2c_w\""
print prev_string
execute(prev_string)
time.sleep(5)





