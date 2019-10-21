#!/bin/bash

# Cut #8 "https://www.hackerrank.com/challenges/text-processing-cut-8/problem"

while read line; do
    echo "$line" | cut -d' ' -f1-3
done

