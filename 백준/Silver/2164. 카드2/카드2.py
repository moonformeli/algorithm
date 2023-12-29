import sys

n = int(sys.stdin.readline())
queue = [(i + 1) for i in range(n)]

t = 0
head = 0
while head != len(queue) - 1:
    if t % 2 != 0:
        queue.append(queue[head])
    head += 1
    t += 1

print(queue[head])
