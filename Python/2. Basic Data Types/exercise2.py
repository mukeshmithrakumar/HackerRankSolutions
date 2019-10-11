# Tuples "https://www.hackerrank.com/challenges/python-tuples/problem"

if __name__ == '__main__':
    n = int(input())
    integer_tuple = tuple(map(int, input().split()))
    print(hash(integer_tuple))
