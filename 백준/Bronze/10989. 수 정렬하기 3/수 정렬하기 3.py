import sys
nums = [0]*10001
for i in range(int(sys.stdin.readline())):
    nums[int(sys.stdin.readline())] += 1
for j in range(len(nums)):
    if nums[j] != 0:
        for k in range(nums[j]):
            print(j)