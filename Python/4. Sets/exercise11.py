# Check Subset "https://www.hackerrank.com/challenges/py-check-subset/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    print(a.issubset(b))
