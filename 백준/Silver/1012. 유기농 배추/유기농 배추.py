from collections import deque
import sys
testCase = int(sys.stdin.readline())
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(testCase):
    cnt = 0
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[True for _ in range(m+2)] for __ in range(n+2)]
    cabbage = deque()
    q = deque()

    # 배추위치 false로 바꾸기 및 배추목록에 추가
    for _ in range(k):
        X, Y = map(int, sys.stdin.readline().split())
        cabbage.append([X+1,Y+1])
        farm[Y+1][X+1] = False

    # 배추위치 꺼내서 주변꺼 다 True로 바꿔주기
    while cabbage:
        temp = cabbage.popleft()
        if not farm[temp[1]][temp[0]]:
            q.append(temp)
            cnt += 1
            while q:
                cab = q.popleft()
                farm[cab[1]][cab[0]] = True

                #주변애들 더해주기
                for i,j in zip(dx,dy):
                    if not farm[cab[1]+j][cab[0]+i]:
                        farm[cab[1] + j][cab[0] + i] = True
                        q.append([cab[0]+i,cab[1]+j])
                # print(q)
    print(cnt)

    # print()
    # for i in range(len(farm)):
    #     for j in range(len(farm[i])):
    #         print(farm[i][j], end=' ')
    #     print()