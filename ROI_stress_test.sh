

adb shell "echo 13 0x0001 0x5a 0x80 0x04 0x00 0x00 0xa8 0x07 0xe8 0x05 0x40 0x01 0x80 0x00  > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"

adb shell "echo 2 0x0002 0x7C 0x02 > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_w"
adb shell "echo 4 0x027C > /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br"
adb shell "cat /sys/class/i2c-adapter/i2c-11/11-0010/i2c_br"