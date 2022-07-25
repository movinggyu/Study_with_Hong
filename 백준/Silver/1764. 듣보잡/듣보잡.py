import sys

hear = set()
see = set()
n, m = map(int,sys.stdin.readline().split())
for i in range(n):
    hear.add(sys.stdin.readline().rstrip())
for j in range(m):
    see.add(sys.stdin.readline().rstrip())
result = list(hear.intersection(see))
result.sort()
print(len(result))
print("\n".join(result))