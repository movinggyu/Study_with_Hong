import sys

fibo1 = 0
fibo2 = 1
num = int(sys.stdin.readline())
if num > 1:
    for i in range(num-1):
        temp = fibo2
        fibo2 = fibo1+fibo2
        fibo1 = temp
print(fibo2)