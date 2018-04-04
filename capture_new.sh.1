#d!/system/bin/sh
# Revision 1.7
# Mar 25, 2016

################################################################################
#                             HELPER FUNCTIONS                                 #
################################################################################

# This version of the capture script supports both I2C and trigger.

do_wait_pid() 
{
    PID_str="unknown"
    PID_str=$PID
    echo "Waiting on PID: $PID"
    wait $PID
    unset PID
    echo "Done waiting on $PID_str"
    PID_str="unknown"
}

put_sensors_sw_standby()
{
    echo "Entering put_sensors_sw_standby"
    if [ "$1" = "ab" ] || [ "$1" = "AB" ]; then
        # AB:
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xFE 0x07 0x00 0x00 0x6C 0x02 \
             0x01 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w
        busybox usleep 10000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0x83 0x00 0xFE 0x07 0x00 0x00 > \
             /sys/class/light_ccb/i2c_interface/i2c_w
        busybox usleep 10000

    elif [ "$1" = "bc" ] || [ "$1" = "BC" ]; then
        # BC:
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xC0 0xFF 0x00 0x00 0x6C 0x02 \
             0x01 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w
        busybox usleep 10000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0x83 0x00 0xC0 0xFF 0x00 0x00 > \
             /sys/class/light_ccb/i2c_interface/i2c_w
        busybox usleep 10000
    elif [ "$1" = "c" ] || [ "$1" = "C" ]; then
        # C:
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0x00 0xF8 0x00 0x00 0x6C 0x02 \
             0x01 0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w
        busybox usleep 10000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0x83 0x00 0x00 0xF8 0x00 0x00 > \
             /sys/class/light_ccb/i2c_interface/i2c_w
        busybox usleep 10000
    fi
}

start_sensors_streaming()
{
    echo "Entering start_sensors_streaming"
    #echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xFE 0x07 0x00 0x00 0x6C 0x02 0x01 \
    #     0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
    #busybox usleep 10000
    ##do_wait_pid
    #echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0x83 0x00 0xFE 0x07 0x00 0x00 > \
    #     /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
    #busybox usleep 10000
    ##do_wait_pid
    if [ "$1" = "ab" ] || [ "$1" = "AB" ]; then
        # AB capture group
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xFE 0x07 0x00 0x00 0x6C 0x02 \
             0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit"
        busybox usleep 250000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0x83 0x00 0xFE 0x07 0x00 0x00 > \
             /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit again"
        busybox usleep 250000
    elif [ "$1" = "bc" ] || [ "$1" = "BC" ]; then
        # BC capture group
        #echo "echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xC0 0xFF 0x00 0x00 0x6C 0x02 0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!"
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xC0 0xFF 0x00 0x00 0x6C 0x02 0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit"
        busybox usleep 250000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0x83 0x00 0xC0 0xFF 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit again"
        busybox usleep 250000
    elif [ "$1" = "c" ] || [ "$1" = "C" ]; then
        # C capture group
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0x00 0xF8 0x01 0x00 0x6C 0x02 \
             0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit"
        busybox usleep 250000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0x83 0x00 0x00 0xF8 0x01 0x00 > \
             /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit again"
        busybox usleep 250000
    fi
}

start_sensors_streaming_offsets()
{
    echo "Entering start_sensors_streaming_offsets"
    if [ "$1" = "ab" ] || [ "$1" = "AB" ]; then
        # AB capture group
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xFE 0x07 0x00 0x00 0x6C 0x02 \
             0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit"
        busybox usleep 250000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0xF5 0x00 0xFE 0x07 0x00 0x00 > \
             /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit again"
        busybox usleep 250000
    elif [ "$1" = "bc" ] || [ "$1" = "BC" ]; then
        # BC capture group
        echo "echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xC0 0xFF 0x00 0x00 0x6C 0x02 0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!"
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0xC0 0xFF 0x00 0x00 0x6C 0x02 0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit"
        busybox usleep 250000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0xF5 0x00 0xC0 0xFF 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit again"
        busybox usleep 250000
    elif [ "$1" = "c" ] || [ "$1" = "C" ]; then
        # C capture group
        echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0x00 0xF8 0x00 0x00 0x6C 0x02 \
             0x01 0x00 0x01 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit"
        busybox usleep 250000
        echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0xF5 0x00 0x00 0xF8 0x00 0x00 > \
             /sys/class/light_ccb/i2c_interface/i2c_w & PID=$!
        echo "Letting sensors stream for a bit again"
        busybox usleep 250000
    fi
}

