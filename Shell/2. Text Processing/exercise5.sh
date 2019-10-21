#!/bin/bash

# Cut #5 "https://www.hackerrank.com/challenges/text-processing-cut-5/problem"

# d is for delimeter and $'\t' is about the tab seperator and f specifies the fields from 1-3
while read line; do
    echo "$line" | cut -d $'\t' -f1-3
done
