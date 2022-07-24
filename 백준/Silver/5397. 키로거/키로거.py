import sys

for _ in range(int(sys.stdin.readline())):
    key = sys.stdin.readline().rstrip()
    result = []
    imsi = []
    for i in key:
        if i == "<":
            if result:
                imsi.append(result.pop())
        elif i == "-":
            if result:
                result.pop()
        elif i == ">":
            if imsi:
                result.append(imsi.pop())
        else:
            result.append(i)
    while imsi:
        result.append(imsi.pop())
    print(''.join(result))
