#!/bin/bash
path=$1
folder_list=(`ls $path`)
for i in ${!folder_list[*]}
do
	python ../split_image.py -f i3_e_100_g_100_z_1.0.raw -g AB
	./../quick_phase/quick_phase --fmt=5 -x i3_e_100_g_100_z_1.0_raw_*.raw
done
