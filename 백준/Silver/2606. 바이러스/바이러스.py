import queue
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
computers = [False for _ in range(n)]
connects = {i:[] for i in range(1,n+1)}

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    connects[a].append(b)
    connects[b].append(a)

q = queue.Queue()
q.put(1)
while not q.empty():
    temp = q.get()
    if computers[temp-1]:
        continue
    else:
        computers[temp-1] = True
        for _ in range(len(connects[temp])):
            q.put(connects[temp].pop())

cnt = 0
for i in computers:
    if i:
        cnt+=1
print(cnt-1)