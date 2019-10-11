# Word Order "https://www.hackerrank.com/challenges/word-order/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
# define empty ordered dictionary, which counts occurrences
dict = OrderedDict()

for i in range(int(input())):
    # If input not in the dictionary, then add it
    # else increment the counter
    key = input()
    if key not in dict.keys():
        dict.update({key: 1})
        continue
    dict[key] += 1

print(len(dict.keys()))
print(*dict.values())
