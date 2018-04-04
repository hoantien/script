#!/bin/bash
path=$1
array=(`ls $path`)

len=${#array[*]}

i=0
max=$len
max=$((max-2))

while [ $i -lt $max ]
do
	cam=0
	while [ $cam -lt 10 ]
	do
		A1prev=`dd bs=9987840 skip=$cam count=1 if=${array[$i]} 2> /dev/null | md5sum`
		A1next=`dd bs=9987840 skip=$cam count=1 if=${array[$i+1]} 2> /dev/null | md5sum`
		if [ “${A1prev}” = “${A1next}” ];then
			echo “SAME IMAGE: ${array[$i]} and ${array[$j]}”
			echo “CAMERA: ${cam}”
			echo ”HASH: ${A1prev}, ${A1next}”
		else
			echo “DIFFERENT:$i, $cam: ${A1prev}, ${A1next}”
		fi
		let cam++
	done
	let i++
done