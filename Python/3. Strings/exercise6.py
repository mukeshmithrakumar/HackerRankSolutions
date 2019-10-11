# String Validators "https://www.hackerrank.com/challenges/string-validators/problem"

if __name__ == '__main__':
    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))
