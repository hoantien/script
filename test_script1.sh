#!/bin/bash

sh fpga_on.sh
sleep 2
sh manual_mode.sh
sleep 1
sh ucid_preview.sh
sleep 1
python camera_script.py -c a1 -e 50000000 -g 0x1000 -f 150 -s on -u preview
sleep 1
#sh setup_CS_for_preview.sh
#sleep 1
#sh set_preview_ucid.sh
#sleep 1
python camera_script.py -c a2 -e 50000000 -g 0x1000 -f 150 -s on -u preview
sleep 1
#sh setup_CS_for_preview.sh
#sleep 1
#sh set_preview_ucid.sh
#sleep 1
python camera_script.py -c a3 -e 50000000 -g 0x1000 -f 150 -s on -u preview
sleep 1
#sh setup_CS_for_preview.sh
#sleep 1
#sh set_preview_ucid.sh
#sleep 1
python camera_script.py -c a4 -e 50000000 -g 0x1000 -f 150 -s on -u preview
sleep 1
#sh setup_CS_for_preview.sh
#sleep 1
#sh set_preview_ucid.sh
#sleep 1
python camera_script.py -c a5 -e 50000000 -g 0x1000 -f 150 -s on -u preview
sleep 1
#sh setup_CS_for_preview.sh
#sleep 1
#sh set_preview_ucid.sh
#sleep 1
python camera_script.py -c a1 -e 50000000 -g 0x1000 -f 150 -s on -u preview
sleep 1
python camera_script.py -c a1 -e 50000000 -g 0x1000 -f 150 -u preview
sleep 1
python camera_script.py -c a2 -e 50000000 -g 0x1000 -f 150 -u preview
sleep 1
python camera_script.py -c a3 -e 50000000 -g 0x1000 -f 150 -u preview
sleep 1
python camera_script.py -c a4 -e 50000000 -g 0x1000 -f 150 -u preview
sleep 1
python camera_script.py -c a5 -e 50000000 -g 0x1000 -f 150 -u preview
sleep 1
python camera_script.py -c b1 -e 50000000 -g 0x1000 -u preview
sleep 1
python camera_script.py -c b2 -e 50000000 -g 0x1000 -u preview
sleep 1
python camera_script.py -c b3 -e 50000000 -g 0x1000 -u preview
sleep 1
python camera_script.py -c b4 -e 50000000 -g 0x1000 -u preview
sleep 1
python camera_script.py -c b5 -e 50000000 -g 0x1000 -u preview
sleep 1
adb shell sh /data/prep_capture.sh AB
sleep 1
#sh ../compimaging/capture_scripts/pull_lens_piezo.sh
#sleep 1
#sh ../compimaging/capture_scripts/pull_mirror_piezo.sh
#sleep 1
adb shell sh /data/capture_new.sh AB test /sdcard/DCIM/rdi/ trigger
