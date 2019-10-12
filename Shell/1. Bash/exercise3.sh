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
# grep i where i ignores case and grep returns whole line in which pattern is matched
# read char; echo -e "YES\nNO\n" | grep -i $char
