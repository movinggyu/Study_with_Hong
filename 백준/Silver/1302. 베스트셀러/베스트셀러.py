import sys

books = {}
for _ in range(int(sys.stdin.readline())):
    name = sys.stdin.readline().rstrip()
    if name not in books.keys():
        books[name] = 1
    else:
        books[name] += 1
result = [x for x in books.keys() if books[x] == max(books.values())]
result.sort()
print(result[0])