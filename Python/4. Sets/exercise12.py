# Check Strict Superset "https://www.hackerrank.com/challenges/py-check-strict-superset/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

arr = set(map(int, input().split()))

issup = []
for i in range(int(input())):
    sup = set(map(int, input().split()))
    issup.append(arr.issuperset(sup))

print(all(issup))
