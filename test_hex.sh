#!/bin/bash
t2=""
function gen_tid()
{
	tid=$((RANDOM % 65535))

	if [[ $tid -le 15 ]];then
		printf -v result "%x" "$tid"
		t1="000$result"
	elif [[ $tid -le 255 ]] && [[  $tid -gt 15  ]];then
		printf -v result "%x" "$tid"
		t1="00$result"
	elif [[ $tid -le 4095 ]] && [[  $tid -gt 255  ]];then
		printf -v result "%x" "$tid"
		t1="0$result"
	else
		printf -v result "%x" "$tid"
		t1="$result"
	fi
	t2="${t1:0:2} ${t1:2:4}"
	return $t2
}
gen_tid

echo "adb $t2"