#!/bin/bash

# Middle of a Text File "https://www.hackerrank.com/challenges/text-processing-in-linux---the-middle-of-a-text-file/problem"

head -n 22 | tail -n +12

# Another option is to use sed "https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/"
# sed -n 12,22p
