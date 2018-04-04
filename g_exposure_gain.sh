gain=$1
exp=$2
adb shell "fpga_off.sh"
sleep 1
adb shell "fpga_on.sh"
sleep 1
adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"
adb shell "echo 2 0x1000 0x00 0x03 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 4 0x0000 0x01 0x00 0x00 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
sleep 10
	sleep 2
	python camera_script.py -u preview -c b1 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c b2 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c b3 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c b4 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c b5 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c c1 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c c2 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c c3 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c c4 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c c5 -s on -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c c6 -s on -g $gain -e $exp
	sleep 2
#group A
	sleep 2
	python camera_script.py -u preview -c a1 -s on -f 150 -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c a2 -s on -f 150 -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c a3 -s on -f 150 -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c a4 -s on -f 150 -g $gain -e $exp
	sleep 2
	python camera_script.py -u preview -c a5 -s on -f 150 -g $gain -e $exp
	adb shell "cd /data; sh prep_capture.sh AB"
	sleep 1
	adb shell "cd /data; sh capture_new.sh AB test /sdcard/DCIM/rdi/ trigger"