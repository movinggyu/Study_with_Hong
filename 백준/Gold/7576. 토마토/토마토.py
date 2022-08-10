from collections import deque
import sys

m, n = map(int,sys.stdin.readline().split())
box = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
check = [[False for _ in range(m)] for __ in range(n)]
q = deque()

#1과 -1위치 체크 : 체크하고 시작위치 찾아야되기 때문에
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            check[i][j] = True
            q.append([i,j])
        if box[i][j] == -1:
            check[i][j] = True

#상하좌우 체크하면서 큐 비우고 채우고 반복
dx = [0,0,-1,1]
dy = [-1,1,0,0]
day = -1
while q:
    day += 1
    for _ in range(len(q)):
        temp = q.popleft()
        for i in range(4):
            if -1<temp[0]+dy[i]<n and -1<temp[1]+dx[i]<m: #박스 안쪽에있어야됨 무적권
                if not check[temp[0]+dy[i]][temp[1]+dx[i]]:
                    q.append([temp[0]+dy[i],temp[1]+dx[i]])
                    check[temp[0]+dy[i]][temp[1]+dx[i]] = True

#check에 False 있는지 체크 : 있다면 -1출력 없다면 day/start 출력
for i in range(n):
    for j in range(m):
        if not check[i][j]:
            day = -1
            break
print(day)