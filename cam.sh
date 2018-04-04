#!/bin/bash
###############################################################################
log_level=1

function adb_root()
{
	adb wait-for-devices
	adb root > cam.txt
	while read line; do    
	    if [ "$line" != "\n" ]; then
	    	linex="$line"
	    fi    
	done < cam.txt

	if [ "$linex" = "adbd is already running as root" ]; then
		sleep 0
	else	
		sleep 2
	fi
	rm cam.txt
}

function log()
{	
	if [ "$1" = "all" ]; then
		echo "Active all log level"
		adb shell "echo 00 00 02 19 00 1F 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
	elif [ "$1" = "error" ]; then
		adb shell "echo 00 00 02 19 00 02 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
		echo "Active log error"
	elif [ "$1" = "warning" ]; then
		echo "Active log warning"
		adb shell "echo 00 00 02 19 00 04 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
	elif [ "$1" = "info" ]; then
		echo "Active log info"
		adb shell "echo 00 00 02 19 00 08 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
	elif [ "$1" = "debug" ]; then
		echo "Active log debug"
		adb shell "echo 00 00 02 19 00 10 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
	elif [ "$1" = "off" ]; then
		echo "Deactive all log level"
		adb shell "echo 00 00 02 19 00 00 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
	fi
}
###############################################################################
adb_root
if [ "$1" = "on" ]; then
	adb shell fpga_on.sh
	adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"
	log "$2"
elif [ "$1" = "off" ]; then
	adb shell fpga_off.sh
elif [ "$1" = "reboot" ]; then
	adb reboot
	adb_root
elif [ "$1" = "reset" ]; then
	adb shell fpga_off.sh
	sleep 1
	adb shell fpga_on.sh
	adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"
	log "$2"
elif [ "$1" = "log" ]; then
	log "$2"
elif [ "$1" = "apk_ins" ]; then
	adb install "$2"
elif [ "$1" = "apk_uins" ]; then
	adb uninstall co.light
elif [ "$1" = "stm" ]; then
	adb push "$2" /sdcard/stm.bin
	adb shell flashstm32.sh
elif [ "$1" = "fpga" ]; then
	adb push "$2" /sdcard/fpga.bit
	adb shell flash_fpga.sh
	adb reboot
	adb_root
else
	sleep 0
fi
echo "Done"
