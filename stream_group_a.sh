python camera_script.py -c a1 -s on -f 150  -u preview
sleep 2

python camera_script.py -c a2 -s on -f 150  -u preview
sleep 2

python camera_script.py -c a3 -s on -f 150  -u preview
sleep 2

python camera_script.py -c a4 -s on -f 150  -u preview
sleep 2

python camera_script.py -c a5 -s on -f 150  -u preview
sleep 2
adb shell "echo 7 0x0002 0x02 0x00 0x00 0x01 0x00 0x00 0x01 > /sys/class/light_ccb/i2c_interface/i2c_w"