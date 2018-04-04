#!/bin/bash
log=$1
if [[ $log = "debug" ]]; then
	adb shell "echo 02 19 00 10 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
elif [[ $log = "error" ]]; then
	adb shell "echo 02 19 00 02 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
elif [[ $log = "all" ]]; then
	adb shell "echo 02 19 00 1F 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
elif [[ $log = "warning" ]]; then
	adb shell "echo 02 19 00 04 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
elif [[ $log = "info" ]]; then
	adb shell "echo 02 19 00 08 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
else
	adb shell "echo 02 19 00 00 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
fi
