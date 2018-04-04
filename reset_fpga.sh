#!/bin/bash
adb shell fpga_off.sh
adb shell fpga_on.sh
sleep 1
adb shell "echo 02 19 00 1F 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
sh manual_mode.sh
sh ucid_preview.sh
sh open_g_enable.sh