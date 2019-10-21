#!/bin/bash

# Cut #7 "https://www.hackerrank.com/challenges/text-processing-cut-7/problem"

while read line; do
    echo "$line" | cut -d $' ' -f4
done

