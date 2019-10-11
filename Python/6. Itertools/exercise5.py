# Compress the String! "https://www.hackerrank.com/challenges/compress-the-string/problem"

from itertools import groupby

num = list(map(int, input()))
dic = []

for k, v in groupby(num, key=None):
    print((len(list(v)), k), end=' ')

# print(*[(len(list(v)), int(k)) for k, v in groupby(input())])
