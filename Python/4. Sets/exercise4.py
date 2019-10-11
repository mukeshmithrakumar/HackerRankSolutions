# Set .discard(), .remove() & .pop() "https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem"

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split() + ['']))

print(sum(s))
