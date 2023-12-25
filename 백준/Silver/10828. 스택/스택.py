import sys

n = int(sys.stdin.readline())

stack = []


def push(x: int):
    stack.append(x)


def size():
    print(len(stack))


def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop(-1)


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


for i in range(n):
    c = sys.stdin.readline().split()

    if c[0] == "push":
        push(int(c[1]))
    elif c[0] == "pop":
        pop()
    elif c[0] == "top":
        top()
    elif c[0] == "size":
        size()
    elif c[0] == "empty":
        empty()
