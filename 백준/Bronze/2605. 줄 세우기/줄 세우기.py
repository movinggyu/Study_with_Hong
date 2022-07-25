import sys

person = int(sys.stdin.readline())
nums = sys.stdin.readline().split()
result = []
imsi = []
for i in range(person):
    for _ in range(int(nums[i])):
        imsi.append(result.pop())
    result.append(str(i+1))
    while imsi:
        result.append(imsi.pop())
print(" ".join(result))