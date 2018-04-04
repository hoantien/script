#!/bin/bash
path=$1
folder_list=(`ls $path`)
for i in ${!folder_list[*]}
do
	gedit $path/${folder_list[$i]}/AB_1.out
done
