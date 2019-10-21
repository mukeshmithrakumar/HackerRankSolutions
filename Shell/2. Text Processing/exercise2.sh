#!/bin/bash

# Cut #2 "https://www.hackerrank.com/challenges/text-processing-cut-2/problem"

# cut is the utility for cutting sections from each line of files
# To cut by character use the -c option
while read line; do
    echo "$line" | cut -c2,7
done
