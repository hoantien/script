while true
do
adb shell "cd data;./lcc -m 0 -s 0 -w -p 00 01 40 00 40 00 00 FF FF"
adb shell "cd data;./lcc -m 0 -s 0 -r -p 00 01 40 00 40 00 00"
done
