# Set .difference() Operation "https://www.hackerrank.com/challenges/py-set-difference-operation/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
english = set(map(int, input().split()))

m = input()
french = set(map(int, input().split()))

both = english - french
print(len(both))
