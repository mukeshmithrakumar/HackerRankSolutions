# itertools.combinations_with_replacement() "https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

c, k = input().split()

print(*[''.join(i) for i in combinations_with_replacement(sorted(c), int(k))], sep='\n')
