
# Group AB
if [ $1 = "AB" ]; then
	# adb shell "echo 15 0x0011 0x00 0x00 0xFE 0x07 0x00 0x02 0x02 0x02 0x02 0x02 0x02 0x02 0x02 0x02 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	adb shell "echo 6 0x0011 0x00 0x00 0x01 0x00 0x00 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 1
	adb shell "echo 4 0x000C 0x00 0x10 0x05 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 1
	adb shell "echo 3 0x000D 0x10 0x00 0x01 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 2
	adb shell "echo 35 0x000E 0x02 0x00 0xFE 0x07 0x00 0x11 0x13 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 3
	adb shell "echo 35 0x000E 0x02 0x00 0xFE 0x07 0x00 0x10 0x13 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
# Group BC
elif [ $1 = "BC" ]; then
	adb shell "echo 16 0x0011 0x00 0x00 0xC0 0xFF 0x01 0x02 0x02 0x02 0x02 0x02 0x02 0x02 0x02 0x02 0x02 0c02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 1
	adb shell "echo 4 0x000C 0x00 0x10 0x05 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 1
	adb shell "echo 3 0x000D 0x10 0x00 0x01 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 2
	adb shell "echo 38 0x000E 0x02 0x00 0xC0 0xFF 0x01 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 3
	adb shell "echo 38 0x000E 0x02 0x00 0xC0 0xFF 0x01 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x11 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
# Group C
elif [ $1 = "C" ]; then
	adb shell "echo 11 0x0011 0x00 0x00 0x00 0xF8 0x01 0x02 0x02 0x02 0x02 0x02 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 1
	adb shell "echo 4 0x000C 0x00 0x10 0x05 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 1
	adb shell "echo 3 0x000D 0x10 0x00 0x01 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 2
	adb shell "echo 23 0x000E 0x02 0x00 0x00 0xF8 0x01 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	sleep 3
	adb shell "echo 23 0x000E 0x02 0x00 0x00 0xF8 0x01 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
elif [ $1 = "x" ]; then
	if [ $2 = "1" ]; then
		adb shell "echo 6 0x0011 0x00 0x00 0x00 0x80 0x00 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 4 0x000C 0x00 0x10 0x05 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 3 0x000D 0x10 0x00 0x01 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 2
		adb shell "echo 8 0x000E 0x02 0x00 0x00 0x80 0x00 0x11 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 3
		adb shell "echo 8 0x000E 0x02 0x00 0x00 0x80 0x00 0x10 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	elif [ $2 = "2" ]; then
		adb shell "echo 7 0x0011 0x00 0x00 0x22 0x00 0x00 0x02 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 4 0x000C 0x00 0x10 0x05 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 3 0x000D 0x10 0x00 0x01 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 2
		adb shell "echo 11 0x000E 0x02 0x00 0x22 0x00 0x00 0x11 0x12 0x00 0x11 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 3
		adb shell "echo 11 0x000E 0x02 0x00 0x22 0x00 0x00 0x10 0x12 0x00 0x10 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	elif [ $2 = "3" ]; then
		adb shell "echo 8 0x0011 0x00 0x00 0xA2 0x00 0x00 0x02 0x02 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 4 0x000C 0x00 0x10 0x05 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 3 0x000D 0x10 0x00 0x01 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 2
		adb shell "echo 14 0x000E 0x02 0x00 0xA2 0x00 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 3
		adb shell "echo 14 0x000E 0x02 0x00 0xA2 0x00 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	elif [ $2 = "4" ]; then
		adb shell "echo 9 0x0011 0x00 0x00 0xA2 0x02 0x00 0x02 0x02 0x02 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 4 0x000C 0x00 0x10 0x05 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 3 0x000D 0x10 0x00 0x01 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 2
		adb shell "echo 17 0x000E 0x02 0x00 0xA2 0x02 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 3
		adb shell "echo 17 0x000E 0x02 0x00 0xA2 0x02 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	elif [ $2 = "5" ]; then
		adb shell "echo 10 0x0011 0x00 0x00 0xA2 0x06 0x00 0x02 0x02 0x02 0x02 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 4 0x000C 0x00 0x10 0x05 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 1
		adb shell "echo 3 0x000D 0x10 0x00 0x01 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 2
		adb shell "echo 20 0x000E 0x02 0x00 0xA2 0x06 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 0x11 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		sleep 3
		adb shell "echo 20 0x000E 0x02 0x00 0xA2 0x06 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 0x10 0x12 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	fi
else
	echo "Not supported"
fi