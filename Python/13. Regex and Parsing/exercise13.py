# Validating UID "https://www.hackerrank.com/challenges/validating-uid/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


no_repeats = r"(?!.*(.).*\1)"
two_or_more_upper = r"(?=(?:.*[A-Z]){2,})"
three_or_more_digits = r"(?=(?:.*\d){3,})"
ten_alphanumerics = r"[a-zA-Z0-9]{10}"
filters = no_repeats, two_or_more_upper, three_or_more_digits, ten_alphanumerics

for uid in [input() for _ in range(int(input()))]:
    if all([re.match(f, uid) for f in filters]):
        print("Valid")
    else:
        print("Invalid")
