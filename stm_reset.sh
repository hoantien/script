#!/system/bin/sh
adb shell "echo gpio-85 low > /sys/class/gpio/control"
sleep 0.5
adb shell "echo gpio-85 high > /sys/class/gpio/control"
