#!/bin/bash

adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"
sleep 1
adb shell "echo 30 > /sys/class/msm_csid/msm_csid0/mipi_input_type"
sleep 1
adb shell "echo 30 > /sys/class/msm_csid/msm_csid2/mipi_input_type"
sleep 1




