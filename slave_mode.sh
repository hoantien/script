#!/bin/bash

############# Set sensors to slave mode ##############
adb shell "echo 15 0x004E 0x00 0x01 0x0C 0x82 0x00 0xFE 0x07 0x00 0x00 0x6C 0x02 0x01 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 9 0x004E 0x00 0x01 0x06 0x83 0x00 0xFE 0x07 0x00 0x00  > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 15 0x004E 0x00 0x01 0x0C 0x82 0x00 0xFE 0x07 0x00 0x00 0x6C 0x03 0x31 0x58 0xa0 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 9 0x004E 0x00 0x01 0x06 0x83 0x00 0xFE 0x07 0x00 0x00  > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 15 0x004E 0x00 0x01 0x0C 0x82 0x00 0xFE 0x07 0x00 0x00 0x6C 0x02 0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 9 0x004E 0x00 0x01 0x06 0x83 0x00 0xFE 0x07 0x00 0x00  > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1





