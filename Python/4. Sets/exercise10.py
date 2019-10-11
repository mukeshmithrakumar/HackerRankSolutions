# The Captain's Room "https://www.hackerrank.com/challenges/py-the-captains-room/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
arr = list(map(int, input().split()))
myset = set(arr)

tot = sum(myset) * k
print((tot - sum(arr)) // (k - 1))
