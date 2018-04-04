#!/bin/bash
adb shell  "echo 1 > /sys/class/light_ccb/common/manual_control"
while true
do
	python camera_script_asb.py -c b5 -o hw
	python camera_script_asb.py -c b5 -o sw -u preview -e 50000000 -g 200 -fps 30
	python camera_script_asb.py -c b5 -u preview -e 50000000 -g 200 -fps 30
	python camera_script_asb.py -c b5 -s on -tx 0 -vc 0
	sleep 5
	python camera_script_asb.py -c b5 -s off -tx 0 -vc 0
	sleep 1
	python camera_script_asb.py -u preview -e 5000000 -g 800 -fps 30
	python camera_script_asb.py -c b5 -s on -tx 0 -vc 0
	sleep 2
	python camera_script_asb.py -c b5 -s off -tx 0 -vc 0
	python camera_script_asb.py -c b5 -o hw
	python camera_script_asb.py -c b5 -o cl
done
