import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(" ")))
s = set(arr)

for i in range(1, n+1):
    if i not in s:
        print(i)

