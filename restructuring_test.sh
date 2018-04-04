#!/bin/bash

if [ "$1" = "capture" ]; then
	python camera_script_asb.py -c c5 -o sw -u hires -burst 1
	sleep 1
	python camera_script_asb.py -c c5 -s on -tx 0 -vc 1
	sleep 5
	python camera_script_asb.py -c c5 -s off -tx 0 -vc 1
elif [ "$1" = "preview" ]; then
	python camera_script_asb.py -c c5 -o sw -u preview  -e 10000000
	sleep 1
	python camera_script_asb.py -c c5 -s on -tx 0 -vc 0
	sleep 5
	python camera_script_asb.py -c c5 -s off -tx 0 -vc 0
elif [ "$1" = "preview_cycle" ]; then
	python camera_script_asb.py -c c5 -o sw -u preview -e 10000000
	sleep 1
	while true
	do
		python camera_script_asb.py -c c5 -s on -tx 0 -vc 0
		sleep 5
		python camera_script_asb.py -c c5 -s off -tx 0 -vc 0
		sleep 1
	done
elif [ "$1" = "preview_open_cycle" ]; then
	while true
	do
		python camera_script_asb.py -c c5 -o sw -u preview -e 10000000
		sleep 1
		python camera_script_asb.py -c c5 -s on -tx 0 -vc 0
		sleep 5
		python camera_script_asb.py -c c5 -s off -tx 0 -vc 0
		sleep 1
		python camera_script_asb.py -c c5 -o cl
		sleep 1
	done
elif [ "$1" = "preview_capture_cycle" ]; then
	python camera_script_asb.py -c c5 -o sw -u preview -e 10000000
	sleep 1
	while true
	do
		python camera_script_asb.py -u preview
		sleep 1
		python camera_script_asb.py -c c5 -s on -tx 0 -vc 0
		sleep 5
		python camera_script_asb.py -c c5 -s off -tx 0 -vc 0
		sleep 1
		python camera_script_asb.py -u hires
		python camera_script_asb.py -burst 1
		sleep 1
		python camera_script_asb.py -c c5 -s on -tx 0 -vc 1
		sleep 5
		python camera_script_asb.py -c c5 -s off -tx 0 -vc 1
		sleep 1
	done
elif [ "$1" = "preview_capture_open_cycle" ]; then
	while true
	do
		python camera_script_asb.py -c c5 -o sw -u preview -e 10000000
		sleep 1
		python camera_script_asb.py -u preview
		sleep 1
		python camera_script_asb.py -c c5 -s on -tx 0 -vc 0
		sleep 5
		python camera_script_asb.py -c c5 -s off -tx 0 -vc 0
		sleep 1
		python camera_script_asb.py -u hires
		python camera_script_asb.py -burst 1
		sleep 1
		python camera_script_asb.py -c c5 -s on -tx 0 -vc 1
		sleep 5
		python camera_script_asb.py -c c5 -s off -tx 0 -vc 1
		sleep 1
		python camera_script_asb.py -c c5 -o cl
		sleep 1
	done
else
	echo "capture : test snapshot"
	echo "preview : test preview"
	echo "preview_cycle : test stream on after stream off"
	echo "preview_open_cycle : test stream on after close camera"
	echo "preview_capture_cycle : test capture after preview"
	echo "preview_capture_open_cycle : test capture and preview after reopen"
fi
