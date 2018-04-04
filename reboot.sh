#!/bin/bash
adb reboot
adb wait-for-device
adb root
sleep 2
adb shell "echo 02 19 00 1F 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"