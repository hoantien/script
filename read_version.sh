#!/bin/sh
while true;
do
	adb shell "echo 0x18,0x00A4 > /sys/class/light_ccb/i2c_interface/i2c_addr"
	adb shell "echo 4 > /sys/class/light_ccb/i2c_interface/i2c_br"
	adb shell "cat /sys/class/light_ccb/i2c_interface/i2c_br"
done