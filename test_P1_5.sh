#!/bin/bash

# adb wait-for-devices
# adb root
while true
do
	#open camera
	./camera_script_asb.py -c c5 -o sw

	#set ucid preview
	./camera_script_asb.py -u preview

	# #set fps 20
	# ./camera_script_asb.py -c c5 -u preview -fps 20 -e 5000000 -g 200

	#stream on a1
	./camera_script_asb.py -c c5 -s on -tx 0
	#sleep 10

	#stream off a1
	./camera_script_asb.py -c c5 -s off -tx 0

	#close camera
	./camera_script_asb.py -c c5 -o cl
	# python camera_script_asb.py -c a1 -rhsv -m
done
