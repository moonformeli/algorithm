import sys

queue = []

n = int(sys.stdin.readline())
for _ in range(n):
    command = sys.stdin.readline().split()

    c = command[0]
    if c == "push":
        queue.append(int(command[1]))
    elif c == "pop":
        print(-1 if len(queue) == 0 else queue.pop(0))
    elif c == "size":
        print(len(queue))
    elif c == "empty":
        print(1 if len(queue) == 0 else 0)
    elif c == "front":
        print(-1 if len(queue) == 0 else queue[0])
    elif c == "back":
        print(-1 if len(queue) == 0 else queue[-1])
