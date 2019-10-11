# Any or All "https://www.hackerrank.com/challenges/any-or-all/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, pal_int = int(input()), list(map(int, input().split()))

print(all(i > 0 for i in pal_int) and any(str(i) == str(i)[::-1] for i in pal_int))
