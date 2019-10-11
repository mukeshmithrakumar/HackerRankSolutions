# Lists "https://www.hackerrank.com/challenges/python-lists/problem"

n = input()
l = [] # noqa
for _ in range(int(n)):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l." + cmd)
    else:
        print(l)
