#!/bin/bash
i=0
if [[ $1 = "ab" ]];then
    while true
    do
    i=$(($i+1))
    echo "Loop $i"
    ./capture_lcc.sh ab
    done
elif [[ $1 = "bc" ]]; then
    while true
    do
    i=$(($i+1))
    echo "Loop $i"
    ./capture_lcc.sh bc
    done
elif [[ $1 = "c" ]]; then
    while true
    do
        i=$(($i+1))
        echo "Loop $i"
        ./capture_lcc.sh c
    done
elif [[ $1 = "abc" ]]; then
    while true
    do
        i=$(($i+1))
        echo "Loop $i"
        ./capture_lcc.sh abc
    done
else
    while true
    do
        i=$(($i+1))
        echo "Loop $i"
        ./capture_lcc.sh ab
        ./capture_lcc.sh bc
        ./capture_lcc.sh c
        ./capture_lcc.sh abc
    done
fi
