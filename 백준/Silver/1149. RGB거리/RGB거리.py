import sys
sys.setrecursionlimit(10**6)

testCase = int(sys.stdin.readline())
houses = []
memo = []
for _ in range(testCase):
    houses.append(list(map(int, sys.stdin.readline().split())))
    memo.append([False, False, False])


def price(lst, n, m, k):
    if n == k - 1:
        return lst[n][m]
    if memo[n][m]:
        return memo[n][m]

    delta = [0, 1, 2]
    del delta[m]

    now = lst[n][m]
    left = price(lst, n + 1, delta[0], k)
    right = price(lst, n + 1, delta[1], k)

    if left < right:
        memo[n][m] = now + left
        return memo[n][m]
    else:
        memo[n][m] = now + right
        return memo[n][m]


answer = [price(houses, 0, 0, testCase), price(houses, 0, 1, testCase), price(houses, 0, 2, testCase)]
print(min(answer))
