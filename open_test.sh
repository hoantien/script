#!/bin/bash
i=0
while [[ $i -lt 10000 ]]
do
	adb shell "echo 6 0x0000 0x00 0x00 0x01 0x00 0x00 0x02  > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
	echo $i
	i=$(($i+1))
done
