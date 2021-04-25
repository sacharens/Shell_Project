#!/bin/bash
#echo fuck this
# netcat tricky-guess.csa-challenge.com 2222
sleep 7
#echo -e "\n"
# Declare a string array with type
declare -a StringArray=("tqljfoenhyub" "tfnqupbmyoil" "qobztumfnyac" "wlcobqygntsu" "jzobtxduynfq" "ytdquobawnlc" "txruabyowvqn" "kwotbyrunfpq" "pmqxcutryobn" "blqoprtwnuyj" "tnzdoxuaqbyv" "joyubhngftdq" "wpymdbtuokre" "ixcndgobtuqp" "btufzokynmsh")
# Read the array values with space
COUNTER=0
for val in "${StringArray[@]}"; do
  COUNTER=$((COUNTER+1))	
  echo $val
  # echo -e "\n"
  sleep 0.5
done
b=15
if [ "$COUNTER" -ne "$b" ];then
  echo "They're not equal";
fi
