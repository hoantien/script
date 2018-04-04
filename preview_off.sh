#!/bin/bash


############ Check if FPGA was being reset ##############
## If readback fails to match expected value, FPGA was being reset before this point
echo "Checking if FPGA is being reset. If readback fails to match expected value, FPGA was being reset before this point"
sh verify_simple.sh
sleep 5

############ Preview off ##############
adb shell "echo 5 0x004E 0x00 0x01 0x02 0xB4 0x00  > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
############# Trigger off  ###############
adb shell "echo 9 0x004E 0x00 0x01 0x06 0xE4 0x00 0xFE 0x07 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 5

############ Check if FPGA was being reset ##############
## If readback fails to match expected value, FPGA was being reset before this point
echo "Checking if FPGA is being reset. If readback fails to match expected value, FPGA was being reset before this point"
sh verify_simple.sh
sleep 5



