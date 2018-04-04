#!/bin/bash
LIGHT_HEADER_VALID_MASK='hw_info->tof'

pass_cnt=0
fail_cnt=0

adb root
adb push light_header_android /data
adb shell "chmod +x /data/light_header_android"

#Test report
echo "Test report" > report.txt
echo "...................................................." >> report.txt
n=$1
k=$2
for ((c = 1; c <= n; c++ ))
do
	for ((z = 1; z <= k; z++ ))
	do
		# Remove lri file from previous capture
		#adb pull /data/misc/camera/
		adb shell "rm -f /data/misc/camera/RDI*"
		echo "Set Preview Resolution to 4208 x 3120"
		adb shell "cd data; ./lcc -m 0 -s 0 -w -p 00 00 2C 00 01 00 00 03 00 70 10 00 00 30 0C 00 00" &>/dev/null
		echo "Set Preview Gain to 1.0"
		adb shell "cd data; ./lcc -m 0 -s 0 -w -p 00 00 30 00 01 00 00 03 00 00 00 80 3F" &>/dev/null
		#echo "Set Preview FPS to 30"
		#adb shell "cd data; ./lcc -m 0 -s 0 -w -p 00 00 50 00 01 00 00 03 00 1E 00" &>/dev/null
		#echo "Set Capture Exposure Time to ????"
		#adb shell "cd data; ./lcc -m 0 -s 0 -w -p 00 00 32 00 01 00 00 03 00 80 84 1E 00 00 00 00 00" &>/dev/null

		echo "Set Capture Resolution to 4208 x 3120"
		adb shell "cd data; ./lcc -m 0 -s 0 -w -p 00 00 2C 00 01 00 00 05 00 70 10 00 00 30 0C 00 00" &>/dev/null
		echo "Set Capture Gain to 1.0"
		adb shell "cd data; ./lcc -m 0 -s 0 -w -p 00 00 30 00 01 00 00 05 00 00 00 80 3F" &>/dev/null
		#echo "Set Capture FPS to 30"
		#adb shell "cd data; ./lcc -m 0 -s 0 -w -p 00 00 50 00 01 00 00 05 00 1E 00" &>/dev/null
		#echo "Set Capture Exposure Time to ????"
		#adb shell "cd data; ./lcc -m 0 -s 0 -w -p 00 00 32 00 01 00 00 05 00 80 84 1E 00 00 00 00 00" &>/dev/null


		random=$((RANDOM % 4))
		if [ $random == 0 ]; then
			echo "CAPTURE GROUP AB"
			adb shell "cd data; ./lcc -m 0 -s 0 -f 1 FE 07 00 11 21 00 -R 4208,3120"
		elif [ $random == 1 ];then
			echo "CAPTURE GROUP BC"
			adb shell "cd data; ./lcc -m 0 -s 0 -f 1 C0 FF 01 11 21 00 -R 4208,3120"
		elif [ $random == 2 ];then
			echo "CAPTURE GROUP C"
			adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 F8 01 11 21 00 -R 4208,3120"
		elif [ $random == 3 ];then
			echo "CAPTURE GROUP ABC"
			adb shell "cd data; ./lcc -m 0 -s 0 -f 1 FE FF 01 11 21 00 -R 4208,3120"
		fi
		lri_name=$(adb shell "ls /data/misc/camera | grep RDI")
		if [ ! $lri_name ]; then
			fail_cnt=$((fail_cnt+1))
			echo "FAILED to capture. No lri file generated." >> report.txt
		else
			lri_name=$(echo $lri_name | sed $'s/\r//')
			lri_name="/data/misc/camera/"$lri_name
			if [ $random == 0 ];then
				valid_line_count=$(adb shell "/data/light_header_android $lri_name 2" | grep "$LIGHT_HEADER_VALID_MASK" | wc -l)
				if [ "$valid_line_count" -ne "2" ]; then
					fail_cnt=$((fail_cnt+1))
					echo "FAILED to parse light header info." >> report.txt
				else
					pass_cnt=$((pass_cnt+1))
					echo "Capture PASS" >> report.txt
				fi
			else
				valid_line_count=$(adb shell "/data/light_header_android $lri_name 3" | grep "$LIGHT_HEADER_VALID_MASK" | wc -l)
				if [ "$valid_line_count" -ne "3" ]; then
					fail_cnt=$((fail_cnt+1))
					echo "FAILED to parse light header info." >> report.txt
				else
					pass_cnt=$((pass_cnt+1))
					echo "Capture PASS $pass_cnt" >> report.txt
				fi
			fi
		fi
	done
	adb shell "cd /data/; ls; ./prog_app_v02 -q" &>/dev/null
	echo "Reseting the ASICs. Please wait"
	echo "Times capture pass: "$pass_cnt
	echo "Times capture fail: "$fail_cnt
	sleep 20
done

echo "Times capture pass: "$pass_cnt >> report.txt
echo "Times capture fail: "$fail_cnt >> report.txt
