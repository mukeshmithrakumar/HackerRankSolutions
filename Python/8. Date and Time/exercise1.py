# Calendar Module "https://www.hackerrank.com/challenges/calendar-module/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

user = input().split()
m = int(user[0])
d = int(user[1])
y = int(user[2])
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
