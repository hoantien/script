adb shell am force-stop org.codeaurora.snapcam
adb shell setprop debug.factory.light.preview 3
adb shell "echo 1 > /sys/class/light_ccb/common/manual_control"
adb shell "echo 6 0x0000 0x00 0x00 0x00 0x08 0x00 0x02  > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
sleep 2
adb shell 'echo 4 0x0000 0x00 0x10 0x03 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w'
adb shell "echo 8 0x0000 0x02 0x00 0x00 0x08 0x00 0x11 0x00 0x00 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
adb shell monkey -p org.codeaurora.snapcam -c android.intent.category.LAUNCHER 1