#!/bin/bash

# Cut #1 "https://www.hackerrank.com/challenges/text-processing-cut-1/problem"

# Reads line and then from $splits line from index 2 and gets 1 letter
while read line; do
	echo "${line:2:1}"
done
