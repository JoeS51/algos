import sys
input = sys.stdin.readline

n = int(input())
res = [str(n)]

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n + 1
    res.append(str(n))

print(" ".join(res))

