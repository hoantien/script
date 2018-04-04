#!/bin/bash
path=$1
folder_list=(`ls $path`)
for i in ${!folder_list[*]}
do
	sh read_md5.sh $path/${folder_list[$i]}/AB_1
done
