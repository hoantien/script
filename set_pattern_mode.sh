#!/bin/bash

#*******************************************************************************
#                            REVISION HISTORY
#*******************************************************************************
# * 1.0.0	24-Oct-2016		Initial revision 
#*******************************************************************************

#*******************************************************************************
# Syntax: 
#   $ ./set_pattern_mode.sh a1/…c6 on/off
# Example: 
#   Set a1 pattern mode
#   $ ./set_pattern_mode.sh a1 on
#   Set a1 normal mode
#   $ ./set_pattern_mode.sh a1 off
#*******************************************************************************


camlist=(
		#"CAM ASIC_NUM I2C_CHANNEL"
		"a1 0x01 0x04" #a1
		"a2 0x02 0x03" #a2
		"a3 0x02 0x04" #a3
		"a4 0x02 0x00" #a4
		"a5 0x01 0x03" #a5
		"b1 0x02 0x05" #b1
		"b2 0x01 0x05" #b2
		"b3 0x02 0x01" #b3
		"b4 0x01 0x02" #b4
		"b5 0x01 0x01" #b5
		"c1 0x03 0x02" #c1
		"c2 0x02 0x02" #c2
		"c3 0x03 0x05" #c3
		"c4 0x03 0x04" #c4
		"c5 0x01 0x00" #c5
		"c6 0x03 0x00" #c6
   )

TID=""

function gen_tid()
{
	num=$((RANDOM % 65535))

	if [[ $num -le 15 ]];then
		printf -v result "%x" "$num"
		t1="000$result"
	elif [[ $num -le 255 ]] && [[  $num -gt 15  ]];then
		printf -v result "%x" "$num"
		t1="00$result"
	elif [[ $num -le 4095 ]] && [[  $num -gt 255  ]];then
		printf -v result "%x" "$num"
		t1="0$result"
	else
		printf -v result "%x" "$num"
		t1="$result"
	fi
	TID="0x${t1:0:2}${t1:2:4}"
}

CAM_TEST=$1
CAM_TEST="${CAM_TEST,,}"
MODE=$2

for cam in "${camlist[@]}"
do
	# Read params 
	tmp=($cam)
	if [[ $CAM_TEST == ${tmp[0]} ]];then
		ASIC_NUM=${tmp[1]}
		I2C_CHANNEL=${tmp[2]}
		# Send commands
		gen_tid
		if [[ $MODE == "on" ]];then
			adb shell "echo 11 $TID 0x5B 0x00 $ASIC_NUM $I2C_CHANNEL 0x36 0x02 0x00 0x06 0x02 0x02 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		elif [[ $MODE == "off" ]];then
			adb shell "echo 11 $TID 0x5B 0x00 $ASIC_NUM $I2C_CHANNEL 0x36 0x02 0x00 0x06 0x02 0x00 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
		fi
		sleep 0.5
	fi
done





