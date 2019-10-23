#!/bin/bash

# Cut #6 "https://www.hackerrank.com/challenges/text-processing-cut-6/problem"

while read line; do
    echo "$line" | cut -c13-
done