modify_llplck()
{
    echo "Entering modify_llplck"
    echo 17 0x0000 0x4E 0x00 0x00 0x01 0x0C 0x82 0x00 0x36 0x00 0x00 0x00 0x6C 0x03 0x30 \
         0x0C 0x0E 0xD8 > /sys/class/light_ccb/i2c_interface/i2c_w
    busybox usleep 10000
    #do_wait_pid
    echo 11 0x0000 0x4E 0x00 0x00 0x01 0x06 0x83 0x00 0x36 0x00 0x00 0x00 > \
         /sys/class/light_ccb/i2c_interface/i2c_w
    busybox usleep 10000
    #do_wait_pid
}

setup_rdi_capture()
{
    echo "Entering setup_rdi_capture"
    echo 1 > /sys/class/light_ccb/common/manual_control
    busybox usleep 10000
    echo 30 > /sys/class/msm_csid/msm_csid0/mipi_input_type
    busybox usleep 10000
    echo 30 > /sys/class/msm_csid/msm_csid2/mipi_input_type
    busybox usleep 10000
}

setup_preview()
{
    echo "Entering setup_preview"
    busybox usleep 10000
    echo 0 > /sys/class/msm_csid/msm_csid0/mipi_input_type
    busybox usleep 10000
    echo 0 > /sys/class/msm_csid/msm_csid2/mipi_input_type
    busybox usleep 10000
}

program_sync_offsets() 
{
    echo "Entering program_sync_offsets"
    echo 27 0x0000 0x4E 0x00 0x00 0x01 0x16 0xF0 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
         0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 > \
         /sys/class/light_ccb/i2c_interface/i2c_w
    #do_wait_pid
    busybox usleep 100000

    echo 27 0x0000 0x4E 0x00 0x00 0x01 0x16 0xF1 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
         0x00 0xD1 0x01 0x00 0x2D 0xE8 0x00 0x80 0x96 0xD1 0x01 0x00 0x2D > \
         /sys/class/light_ccb/i2c_interface/i2c_w
    #do_wait_pid
    #echo 27 0x0000 0x4E 0x00 0x00 0x01 0x16 0xF1 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00\
    #     0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
    #      > /sys/class/light_ccb/i2c_interface/i2c_w
    busybox usleep 100000

    echo 31 0x0000 0x4E 0x00 0x00 0x01 0x1A 0xF2 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
         0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 \
         0x00 0x00 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w
    #do_wait_pid
    busybox usleep 100000
}



