# itertools.combinations() "https://www.hackerrank.com/challenges/itertools-combinations/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

comb, k = input().split()

for j in range(1, int(k) + 1):
    print(*[''.join(i) for i in combinations(sorted(comb), j)], sep='\n')
