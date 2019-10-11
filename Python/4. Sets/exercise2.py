# Symmetric Difference "https://www.hackerrank.com/challenges/symmetric-difference/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
a = set(map(int, input().split()))

m = input()
b = set(map(int, input().split()))

diff = list(a.difference(b)) + list(b.difference(a))
diff_sort = sorted(diff)
print(*diff_sort, sep="\n")
