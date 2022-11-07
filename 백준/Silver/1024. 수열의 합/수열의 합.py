import sys
from collections import deque

result = deque()
N, L = map(int, sys.stdin.readline().split())
start = N // L
result.append(start)
cnt = 1
toggle = True

while True:
    if toggle:
        result.append(start + cnt)
        toggle = not toggle
    else:
        if start - cnt < 0:
            result.clear()
            result.append(-1)
            break
        result.appendleft(start - cnt)
        toggle = not toggle
        cnt += 1
    if sum(result) == N:
        if len(result) > 100:
            result.clear()
            result.append(-1)
            break
        if result[0] == 1 and len(result) < L:
            result.appendleft(0)
            break
        elif len(result) < L:
            result.clear()
            result.append(-1)
            break
        else:
            break
    if sum(result) > N:
        result.clear()
        L += 1
        if L > 100:
            result.clear()
            result.append(-1)
            break
        start = N // L
        result.append(start)
        cnt = 1
        toggle = True

for i in result:
    print(i, end=" ")
