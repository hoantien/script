#*******************************************************************************
# Syntax: $ read_eeprom.sh module_id block_size offset output_file
# Example: $ read_eeprom.sh A1 512 1 text.txt

if [ "$#" -lt 3 ]
then
	echo "Number of arguments is not correct."
	exit
fi

if [ "$#" -eq 3 ]
then
	echo "Default offset"
	module_id=$1                                 # Module bit mask
	block_size=$2                                # Block size that needs to be read 
	offset=$((0))        	                     # Default offset
	output_file=$3                               # Output directory
fi
if [ "$#" -eq 4 ] 
then
	module_id=$1                                 # Module bit mask
	block_size=$2                                # Block size that needs to be read 
	offset=$(($3))                               # Chunk offset
	output_file=$4                               # Output directory 
fi

if [ "$#" -gt 4 ]
then
	echo "Redundant command's parameters"
	exit
fi

#*******************************************************************************
# Constants
#declare -A cam_hash
#cam_hash=(["A1"]="02 00 00"  ["A2"]="04 00 00" ["A3"]="08 00 00" \
#          ["A4"]="10 00 00"  ["A5"]="20 00 00" ["B1"]="40 00 00" \
#          ["B2"]="80 00 00"  ["B3"]="00 01 00" ["B4"]="00 02 00" \
#          ["B5"]="00 04 00"  ["C1"]="00 08 00" ["C2"]="00 10 00" \
#          ["C3"]="00 20 00"  ["C4"]="00 40 00" ["C5"]="00 80 00" \
#          ["C6"]="00 00 01")
cam_hash=("02 00 00"  "04 00 00" "08 00 00" \
          "10 00 00"  "20 00 00" "40 00 00" \
          "80 00 00"  "00 01 00" "00 02 00" \
          "00 04 00"  "00 08 00" "00 10 00" \
          "00 20 00"  "00 40 00" "00 80 00" \
          "00 00 01")                          
module_id_hash=("A1" "A2" "A3" "A4" "A5" \
                "B1" "B2" "B3" "B4" "B5" \
                "C1" "C2" "C3" "C4" "C5" "C6")                          
                  
slave_ID_hash=("00" "02" "04" "06")
addr_hash=("0" "512" "1024" "1536")
block_size_hash=("512" "1024" "2048")
#*******************************************************************************
# Error handling
#*******************************************************************************
valid="no"
for index in ${!block_size_hash[*]}
do 
	if [ "$block_size" = ${block_size_hash[$index]} ]
	then
		valid="yes"
		break
	fi
done
if ((block_size < 0)) || ((block_size > 2048)) || [ $valid = "no" ]
then
	echo "Invalid data block size"
	echo "Please type the command according following:"
	echo "Syntax: sh read_eeprom.sh module_id block_size offset output_file"
	echo "  + module_id: camera module (A1-A5,B1-B5,C1-C6)"
	echo "  + block_size: size in bytes of memory block that needs to be "
	echo "		      read (512, 1024, 2048)"
	echo "  + offset: chunk offset of the data address (0, 1, 2, 3)"
	echo "  + output_file: output filename"
	exit
fi
#*******************************************************************************
# Check chunk
#if (($((2048%blocksize)) >  0))
#then
#	echo "The chunk is NG. Please use the block size as one of 512, 1024 or"
#	echo "2048"
#	exit
#fi
#*******************************************************************************
# Check bit mask
module_index=$((16))
index=$((0))
module_bit_mask=""
for index in ${!module_id_hash[*]}
do
	if [ $module_id = ${module_id_hash[$index]} ]
	then
		module_bit_mask=${cam_hash[$index]}
		break;
	fi
done
if [ "$module_bit_mask" = "" ]
then
	echo "Invalid module ID"
	echo "The module_ID have to be one of these:"
	for CAM in ${module_id_hash[@]}
	do
		echo ${CAM}
	done
	exit
fi
#*******************************************************************************
# Check offset
if ((offset * block_size >= 2048))
then
	echo "The offset is out of range"
	exit
fi
#******************************************************************************* 
# Convert block size
#hex_size=$(printf '%04x\n' $block_size)
#hex_size=$(echo $((16#$block_size)))
#hex_size=$(hexdump -e '"%04x"' <<< "$block_size")
# 512
if [ $block_size = 512 ]
then 
	hex_size="0200"
fi
# 1024
if [ $block_size = 1024 ]
then 
	hex_size="0400"
fi
# 2048
if [ $block_size = 2048 ]
then 
	hex_size="0800"
fi

byte1=${hex_size:0:2} 
byte0=${hex_size:2:2}
#*******************************************************************************
# Parse offset address
hex_addr=""
index=$((0))
for index in ${!addr_hash[*]}
do
	if [ $((offset*block_size)) = ${addr_hash[$index]} ]
	then
		hex_addr=${slave_ID_hash[$index]}
		break
	fi	
done
#*******************************************************************************
# Call to camera
tmp=""
echo "echo 00 00 02 72 $module_bit_mask 04 $hex_addr 00 $byte1 $byte0 00 00  > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write"
echo 00 00 02 72 $module_bit_mask 04 $hex_addr 00 $byte1 $byte0  00 00  > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/write
count=$((0)) 
	while [ "$tmp" = "" ] 
	do
		count=$((count+1))
		echo 1 > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/read
		sleep 1
		tmp=$(cat /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/read | grep "0x01")
		if (( $count > 30 ))
		then
			echo "There is no respond from STM FW" 
			exit
		fi
	done
echo $block_size > /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/read
cat /sys/devices/soc.0/f9923000.spi/spi_master/spi0/spi0.0/read >> $output_file
sleep 1
