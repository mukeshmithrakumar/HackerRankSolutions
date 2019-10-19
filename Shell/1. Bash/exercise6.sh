#!/bin/bash

# The World of Numbers "https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers/problem"

read x
read y

echo $((x + y))
echo $((x - y))
echo $((x * y))
echo $((x / y))

# The above code can also be written as below where:
# printf is similar to printf in C,
# %s is print as string
# The full form of bc is Bash Calculator.
# It is used for performing floating-point mathematical operations.
# The pipe operator (|) passes this string as an argument to the bc program.

# printf "%s\n" $x{+,-,*,/}"($y)" | bc
