import sys, os, argparse, string

# given a 200MB binary file, split it into 10 images
# only the first 100MB is image data

# I2C ordering
# 00 A2
# 01 A1
# 02 A4
# 03 A5
# 04 A3
# 05 B4
# 06 B5
# 07 B3
# 08 B2
# 09 B1
# 10 C1
# 11 C2
# 12 C4
# 13 C3
# 14 C6
# 15 C5

# file name is always dump.raw
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="give the input filename",
                    action="store")
parser.add_argument("-g", "--group", help="give the RDI groups: 'AB' or 'BC'",
                    action="store")

args = parser.parse_args()

if args.filename:
    original = open(args.filename, 'rb')
else:
    print "Give a filename with the -f flag"
    exit()
if args.group:
    if args.group == 'AB' or args.group == 'ab':
        camera_list = ['a2', 'a1', 'a4', 'a5', 'a3', 'b4', 'b5', 'b3', \
                       'b2', 'b1']
    elif args.group == 'BC' or args.group == 'bc' :
        # since we are not capturing with C6 in RDI capture, we leave it out
        # the following is the explicit I2C ordering
        #camera_list = ['b4', 'b5', 'b3', 'b2', 'b1', 'c1', 'c2', 'c4', \
        #               'c3', 'c6', 'c5']
        # the following is the ordering with C6 missing 
        camera_list = ['b4', 'b5', 'b3', 'b2', 'b1', 'c1', 'c2', 'c4', \
                       'c3', 'c5'] #'c6'
    elif args.group == 'C' or 'c':
        camera_list = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6']
    else:
        print "Group name must be 'AB' or 'BC'. Exiting..."
        exit()
else:
    print "Give a filename with the -f flag"
    exit()

#camera_list = ['a2', 'a1', 'a4', 'a5', 'a3', 'b4', 'b5', 'b3', \
#               'b2', 'b1', 'c1', 'c2', 'c4', 'c3', 'c6', 'c5']

image_x_pixels = 3264
image_y_pixels = 2448
image_size = image_x_pixels * image_y_pixels
image_bytes = (image_size * 10) / 8

offset = 0;
output_name = ""
if args.filename[-4:] == ".raw":
    name = args.filename[:-4]
else:
    name = args.filename

if args.group == 'AB' or args.group == 'ab' or args.group == 'BC' or args.group == 'bc':
    for i in xrange(10):
        print camera_list[i]
        offset = i * image_size;
        output_name = name + "_" + camera_list[i] + ".raw"
        out_file = open(output_name, "wb")
        data = original.read(image_bytes)
        print output_name
        out_file.write(data)
        out_file.close()
else :
    for i in xrange(6) :
        print camera_list[i]
        offset = i * image_size;
        output_name = name + "_" + camera_list[i] + ".raw"
        out_file = open(output_name, "wb")
        data = original.read(image_bytes)
        print output_name
        out_file.write(data)
        out_file.close()
        
original.close()






