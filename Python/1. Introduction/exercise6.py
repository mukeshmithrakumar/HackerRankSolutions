# Write a function "https://www.hackerrank.com/challenges/write-a-function/problem"


def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
        if (year % 4 == 0):
            leap = True
    return leap
