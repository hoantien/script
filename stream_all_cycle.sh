#!/bin/bash
delay=$1
exp_list=("50000000" "100000000" "250000000" "1000000000" "1500000000")
for j in ${!exp_list[*]} 
do
    python camera_script.py -c a1 -s on -f 150 -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c a2 -s on -f 150 -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c a3 -s on -f 150 -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c a4 -s on -f 150 -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c a5 -s on -f 150 -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c b1 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c b2 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c b3 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c b4 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c b5 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c c1 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c c2 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c c3 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c c4 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c c5 -s on -u preview -e ${exp_list[$j]}
    sleep $delay

    python camera_script.py -c c6 -s on -u preview -e ${exp_list[$j]}
    sleep $delay
done
