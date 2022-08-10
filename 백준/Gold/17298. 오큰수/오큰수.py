import sys

n = int(sys.stdin.readline())
series = list(map(int,sys.stdin.readline().split()))
result = [-1]
maxNums = []

for _ in range(len(series)):
    temp = series.pop()
    while True:
        if not maxNums:
            result.append(-1)
            break
        elif temp < maxNums[-1]:
            result.append(maxNums[-1])
            break
        else:
            maxNums.pop()
    maxNums.append(temp)

for _ in range(len(result)-1):
    print(result.pop(),end = " ")