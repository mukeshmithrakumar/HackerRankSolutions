# Exceptions "https://www.hackerrank.com/challenges/exceptions/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    a, b = map(str, input().split())
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code: {}".format(e))
