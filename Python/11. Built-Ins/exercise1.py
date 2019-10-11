# Zipped! "https://www.hackerrank.com/challenges/zipped/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split())

sheet = [map(float, input().split()) for _ in range(x)]
print(*[sum(i) / len(i) for i in zip(*sheet)], sep='\n')
