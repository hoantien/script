#!/bin/bash
path_scr=$1
k=1
# path_des=$2
folder_list=(`ls $path_scr`)
for i in ${!folder_list[*]}
do
	sudo mv $path_scr/${folder_list[i]}/*.raw $path_scr${folder_list[i]}/AB_$k.raw13
	k=$((k+1))
done