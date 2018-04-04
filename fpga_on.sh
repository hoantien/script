#!/bin/bash
adb wait-for-devices && adb root
sleep 3
adb shell fpga_on.sh
adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"
if [ "$1" = "log" ]; then
	adb shell "echo 00 00 02 19 00 1F 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
fi

