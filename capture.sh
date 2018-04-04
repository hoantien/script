#!/bin/bash
group=$1
k=0
i=0
j=0
#while (($i<10))
#do
#	k=0
#	while (($k<10))
#	do
#		adb shell "cd /data; sh prep_capture.sh $group"
#		adb shell "cd /data; sh capture_new.sh $group test /sdcard/DCIM/rdi/ trigger"
#		sleep 5
#		sh ucid_preview.sh
#		sleep 1
#		k=$((k+1))
#	done
#	adb shell "rm -rf /sdcard/DCIM/rdi/*"
#	sleep 1
#	i=$((i+1))
#done
#while (($j<10))
#do
	adb shell "cd /data; sh prep_capture.sh $group"
	sleep 1
	adb shell "cd /data; sh capture_new.sh $group test /sdcard/DCIM/rdi/ trigger"
#	sleep 5
#	sh ucid_preview.sh
#	sleep 1
#	j=$((j+1))
#done
