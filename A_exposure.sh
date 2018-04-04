expa1=$1
expa2=$2
expa3=$3
expa4=$4
expa5=$5
    python camera_script.py -u preview -c a1 -f 150 -e $expa1
    sleep 1
	python camera_script.py -u preview -c a2 -f 150 -e $expa2
    sleep 1
    python camera_script.py -u preview -c a3 -f 150 -e $expa3
    sleep 1
	python camera_script.py -u preview -c a4 -f 150 -e $expa4
    sleep 1
    python camera_script.py -u preview -c a5 -f 150 -e $expa5
    sleep 1
