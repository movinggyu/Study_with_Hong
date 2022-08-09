import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
q = deque(list(range(1,n+1)))
result = []
cnt = 1
while q:
    if cnt == k:
        result.append(str(q.popleft()))
        cnt = 1
    else:
        q.append(q.popleft())
        cnt += 1
print("<"+", ".join(result)+">")