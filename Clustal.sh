#!/bin/bash

WHITE="\e[39m"
RED="\e[31m"
GREEN="\e[32m"

[[ -z $1 ]] && echo -e ${RED}Missing path${WHITE} && exit

DIR=${1}
echo $DIR
echo "`ls $DIR`"

for file in `ls $DIR`; do
	~/./clustalo-1.2.4-Ubuntu-x86_64 -i $DIR$file'/'$file'_sequences.fa' -o $DIR$file'/'$file'_MSA.fa' --outfmt=fa
done
