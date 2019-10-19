#!/bin/bash

# Comparing Numbers "https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem"

read a
read b

if (( $a > $b )); then
    printf "X is greater than Y"

elif (( $a < $b )); then
    printf "X is less than Y"

else
    printf "X is equal to Y"

fi

# The above code can also be written as below where:
# -gt is greater than
# -lt is less than
# -eq is equal to

# [[ $a -gt $b ]] && echo 'X is greater than Y'
# [[ $a -lt $b ]] && echo 'X is less than Y'
# [[ $a -eq $b ]] && echo 'X is equal to Y'
