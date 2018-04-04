#!/bin/bash
declare -A animals
animals=( \
	["moo"]=1 \
	["woof"]=2\
	)
a=${animals[moo]}
b=${animals[woof]}
a=$(($a+$b))
echo "$a"