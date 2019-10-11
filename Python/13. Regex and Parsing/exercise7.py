# Validating phone numbers "https://www.hackerrank.com/challenges/validating-the-phone-number/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    print("YES" if re.match(r'^[789]\d{9}$', input()) else "NO")
