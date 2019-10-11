# Find the Runner-Up Score! "https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem"

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new = set(arr)
    new.remove(max(new))
    print(max(new))
