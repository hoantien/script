#!/bin/bash
adb root
NOFILE="lcc: No such file"
CHECKFILE=`adb shell "cd /data; ls lcc"`

if [[ "$CHECKFILE" == $NOFILE* ]];then
	echo "Copying the lcc app to mainboard"
	adb push lcc /data
	adb shell "chmod +x /data/lcc"
fi

if [[ $1 == "AB" ]] || [[ $1 == "ab" ]];then
	echo "CAPTURE GROUP AB"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 FE 07 00 11 21 00"
elif [[ $1 == "BC" ]] || [[ $1 == "bc" ]];then
	echo "CAPTURE GROUP BC"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 C0 FF 01 11 21 00"
elif [[ $1 == "C" ]] || [[ $1 == "c" ]];then
	echo "CAPTURE GROUP C"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 F8 01 11 21 00"
elif [[ $1 == "ABC" ]] || [[ $1 == "abc" ]];then
	echo "CAPTURE GROUP ABC"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 FE FF 01 11 21 00"

elif [[ $1 == "A1" ]] || [[ $1 == "a1" ]];then
	echo "CAPTURE CAMERA A1"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 02 00 00 11 21 00"
elif [[ $1 == "A2" ]] || [[ $1 == "a2" ]];then
	echo "CAPTURE CAMERA A3"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 04 00 00 11 21 00"
elif [[ $1 == "A3" ]] || [[ $1 == "a3" ]];then
	echo "CAPTURE CAMERA A3"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 08 00 00 11 21 00"
elif [[ $1 == "A4" ]] || [[ $1 == "a4" ]];then
	echo "CAPTURE CAMERA A4"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 10 00 00 11 21 00"
elif [[ $1 == "A5" ]] || [[ $1 == "a5" ]];then
	echo "CAPTURE CAMERA A5"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 20 00 00 11 21 00"
elif [[ $1 == "B1" ]] || [[ $1 == "b1" ]];then
	echo "CAPTURE CAMERA B1"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 40 00 00 11 21 00"
elif [[ $1 == "B2" ]] || [[ $1 == "b2" ]];then
	echo "CAPTURE CAMERA B2"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 80 00 00 11 21 00"
elif [[ $1 == "B3" ]] || [[ $1 == "b3" ]];then
	echo "CAPTURE CAMERA B3"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 01 00 11 21 00"
elif [[ $1 == "B4" ]] || [[ $1 == "b4" ]];then
	echo "CAPTURE CAMERA B4"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 02 00 11 21 00"
elif [[ $1 == "B5" ]] || [[ $1 == "b5" ]];then
	echo "CAPTURE CAMERA B5"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 04 00 11 21 00"
elif [[ $1 == "C1" ]] || [[ $1 == "c1" ]];then
	echo "CAPTURE CAMERA C1"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 08 00 11 21 00"
elif [[ $1 == "C2" ]] || [[ $1 == "c2" ]];then
	echo "CAPTURE CAMERA C2"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 10 00 11 21 00"
elif [[ $1 == "C3" ]] || [[ $1 == "C3" ]];then
	echo "CAPTURE CAMERA C3"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 20 00 11 21 00"
elif [[ $1 == "C4" ]] || [[ $1 == "c4" ]];then
	echo "CAPTURE CAMERA C4"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 40 00 11 21 00"
elif [[ $1 == "C5" ]] || [[ $1 == "c5" ]];then
	echo "CAPTURE CAMERA C5"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 80 00 11 21 00"
elif [[ $1 == "C6" ]] || [[ $1 == "c6" ]];then
	echo "CAPTURE CAMERA C6"
	adb shell "cd data; ./lcc -m 0 -s 0 -f 1 00 00 01 11 21 00"

else
	echo "Not supported this argument"
	echo "Please follow :"
	echo "./capture_lcc <GROUP AB or BC>"
fi
