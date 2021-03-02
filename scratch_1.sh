#!/usr/bin/env bash

#WHITE="\e[39m"
#RED="\e[31m"
#GREEN="\e[32m"
#
##./scratch_1.sh /mnt/c/Users/User/PycharmProjects/Shell_Project/Data_02_13_2020  /mnt/c/Users/User/PycharmProjects/Shell_Project/Data_02_13_2020_data
#diff -q /mnt/c/Users/User/PycharmProjects/Shell_Project/Data_02_13_2020  /mnt/c/Users/User/PycharmProjects/Shell_Project/Data_02_13_2020_data
#
#[[ -z $1 ]] && echo -e ${RED}Missing path${WHITE} && exit
#[[ -z $2 ]] && echo -e ${RED}Missing path${WHITE} && exit

DIR1=${1}
#DIR2=${2}

echo $DIR1
#echo "`ls $DIR1`"
#echo $DIR2
#echo "`ls -LR $DIR2`"

cd $DIR1
find -not -empty -type f -printf "%s\n" | sort -rn | uniq -d | xargs -I{} -n1 find -type f -size {}c -print0 | xargs -0 md5sum | sort | uniq -w32 --all-repeated=separate


#for file in `ls $DIR`; do
#	~/./clustalo-1.2.4-Ubuntu-x86_64 -i $DIR$file'/'$file'_sequences.fa' -o $DIR$file'/'$file'_MSA.fa' --outfmt=fa
#done