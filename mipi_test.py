import argparse
import string
import subprocess
import sys
import time
import datetime

def execute(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    return proc.communicate()[0]

def open_dual_cam():
    cmd = "adb shell am start -n co.light.simpledualstream.app/.MainActivity"
    execute(cmd)

def close_dual_cam():
    cmd = "adb shell am force-stop co.light.simpledualstream.app"
    execute(cmd)

def open_camera2basic():
    cmd = "adb shell am start -n co.light/.CameraActivity"
    execute(cmd)

def close_camera2basic():
    cmd = "adb shell am force-stop co.light"
    execute(cmd)

def kill_daemon():
    cmd = "adb shell \"ps | grep mm-qca\" | awk '{print $2'}"
    pid = execute(cmd).strip()
    cmd = "adb shell kill -9 " + str(pid)
    print "Killing process " + str(pid)
    execute(cmd)

def reset_asb():
    cmd = "sudo gpio reset"
    execute(cmd)

parser = argparse.ArgumentParser()
parser.add_argument("-v, --verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-w", "--wrap_sensor", help="Do sensor wrap around", action="store", choices=['atcm', 'btcm', 'sram','ddr3'])
parser.add_argument("-sp", "--single_preview", help="Do single preview on 1080p", action="store_true")
parser.add_argument("-dp", "--dual_preview", help="Do dual preview on 1080p", action="store_true")
parser.add_argument("-pns", "--preview_snapshot", help="Do preview and snapshot", action="store_true")
parser.add_argument("-dpn1s", "--dual_preview_snapshot", help="Do dual preview and snapshot", action="store", choices=['vc2', 'vc3', 'vc23'])
parser.add_argument("-pnds", "--preview_dual_snapshot", help="Do single preview and dual snapshot", action="store_true")
parser.add_argument("-pnxs", "--preview_x_snapshot", help="Do single preview and x snapshot", action="store", choices=['vc12','vc13','vc23','vc123'])
parser.add_argument("-mt", "--regress", help="Open cam, do preview and snapshot for 3 frames, close cam, loop ", action="store_true")
parser.add_argument("-r", "--reset", help="Reset ASB", action="store_true")
parser.add_argument("-o", "--open", help="Open cameras", action="store", choices=['a1', 'a2', 'dual'])
parser.add_argument("-f", "--flash", help="Flash MB image (boot, system)", action="store_true")
parser.add_argument("-c", "--change_lib", help="Push on library", action="store")

args = parser.parse_args()

#kill_daemon()
#exit()
#execute("adb wait-for-devices")
execute("adb root")

if args.flash:
    execute("adb reboot bootloader")
    execute("set -o errexit")
    execute("sudo fastboot -i 0x18d1 flash boot boot.img")
    execute("sudo fastboot -i 0x18d1 flash system system.img")
    execute("sudo fastboot -i 0x18d1 reboot")
    exit()

if args.change_lib:
    p = args.change_lib
    execute("adb remount")
    execute("adb push " + p)
    execute("adb reboot")
    exit()

if args.open:
    cmd = "sudo ft4222 cmd 0x08 0x09 0x00 0x00 0x00 0x00 0x06 0x00 0x00 0x02 0x02"
    if args.open == 'a1':
        cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x02 0x00 0x00 0x02"
    elif args.open == 'a2':
        cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x04 0x00 0x00 0x02"
    execute(cmd)
    exit()

if args.wrap_sensor:
    reset_asb()
    time.sleep(2)
    cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x02 0x00 0x00 0x02"
    execute(cmd)
    dst = args.wrap_sensor
    if dst == "atcm":
        cmd = "sudo ft4222 cmd 0x08 0x0a 0x00 0x00 0x56 0x00 0x01 0x00 0x00 0x30 0x03 0x00"
    elif dst == "btcm":
        cmd = "sudo ft4222 cmd 0x08 0x0a 0x00 0x00 0x56 0x00 0x01 0x00 0x00 0x40 0x03 0x00"
    elif dst == "ddr3":
        cmd = "sudo ft4222 cmd 0x08 0x0a 0x00 0x00 0x56 0x00 0x01 0x00 0x00 0x00 0x40 0x00"
    else:
        cmd = "sudo ft4222 cmd 0x08 0x0a 0x00 0x00 0x56 0x00 0x01 0x00 0xD8 0x2B 0x02 0x00"
    execute(cmd)
    exit()

if args.single_preview:
    cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x02 0x00 0x00 0x02"
    execute(cmd)
    cmd = "sudo ft4222 cmd 0x08 0x07 0x00 0x00 0x56 0x00 0x02 0x01 0xFF"
    execute(cmd)
    close_dual_cam()
    kill_daemon()
    time.sleep(3)
    open_dual_cam()
    exit()

if args.dual_preview:
    cmd = "sudo ft4222 cmd 0x08 0x09 0x00 0x00 0x00 0x00 0x06 0x00 0x00 0x02 0x02"
    execute(cmd)
    cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x56 0x00 0x0C 0xFF 0x00 0x11"
    execute(cmd)
    open_dual_cam()
    exit()

if args.preview_snapshot:
    cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x02 0x00 0x00 0x02"
    execute(cmd)
    cmd = "sudo ft4222 cmd 0x08 0x0E 0x00 0x00 0x56 0x00 0x0A 0xFF 0x00 0x01 0x01 0x00 0x00 0x80 0x00 0x64"
    execute(cmd)
    kill_daemon()
    close_dual_cam()
    open_camera2basic()
    time.sleep(30)
    close_camera2basic()
    exit()

if args.regress:
    cnt = 10
    for cnt in range(0,9):
        print "Open camera"
        cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x02 0x00 0x00 0x02"
        execute(cmd)
        print "Preview and snapshot about 32 frames"
        cmd = "sudo ft4222 cmd 0x08 0x0E 0x00 0x00 0x56 0x00 0x0A 0xFF 0x00 0x01 0xFF 0xFF 0x00 0x80 0x00 0x64"
        execute(cmd)
        time.sleep(3)
        print "Open the dual camera app, wait 30 seconds"
        open_dual_cam()
        time.sleep(30)
        print "Close dual camera app"
        close_dual_cam()
        print "Close camera"
        cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x02 0x00 0x00 0x01"
        execute(cmd)
        time.sleep(5)
    exit()


if args.dual_preview_snapshot:
    print "Open dual camera"
    close_dual_cam()
    kill_daemon()
    time.sleep(1)
    
    
    cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x02 0x00 0x00 0x02"
    execute(cmd)
    time.sleep(1)
    cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x04 0x00 0x00 0x02"
    execute(cmd)
    mode = args.dual_preview_snapshot
    if mode == 'vc2':
        cmd = "sudo ft4222 cmd 0x08 0x0B 0x00 0x00 0x56 0x00 0x0D 0xFF 0x00 0x11 0x22 0xFF 0x00"
    elif mode == 'vc3':
        cmd = "sudo ft4222 cmd 0x08 0x0B 0x00 0x00 0x56 0x00 0x0D 0xFF 0x00 0x11 0x32 0xFF 0x00"
    elif mode == 'vc23':
        cmd = "sudo ft4222 cmd 0x08 0x0B 0x00 0x00 0x56 0x00 0x0D 0xFF 0x00 0x11 0x22 0x33 0x00"
    execute(cmd)
    time.sleep(5)
    open_dual_cam()
    exit()

if args.preview_x_snapshot:
    close_dual_cam()
    kill_daemon()
    cmd = "sudo ft4222 cmd 0x08 0x08 0x00 0x00 0x00 0x00 0x02 0x00 0x00 0x02"
    execute(cmd)
    mode = args.preview_x_snapshot
    if mode == 'vc12':
        cmd = "sudo ft4222 cmd 0x08 0x0B 0x00 0x00 0x56 0x00 0x0E 0xFF 0x00 0x11 0x22 0xFF 0x00"
    elif mode == 'vc23':
        cmd = "sudo ft4222 cmd 0x08 0x0B 0x00 0x00 0x56 0x00 0x0E 0xFF 0x00 0x21 0x32 0xFF 0x00"
    elif mode == 'vc13':
        cmd = "sudo ft4222 cmd 0x08 0x0B 0x00 0x00 0x56 0x00 0x0E 0xFF 0x00 0x11 0x32 0xFF 0x00"
    elif mode == 'vc123':
        cmd = "sudo ft4222 cmd 0x08 0x0B 0x00 0x00 0x56 0x00 0x0E 0xFF 0x00 0x11 0x22 0x33 0x00"
    execute(cmd)
    
    time.sleep(5)
    open_dual_cam()
    
    exit()

if args.reset:
    cmd = "sudo FT2232_GPIO reset"
    execute(cmd)
    exit()

parser.print_help()

