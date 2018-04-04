import argparse
import string
import subprocess
import sys
import time
import datetime
import random
import xlwt
from datetime import datetime
import os
import getpass
import time

camera = ['b1','b2','b3','b4','b5','c1','c2','c3','c4','c5','c6']
lcc_path = "adb shell \"cd data;./lcc -m 0 -s 0 "
write_path = "-w -p "
read_path = "-r -p "
isr_bit='0'
TID=0