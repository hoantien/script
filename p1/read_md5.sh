#!/bin/bash

filename=$1

dd bs=9987840 skip=0 count=1 if=$filename.raw13 | md5sum > $filename.out
dd bs=9987840 skip=1 count=1 if=$filename.raw13 | md5sum >> $filename.out
dd bs=9987840 skip=2 count=1 if=$filename.raw13 | md5sum >> $filename.out
dd bs=9987840 skip=3 count=1 if=$filename.raw13 | md5sum >> $filename.out
dd bs=9987840 skip=4 count=1 if=$filename.raw13 | md5sum >> $filename.out
dd bs=9987840 skip=5 count=1 if=$filename.raw13 | md5sum >> $filename.out
dd bs=9987840 skip=6 count=1 if=$filename.raw13 | md5sum >> $filename.out
dd bs=9987840 skip=7 count=1 if=$filename.raw13 | md5sum >> $filename.out
dd bs=9987840 skip=8 count=1 if=$filename.raw13 | md5sum >> $filename.out
dd bs=9987840 skip=9 count=1 if=$filename.raw13 | md5sum >> $filename.out
