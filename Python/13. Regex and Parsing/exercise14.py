# Validating Credit Card Numbers "https://www.hackerrank.com/challenges/validating-credit-card-number/problem"

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re


TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")
