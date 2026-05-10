import sys
input = sys.stdin.readline

s = input().strip()
max_len = 0
l = 0
prev_char = ''
length = 0

for r in range(0, len(s)):
    char = s[r]
    if char != prev_char:
        prev_char = char
        length = 1
    else:
        length += 1
    max_len = max(max_len, length)

print(max_len)
