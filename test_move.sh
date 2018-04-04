python actuator_test.py -c b1 b2 b3 b4 b5 c1 c2 c3 c4 c5 c6 -r -l -o moving_len_random -n 100
adb shell "cd data;./prog_app_p2 -q"
sleep 15
python actuator_test.py -c b1 b2 b3 b5 c1 c2 c3 c4 -r -m -o moving_mirror_random -n 100
adb shell "cd data;./prog_app_p2 -q"
sleep 15

python actuator_test.py -c b1 b2 b3 b4 b5 c1 c2 c3 c4 c5 c6 -s 50 -l -o step_50_l -n 2
adb shell "cd data;./prog_app_p2 -q"
sleep 15
python actuator_test.py -c b1 b2 b3 b4 b5 c1 c2 c3 c4 c5 c6 -s 100 -l -o step_100_l -n 2
adb shell "cd data;./prog_app_p2 -q"
sleep 15
python actuator_test.py -c b1 b2 b3 b4 b5 c1 c2 c3 c4 c5 c6 -s 50 -m -o step_50_m -n 2
adb shell "cd data;./prog_app_p2 -q"
sleep 15
python actuator_test.py -c b1 b2 b3 b4 b5 c1 c2 c3 c4 c5 c6 -s 100 -m -o step_100_m -n 2
adb shell "cd data;./prog_app_p2 -q"
sleep 15