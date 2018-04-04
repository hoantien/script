#!/bin/bash

mkdir RDI_capture
cd RDI_capture
time=0
while [ $time -lt 3 ] 
do
	mkdir $time

	adb root
	adb reboot

	adb wait-for-device
	sleep 20
	adb root
	sleep 2

	echo "adb shell fpga_on.sh"
	adb shell fpga_off.sh
	adb shell fpga_on.sh
	adb shell fpga_on.sh

	echo 'adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"'
	adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"

	echo "adb shell input keyevent 26"
	adb shell input keyevent 26

	sleep 1
	echo "adb shell input keyevent 82"
	adb shell input keyevent 82

	#remove all raw, image and json files
	adb shell rm /sdcard/DCIM/*.raw
	adb shell rm /sdcard/DCIM/*.jpg
	adb shell rm /sdcard/DCIM/*.json 

	sleep 1
	echo "Open apk"
	adb shell monkey -p co.light -c android.intent.category.LAUNCHER 1

	sleep 1
	temp=0
	while [ $temp -lt 20 ]
	do
		sleep 1
		adb shell input tap 700 350
		temp=$((temp+1))
	done
	echo "Set low exposure"

	exptemp=0
	while [ $exptemp -lt 6 ]

	do
		sleep 2
		echo "Set low exposure"
		adb shell input tap 150 570
		exptemp=$((exptemp+1))
	done

	sleep 2
	echo "Tap exposure button"

	exposure=0
	while [ $exposure -lt 13 ]
	do
		sleep 2
		echo "tap $exposure time"
		adb shell input tap 100 470

		sleep 2
		echo "Capture"
		adb shell "input keyevent KEYCODE_CAMERA"

		tempdelay=0
		while [ $tempdelay -lt 20 ]
		do
			sleep 1
			adb shell input tap 700 350
			tempdelay=$((temp+1))
		done
		exposure=$((exposure+1))
	done


	cd $time
	adb pull /sdcard/DCIM/	
	time=$((time+1))
	cd ..
done
