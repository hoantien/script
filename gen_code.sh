#!/bin/bash
#=("17338" "17386" "17434" "17482" "17530" "17578" "17625" "17673" "17721" "17768" "17815" "17862" "17909" "17956" "18004" "18051" "18098" "18146" "18193" "18241" "18288" "18336" "18384" "18431" "18479" "18526" "18574" "18622" "18670" "18717" "18765" "18813" "18860" "18908" "18956" "19004")
path=$1
folder_list=(`ls $path`)
for i in ${!folder_list[*]}
do
	rm $path/${folder_list[i]}/*.out
done
i=0
sh read_md5.sh $path/BC_RDI_test_0_0_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_0_1_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_0_2_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_0_3_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_0_4_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_0_5_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_1_0_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_1_1_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_1_2_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_1_3_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_1_4_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_1_5_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_2_0_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_2_1_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_2_2_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_2_3_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_2_4_0_1
i=$((i+1))
sh read_md5.sh $path/BC_RDI_test_2_5_0_1