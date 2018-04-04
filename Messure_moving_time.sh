#!/bin/bash

adb shell "echo 6 0x0000 0x00 0x80 0x00 0x10 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w"
adb shell "echo 8 0x0015 0x40 0x80 0x00 0x10 0x00 0x00 0x00 0x05 > /sys/class/light_ccb/i2c_interface/i2c_w"
adb shell "echo 4 0x0015 0x24 0x80 0x40 0x80 > /sys/class/light_ccb/i2c_interface/i2c_w"
adb shell "echo 0x18,0x0024 > /sys/class/light_ccb/i2c_interface/i2c_addr"
adb shell "echo 4 > /sys/class/light_ccb/i2c_interface/i2c_br"
adb shell "cat /sys/class/light_ccb/i2c_interface/i2c_br"
