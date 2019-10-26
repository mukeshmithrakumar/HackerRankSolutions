# itertools.permutations() "https://www.hackerrank.com/challenges/itertools-permutations/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

perm, k = input().split()

print(*[''.join(i) for i in permutations(sorted(perm), int(k))], sep='\n')
