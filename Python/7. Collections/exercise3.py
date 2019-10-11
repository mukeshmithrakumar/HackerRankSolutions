# Collections.namedtuple() "https://www.hackerrank.com/challenges/py-collections-namedtuple/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
fields = input().split()
students = namedtuple('student', fields)

total = 0
for i in range(N):
    field1, field2, field3, field4 = input().split()
    student = students(field1, field2, field3, field4)
    total += int(student.MARKS)
print('{:.2f}'.format(total / N))
