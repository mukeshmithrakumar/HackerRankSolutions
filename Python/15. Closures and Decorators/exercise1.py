# Standardize Mobile Number Using Decorators "https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem"


def wrapper(f):
    def fun(l):
        # complete the function
        f("+91 " + c[-10:-5] + " " + c[-5:] for c in l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    line = [input() for _ in range(int(input()))]
    sort_phone(line)
