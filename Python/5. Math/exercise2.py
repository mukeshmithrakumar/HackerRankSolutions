# Mod Divmod "https://www.hackerrank.com/challenges/python-mod-divmod/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b = (int(input()) for _ in range(2))
print(a // b)
print(a % b)
print(divmod(a, b))
