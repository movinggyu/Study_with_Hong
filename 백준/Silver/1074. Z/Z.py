import sys

N, r, c = map(int, sys.stdin.readline().split())
r,c = r+1, c+1
cnt = 0

while N > 0:
    temp = cnt
    half = 2**(N-1)

    if r <= half and c <= half:  # 1사분면
        cnt += (half**2) * 0

    elif r <= half < c:  # 2사분면
        cnt += (half**2) * 1
        c-=half

    elif r > half >= c:  # 3사분면
        cnt += (half**2) * 2
        r-=half

    elif r > half and c > half:  # 4사분면
        cnt += (half**2) * 3
        r-=half
        c-=half

    N -= 1
print(cnt)
