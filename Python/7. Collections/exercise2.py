# DefaultDict Tutorial "https://www.hackerrank.com/challenges/defaultdict-tutorial/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

d, n = defaultdict(list), list(map(int, input().split()))

for i in range(n[0]):
    d[input()].append(i + 1)

for i in range(n[1]):
    print(' '.join(map(str, d[input()])) or -1)