################################################################################
#                       START OF SCRIPT EXECUTION                              #
################################################################################
    echo 1 > /sys/class/light_ccb/common/manual_control
    
    # ARGUMENTS:
    # Required:
    # $1: RDI group
    # $2: Filename
    # $3: Output file path
    # $4: Trigger/I2C
    # Optional:
    # The last argument is always restore, if present
    # Last argument: 
    # ${@:$#}

    #last=${@:$#}
    last=\${$#}
    
    now=$(date +"%Y.%H.%M.%S")
    echo ""
    echo ""
    echo ""
    echo ""
    echo "################# STARTING CAPTURE SCRIPT #######################"
    echo $(($(date +'%s * 1000 + %-N / 1000000')))
    device_file="/data/device_id.txt"

    # increase the VFE timeout
    setprop persist.camera.vfe.timeout 30

    # to start, assume that the user will only be running one preview 
    # application at a time. this preview application will also be one
    # Joe's apps, and hence have the "co.light" string prepended to its
    # package name/app identifier. 

    app_name="co.light.*"

    # Get the process list, search for the apps that have our 'co.light' string
    # prepended, and get the specific name afterward. We don't know the specific
    # name until we check, because the user could be using any one of Joe's 
    # apps. 

    # this behavior will not work if the user is running more than one 
    # Light APK....

    running_app=$(ps | grep $app_name | busybox awk '{ print $9 }')
    if [ "$running_app" = "" ]; then
        # check for camera2
        app_name="camera2"
        running_app=$(ps | grep $app_name | busybox awk '{ print $9 }')
    fi
    echo running_app: $running_app
    if [ "$running_app" = "" ]; then
        echo No preview app running!
    else
        if [ "$running_app" = "co.light.rawtest.app" ]; then
            # the rawtest app has a different class name, see Joe for details
            app_launch="$running_app/$running_app.ActivityMain"
        elif [ "$running_app" = "com.android.camera2" ]; then
            echo Camera2 detected. Cannot restore Camera2 yet...
        else
            app_launch="$running_app/$running_app.MainActivity"
        fi

        # Kill this app after storing its name
        kill $(ps | grep $running_app | busybox awk '{ print $2 }')
        busybox usleep 1000000
    fi

    if [ -f $device_file ]; then
        device_id=$(cat $device_file)
        echo "This Device : $device_id"
    else
        device_id="unknown"
        echo $device_id
        echo "device_id.txt file not present in /data/"
    fi

    echo "Previewing Off"
    echo 7 0x0000 0x4E 0x00 0x00 0x01 0x02 0xB4 0x00 > /sys/class/light_ccb/i2c_interface/i2c_w
    busybox usleep 10000
    
    if [ "$4" = "trigger" ] || [ "$4" = "Trigger" ]; then 
        echo "Using trigger mode in capture_new.sh\n";
    else
        echo "Using I2C mode in capture_new.sh\n";
        #First put all modules requested for sync into SW_STANDBY
        echo "First put all modules requested for sync into SW_STANDBY"
        put_sensors_sw_standby $1

        #Put all modules requested for sync into STREAMING
        echo "Put all modules requested for sync into STREAMING"
        start_sensors_streaming $1
    fi

    #Setup_rdi_capture
    echo "setup_rdi_capture"
    setup_rdi_capture

    #echo [`date +"%Y %m-%d, %H:%M:%S"`]: "<START>"

    filename=""
    if [ "$2" = "" ] || [ "$2" = "restore" ] || [ "$2" = "Restore" ]; then 
        # no filename, use default
        filename="default_filename"
    else 
        filename=$2
    fi
    echo Filename is: $filename

    filepath=""
    if [ "$3" = "" ] || [ "$3" = "restore" ] || [ "$3" = "Restore" ]; then 
        # no filepath, use default
        filepath="/sdcard/DCIM/rdi/"
    else 
        filepath=$3
    fi
    echo Filepath is: $filepath

    ################### MM-QCAMERA-APP CALLED HERE ########################

    echo "calling mmq-camera-app"
    echo $(($(date +'%s * 1000 + %-N / 1000000')))
    #Run the mm-qcamera-app
    mm-qcamera-app $1 $filename $filepath $4 & PID=$!

    #Now wait on mm-qcamera process
    echo "Waiting for mm-qcamera-app to finish..."
    do_wait_pid
    echo $(($(date +'%s * 1000 + %-N / 1000000')))
    echo "Done with mm-qcamera-app"
    echo [`date +"%Y %m-%d, %H:%M:%S"`]: "<END>"
    
    #######################################################################

    #Sensors in SW standby mode
    #echo "Put all modules requested for sync into SW_STANDBY"
    #put_sensors_sw_standby $1

    # setup_CS_preview
    echo "setup_CS_preview"
    setup_preview

    # check if the user has requested to restore the previewing app, and reopen
    # it if so 
    if [ "$last" = "restore" ] || [ "$last" = "Restore" ]; then # restoring preview
        if [ "$running_app" = "" ]; then
            echo No preview app was running, nothing to restore 
            echo Restoring the running preview APK...
        else
            am start -n $app_launch & PID=$!
        fi
    fi

    # stream/preview a camera
    #if [ "$1" = "ab" ] || [ "$1" = "AB" ]; then
    #    # AB RDI capture group, turn on C1
    #    busybox usleep 10000
    #    echo 11 0x0000 0x82 0x00 0x00 0x08 0x00 0x6c 0x01 0x01 0x00 0x00 0x01 > \
    #         /sys/class/light_ccb/i2c_interface/i2c_w
    #    busybox usleep 10000
    #    echo 7 0x0000 0x4E 0x00 0x00 0x01 0x02 0xB4 0x0B > \
    #         /sys/class/light_ccb/i2c_interface/i2c_w
    #    busybox usleep 10000
    #elif [ "$1" = "bc" ] || [ "$1" = "BC" ] || [ "$1" = "c" ] || [ "$1" = "C" ]; then
    #    # BC or C RDI capture group, turn on A1
    #    busybox usleep 10000
    #    echo 11 0x0000 0x82 0x00 0x02 0x00 0x00 0x6c 0x01 0x01 0x00 0x00 0x01 > \
    #         /sys/class/light_ccb/i2c_interface/i2c_w
    #    busybox usleep 10000
    #    echo 7 0x0000 0x4E 0x00 0x00 0x01 0x02 0xB4 0x01 > \
    #         /sys/class/light_ccb/i2c_interface/i2c_w
    #    busybox usleep 10000
    #fi


    echo "################# END OF CAPTURE SCRIPT #######################"
    echo ""
    echo ""
    echo ""
    echo ""

