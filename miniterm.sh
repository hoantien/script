#!/bin/sh
adb root
sleep 2
adb shell "miniterm -s 115200 /dev/ttyHSL$1"
