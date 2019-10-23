#!/bin/bash

# Cut #4 "https://www.hackerrank.com/challenges/text-processing-cut-4/problem"

while read line; do
    echo "${line:0:4}"
done

# You can do the same using cut -c-4 as well
