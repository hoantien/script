#!/bin/bash

adb shell "echo 0 > /sys/class/msm_csid/msm_csid0/mipi_input_type"
sleep 1
adb shell "echo 0 > /sys/class/msm_csid/msm_csid2/mipi_input_type"
sleep 1




