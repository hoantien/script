#!/bin/bash
adb shell "fpga_off.sh"
                sleep 1
adb shell "fpga_on.sh"
                sleep 1
adb shell "echo 00 00 02 19 00 1F 00 00 00 00 00 00 00 00 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"
adb shell "echo 4 0x0000 0x00 0x90 0x03 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
                sleep 1
adb shell "echo 8 0x0000 0x00 0x80 0xA2 0x00 0x00 0x02 0x02 0x02 > /sys/class/light_ccb/i2c_interface/i2c_w"
                sleep 1
sleep 10

# Do setting

# A1
adb shell "echo 11 0x0000 0x48 0x80 0x02 0x00 0x00 0x03 0x00 0x96 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 15 0x0000 0x32 0x80 0x02 0x00 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 11 0x0000 0x30 0x80 0x02 0x00 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1

# # A2
# adb shell "echo 11 0x0000 0x48 0x80 0x04 0x00 0x00 0x00 0x03 0x96 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 15 0x0000 0x32 0x80 0x04 0x00 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x04 0x00 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # A3
# adb shell "echo 11 0x0000 0x48 0x80 0x08 0x00 0x00 0x00 0x03 0x96 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 15 0x0000 0x32 0x80 0x08 0x00 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x08 0x00 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # A4
# adb shell "echo 11 0x0000 0x48 0x80 0x10 0x00 0x00 0x00 0x03 0x96 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 15 0x0000 0x32 0x80 0x10 0x00 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x10 0x00 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# A5
adb shell "echo 11 0x0000 0x48 0x80 0x20 0x00 0x00 0x03 0x00 0x96 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 15 0x0000 0x32 0x80 0x20 0x00 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 11 0x0000 0x30 0x80 0x20 0x00 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1

# # B1
# adb shell "echo 15 0x0000 0x32 0x80 0x40 0x00 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x40 0x00 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# B2
adb shell "echo 15 0x0000 0x32 0x80 0x80 0x00 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 11 0x0000 0x30 0x80 0x80 0x00 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1

# # B3
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x01 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x01 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # B4
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x02 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x02 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # B5
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x04 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x04 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # C1
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x08 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x08 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # C2
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x10 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x10 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # C3
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x20 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x20 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # C4
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x40 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x40 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # C5
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x80 0x00 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x80 0x00 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# # C6
# adb shell "echo 15 0x0000 0x32 0x80 0x00 0x00 0x01 0x03 0x00 0x80 0xf0 0xfa 0x02 0x00 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1
# adb shell "echo 11 0x0000 0x30 0x80 0x00 0x00 0x01 0x03 0x00 0x00 0x10 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
# sleep 1

# Stream on
adb shell "echo 8 0x0000 0x02 0x80 0x02 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1
adb shell "echo 8 0x0000 0x02 0x80 0x20 0x00 0x00 0x11 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w"
sleep 1


adb shell "cd /data; sh set_capture_ucid.sh AB"
sleep 1
adb shell "cd /data; sh capture_new.sh AB test /sdcard/DCIM/rdi/ trigger"
sleep 1

