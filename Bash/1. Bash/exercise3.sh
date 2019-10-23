#!/bin/bash

# Getting started with conditionals "https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem"

read char

# Note that spaces are required inside square brackets
if [ "$char" == "Y" ] || [ "$char" == "y" ]; then
    echo YES
else
    echo NO
fi

# The above code can also be written as below where:
# echo -e where echo prints YES and NO in two different lines
# The pipe operator (|) passes the string as an argument to the grep program.
# i ignores case and grep returns whole line char in which pattern is matched

# echo -e "YES\nNO\n" | grep -i $char
