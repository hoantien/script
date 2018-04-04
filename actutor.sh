#!/bin/bash

adb root
adb push lcc /data
adb shell "chmod +x /data/lcc"

bitmash=(
	'40 00 00'
	'80 00 00'
	'00 01 00'
	'00 02 00'
	'00 04 00'
	'00 08 00'
	'00 10 00'
	'00 20 00'
	'00 40 00'
	'00 80 00'
	'00 00 01')
cameras=('B1' 'B2' 'B3' 'B4' 'B5' 'C1' 'C2' 'C3' 'C4' 'C5' 'C6')

for cam in ${bitmash[@]}; do
	# Read hard stop 1

	# Read hard stop 2
done

index=1
while [ $index -le $loop_count ]; do
	echo "#### Start Test cycle $i ####"

	echo "Moving lens"
	i=0
	for cam in ${bitmash[@]}; do
		delta=$end-$start
		rand=$((RANDOM % $delta))
		hallcode=$start+$rand

		# Move lens of cameras[$i]
		# Read value back
		data_back=0
		# Calculate variance
		variance=0
		echo "Camera $i	Exp: $hallcode	Actual: $data_back	Variance: $variance"
		let i=i+1
	done

	echo "#### End Test cycle $i ####"
	echo ""
	let index=index+1
done
