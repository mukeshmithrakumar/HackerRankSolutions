# collections.Counter() "https://www.hackerrank.com/challenges/collections-counter/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

x = int(input())
sizes = list(map(int, input().split()))
s_sizes = Counter(sizes)

revenue = []

for _ in range(int(input())):
    inp = input().split()
    size, price = int(inp[0]), int(inp[1])
    if s_sizes[size] > 0:
        revenue.append(1 * price)
    s_sizes[size] -= 1

print(sum(revenue))
