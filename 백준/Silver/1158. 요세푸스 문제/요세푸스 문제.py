import sys

c = input().split()
n = int(c[0])
k = int(c[1])

queue = []
for i in range(n):
    queue.append(i + 1)


res = "<"
i = 0
while len(queue) > 0:
    i = (i + k - 1) % len(queue)
    if len(res) > 1:
        res += ", "

    res += str(queue.pop(i))

res += ">"

print(res)
