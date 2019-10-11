# Set Mutations "https://www.hackerrank.com/challenges/py-set-mutations/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, arr = int(input()), set(map(int, input().split()))

for i in range(int(input())):
    cmd, b_set = input().split()[0], set(map(int, input().split()))
    (eval('arr.{}({})'.format(cmd, b_set)))

print(sum(arr))
