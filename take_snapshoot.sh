#!/bin/sh
if [ "$1" = "AB" ]; then
	adb shell "cd /data; sh set_capture_ucid.sh AB"
	sleep 2
	adb shell "cd /data; sh capture_new.sh AB test /sdcard/DCIM/rdi/ trigger"
	sleep 1
elif [ "$1" = "BC" ]; then
	adb shell "cd /data; sh set_capture_ucid.sh BC"
	sleep 2
	adb shell "cd /data; sh capture_new.sh BC test /sdcard/DCIM/rdi/ trigger"
	sleep 1
elif [ "$1" = "C" ]; then
	adb shell "cd /data; sh set_capture_ucid.sh C"
	sleep 2
	adb shell "cd /data; sh capture_new.sh C test /sdcard/DCIM/rdi/ trigger"
	sleep 1
fi