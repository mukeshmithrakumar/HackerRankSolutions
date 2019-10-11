# Map and Lambda Function "https://www.hackerrank.com/challenges/map-and-lambda-expression/problem"

cube = lambda x: pow(x, 3) # noqa


def fibonacci(n):
    lis = [0, 1]
    for i in range(2, n):
        lis.append(lis[i - 2] + lis[i - 1])
    return(lis[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
