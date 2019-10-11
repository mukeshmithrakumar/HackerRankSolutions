# Collections.OrderedDict() "https://www.hackerrank.com/challenges/py-collections-ordereddict/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

market = OrderedDict()

for i in range(int(input())):
    item, space, price = input().rpartition(" ")
    market[item] = market.get(item, 0) + int(price)

print(*[" ".join([item, str(price)]) for item, price in market.items()], sep="\n")
